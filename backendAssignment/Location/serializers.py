# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Country, State, City

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    country__name = serializers.SerializerMethodField()
    country__user__name = serializers.SerializerMethodField()

    class Meta:
        model = State
        fields = '__all__'

    def get_my_country__name(self, obj):
        return obj.country.name

    def get_my_country__my_user__name(self, obj):
        return obj.country.user.email

class CitySerializer(serializers.ModelSerializer):
    state__name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = '__all__'

    def get_my_state__name(self, obj):
        return obj.state.name