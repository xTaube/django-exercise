from rest_framework import generics
from pokemon.models import Pokemon
from .serializers import PokemonSerializer
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions

class PokemonAPIView(generics.ListCreateAPIView):
    serializer_class = PokemonSerializer
    search_fields = ['type', 'pokemon_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Pokemon.objects.all()

class PokemonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    lookup_field = 'id'