from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PokemonAPIView
)


urlpatterns = [
    path('pokemons', PokemonAPIView.as_view())
]