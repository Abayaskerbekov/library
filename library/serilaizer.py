from rest_framework import serializers
from .models import *



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"
