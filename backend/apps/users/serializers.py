from django.conf import settings
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    registered_at = serializers.DateTimeField(
        format='%H:%M %d.%m.%Y', read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
    short_name = serializers.SerializerMethodField(read_only=True)
    token = serializers.StringRelatedField(source='auth_token.key', read_only=True)
    bio = serializers.SerializerMethodField(read_only=True)
    score = serializers.IntegerField(source='score.count', read_only=True)

    def get_avatar(self, obj):
        return obj.avatar.url if obj.avatar else settings.STATIC_URL + \
                                                 'images/default_avatar.png'

    def get_full_name(self, obj):
        return obj.full_name

    def get_short_name(self, obj):
        return obj.short_name

    def get_token(self, obj):
        if obj.token:
            return obj.token
        else:
            return None

    def get_bio(self, obj):
        return obj.bio

    def get_id(self, obj):
        return obj.id

    def get_score(self, obj):
        return obj.score

    class Meta:
        model = User
        ref_name = None
        fields = [
            'id',
            'email',
            'avatar',
            'full_name',
            'short_name',
            'registered_at',
            'token',
            'bio',
            'score']


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
