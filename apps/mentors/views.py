from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Mentor
from .serializers import MentorSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


class MentorAPIView(ListCreateAPIView):
    queryset = Mentor.objects.filter(is_active=True)
    serializer_class = MentorSerializer
    pagination_class = PageNumberPagination
    permission_classes = (AllowAny, )


class MentorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.filter(is_active=True)
    serializer_class = MentorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

# class MentorApiView(ModelViewSet):
#     queryset = Mentor
#     serializer_class = MentorSerializer
#     permission_classes = (IsOwnerOrReadOnly, )








