# views.py
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer

from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer
from .permissions import IsOwner

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignInView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        from django.contrib.auth import authenticate
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class SignOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CountryListCreateView(generics.ListCreateAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Country.objects.filter(my_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(my_user=self.request.user)

class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Country.objects.filter(my_user=self.request.user)

class StateListCreateView(generics.ListCreateAPIView):
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return State.objects.filter(my_country__my_user=self.request.user)

    def perform_create(self, serializer):
        country = Country.objects.get(id=self.request.data['my_country'], my_user=self.request.user)
        serializer.save(my_country=country)

class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return State.objects.filter(my_country__my_user=self.request.user)

class CityListCreateView(generics.ListCreateAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return City.objects.filter(my_state__my_country__my_user=self.request.user)

    def perform_create(self, serializer):
        state = State.objects.get(id=self.request.data['my_state'], my_country__my_user=self.request.user)
        serializer.save(my_state=state)

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return City.objects.filter(my_state__my_country__my_user=self.request.user)
