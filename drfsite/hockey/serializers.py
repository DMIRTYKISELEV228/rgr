from rest_framework import serializers

from .models import Hockey, Player, Trener, Staff, Category, Post, Prof


class HockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hockey
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trener
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = "__all__"
