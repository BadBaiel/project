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
    group = serializers.CharField(write_only=True)
    about_me = serializers.CharField(write_only=True)
    # skills = serializers.CharField(write_only=True)
    # employment = serializers.CharField(write_only=True)

    class Meta:
        model = Mentor
        fields = ['id', 'group', 'name', 'directions', 'month', 'contact', 'about_me', 'skills', 'employment', 'user',
                  'likes_count', 'dislikes_count', 'students_count']


class MentorListsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # skills = serializers.CharField(write_only=True)
    # employment = serializers.CharField(write_only=True)

    class Meta:
        model = Mentor
        fields = ['id', 'name', 'directions', 'month', 'contact', 'user',
                          'likes_count', 'dislikes_count', 'students_count']


class MentorDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    skills = TagSerializer(many=True)
    employment = Employment()

    class Meta:
        model = Mentor
        fields = ['id', 'group', 'name', 'about_me', 'directions', 'month', 'contact', 'skills', 'employment', 'user',
                  'likes_count', 'dislikes_count', 'students_count']




