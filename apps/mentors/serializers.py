from rest_framework import serializers
from .models import Mentor, Skills, Employment
from drf_writable_nested import WritableNestedModelSerializer
from apps.users.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['text']


class Employment(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class MentorSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # user_id = serializers.IntegerField()

    skills = TagSerializer(many=True)
    employment = Employment()

    class Meta:
        model = Mentor
        fields = ['id', 'group', 'name', 'contact', 'directions', 'month', 'about_me', 'skills', 'employment', 'user',
                  'likes_count', 'dislikes_count', 'students_count']

        def create(self, validated_data):
            user_data = self.context['request'].user  # Извлекаем данные пользователя из запроса

            validated_data['user'] = user_data
            validated_data['directions'] = user_data.directions
            validated_data['month'] = user_data.month

            return super().create(validated_data)



class MentorListsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


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




