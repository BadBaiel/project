from rest_framework import serializers
from .models import Mentor, Skills, Employment
from drf_writable_nested import WritableNestedModelSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['text']


class Employment(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class MentorSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    skills = TagSerializer(many=True)
    employment = Employment()

    class Meta:
        model = Mentor
        fields = ['id', 'direction', 'month', 'group', 'name', 'about_me', 'contact', 'skills', 'employment', 'user']

