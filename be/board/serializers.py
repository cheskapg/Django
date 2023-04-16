from rest_framework import serializers
from .models import BoardModel

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = ('__all__')

        def create(self, validated_data):
            print(validated_data)

            return BoardModel.objects.create(**validated_data)