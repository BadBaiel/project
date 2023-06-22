from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Mentor
from .serializers import MentorSerializer, MentorDetailSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from apps.users.models import User
from rest_framework import status


class MentorAPIView(ListCreateAPIView):
    queryset = Mentor.objects.filter(is_active=True)
    serializer_class = MentorSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        serializer = MentorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        username = serializer.validated_data.get('username')
        group = serializer.validated_data.get('group')
        about_me = serializer.validated_data.get('about_me')
        contact = serializer.validated_data.get('contact')
        skills = serializer.validated_data.get('skills')
        employment = serializer.validated_data.get('employment')
        directions = Mentor.objects.filter(data=request.user.directions)
        month = Mentor.objects.filter(data=request.user.month)
        mentor = Mentor.objects.create(username=username, group=group, about_me=about_me, contact=contact, skills=skills,
                                       employment=employment, directions=directions, month=month)
        mentor.skills.set(skills)
        return Response(data=MentorSerializer(mentor).data)


class MentorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.filter(is_active=True)
    serializer_class = MentorDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class AddLike(ListCreateAPIView):
    def post(self, request, pk, *args, **kwargs):
        mentor = Mentor.objects.get(pk=pk)
        is_dislike = False

        for dislike in mentor.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if is_dislike:
            mentor.dislikes.remove(request.user)

        is_like = False

        for like in mentor.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            mentor.likes.add(request.user)

        if is_like:
            mentor.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddDislike(ListCreateAPIView):
    def post(self, request, pk, *args, **kwargs):
        mentor = Mentor.objects.get(pk=pk)
        is_like = False

        for like in mentor.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            mentor.likes.remove(request.user)

        is_dislike = False

        for dislike in mentor.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            mentor.dislikes.add(request.user)

        if is_dislike:
            mentor.dislikes.remove(request.user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)








