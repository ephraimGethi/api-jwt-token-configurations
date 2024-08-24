from rest_framework import serializers
from ..models import Note


class userSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    id = serializers.IntegerField()

class NoteSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only = True)
    class Meta:
        model = Note
        fields = ['user','body']