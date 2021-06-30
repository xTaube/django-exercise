from rest_framework import serializers
from pokemon.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'user',
            'pokemon_name',
            'type',
            'description',
            'image',
        ]

    def validate(self, data):
        description = data.get("description", None)
        if description == "":
            description = None

        pokemon_name = data.get("pokemon_name", None)
        if pokemon_name == "":
            pokemon_name = None

        type = data.get("type", None)
        if type == "":
            type = None

        image = data.get("image", None)

        if description is None or pokemon_name is None or image is None or type is None:
            raise serializers.ValidationError("Pokemon name, type, description and image are required")

        return data