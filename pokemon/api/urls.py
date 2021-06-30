from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import (
    PokemonAPIView,
    PokemonDetailAPIView
)


urlpatterns = [
    path('pokemons', PokemonAPIView.as_view()),
    re_path(r'pokemons/(?P<id>\d+)/$', PokemonDetailAPIView.as_view())
]