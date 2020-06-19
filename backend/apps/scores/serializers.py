from rest_framework import serializers

from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['count', 'owner']


class ScoreWriteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Score
        fields = ['count', 'owner']
