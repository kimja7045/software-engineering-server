from service.models import Post
from rest_framework import serializers
from service.serializers import UserProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    has_favorite = serializers.SerializerMethodField(read_only=True)
    user = UserProfileSerializer(read_only=True)
    is_mine = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'favorite_count',
            'has_favorite',
            'is_mine',
            'created_at',
        )

    def get_is_mine(self, obj):
        if not self.context['request'].user.is_authenticated:
            return False
        return obj.user_id == self.context['request'].user.id

    def get_has_favorite(self, obj):
        return self.context['request'].user.id in [favorite_user for favorite_user in obj.favorite_users.all()]
