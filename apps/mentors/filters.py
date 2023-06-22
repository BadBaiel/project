from django_filters import rest_framework as filters
from .models import Mentor


class MentorFilter(filters.FilterSet):
    directions = filters.CharFilter()
    month = filters.CharFilter()

    class Meta:
        model = Mentor
        fields = ['directions', 'month']