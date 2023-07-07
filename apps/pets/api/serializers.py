from rest_framework import serializers
from apps.pets.models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'image', 'short_name']
        read_only_fields = ['name', 'id']

    def validate_short_name(self, data):
        if not data.isalnum():
            raise serializers.ValidationError(
                "El campo debe contener solo caracteres alfanuméricos.")
        if ' ' in data:
            raise serializers.ValidationError(
                "El campo no debe contener espacios.")

        qs = Pet.objects.filter(short_name=data, is_active=True)
        if qs.exists():
            raise serializers.ValidationError(
                "Ya existe una mascota con ese nombre corto")
        return data

    def create(self, validated_data):
        user = self.context['request'].user  # Obtener el usuario autenticado
        validated_data['owner'] = user  # Establecer el dueño
        pet = Pet.objects.create(**validated_data)
        return pet
