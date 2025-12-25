
from django.shortcuts import render
from rest_framework import generics
from .serilaizer import *
# Create your views here.


class AuthorView(generics.ListAPIView):
    queryset=Author.objects.all()
    serilaizer_class=AuthorSerializer


class BookView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer


class Feedback(generics.ListAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer



