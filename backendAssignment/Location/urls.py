# urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    UserListCreateView, 
    UserRetrieveUpdateDestroyView, 
    SignInView, 
    SignOutView,
    CountryListCreateView,
    CountryRetrieveUpdateDestroyView,
    StateListCreateView,
    StateRetrieveUpdateDestroyView,
    CityListCreateView,
    CityRetrieveUpdateDestroyView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('signin/', SignInView.as_view(), name='sign-in'),
    path('signout/', SignOutView.as_view(), name='sign-out'),
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<uuid:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<uuid:pk>/', StateRetrieveUpdateDestroyView.as_view(), name='state-detail'),
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<uuid:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
]

