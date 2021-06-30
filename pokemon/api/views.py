from rest_framework import generics
from pokemon.models import Pokemon
from .serializers import PokemonSerializer

class PokemonAPIView(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class PokemonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    lookup_field = 'id'