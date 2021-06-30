# from rest_framework import Response
from rest_framework import generics
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

class PokemonAPIView(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()