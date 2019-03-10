from rest_framework import serializers
from beer.models import Beer


class BeerSerializer(serializers.Serializer):
    class Meta:
        model = Beer
        fields = ('name', 'manufacturer')

    name = serializers.CharField()
    #manufacturer = serializers.SlugRelatedField(slug_field='name')

    def create(self, validated_data):
        return Beer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance
