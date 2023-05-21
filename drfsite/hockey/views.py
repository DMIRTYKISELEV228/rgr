from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hockey, Player, Trener, Staff, Category, Post, Prof
from .serializers import HockeySerializer, PlayerSerializer, TrenerSerializer, StaffSerializer, CategorySerializer, \
    PostSerializer, ProfSerializer


class HockeyViewSet(viewsets.ModelViewSet):
    queryset = Hockey.objects.all()
    serializer_class = HockeySerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TrenerViewSet(viewsets.ModelViewSet):
    queryset = Trener.objects.all()
    serializer_class = TrenerSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProfViewSet(viewsets.ModelViewSet):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
