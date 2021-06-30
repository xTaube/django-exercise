from rest_framework import serializers
from pokemon.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [
            'user',
            'pokemon_name',
            'content',
            'image',
        ]

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None

        pokemon_name = data.get("pokemon_name", None)
        if pokemon_name == "":
            pokemon_name = None

        image = data.get("image", None)

        if content is None or pokemon_name is none or image is None:
            raise serializers.ValidationError("Pokemon name, content and image are required")
