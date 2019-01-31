from rest_framework import serializers
from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Idea
        fields = ('id', 'name', 'owner','date_created','problem','potential_solution','likeCount', 'coderCount', 'imageURL', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')