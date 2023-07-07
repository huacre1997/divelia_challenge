from rest_framework import serializers
from apps.toys.models import Toy, Gift
from apps.pets.models import Pet


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ['id', 'name', 'price', 'url']
        read_only_fields = ['id']

    def validate_name(self, data):

        qs = Toy.objects.filter(name=data, is_active=True)
        if qs.exists():
            raise serializers.ValidationError(
                "Ya existe un juguete con ese nombre")
        return data


class GiftSerializer(serializers.ModelSerializer):
    short_name = serializers.CharField(write_only=True)

    class Meta:
        model = Gift
        fields = ['id', 'toy', 'short_name']

    def validate_short_name(self, short_name):
        # Verificar si existe una mascota con el short_name proporcionado
        try:
            self.pet = Pet.objects.get(short_name=short_name)
        except Pet.DoesNotExist:
            raise serializers.ValidationError(
                "No se encontró una mascota con el nombre corto proporcionado.")
        return short_name

    def create(self, validated_data):

        # Crear la instancia de Gift y asociarla a la mascota
        gift = Gift.objects.create(toy=validated_data['toy'], pet=self.pet)

        return gift

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["toy"] = instance.toy.name
        data["pet"] = instance.pet.name
        return data
