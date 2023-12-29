from rest_framework import serializers

class RecipeSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_lenght=255)
    description = serializers.CharField(max_lenght=255)