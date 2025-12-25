from django.urls import path
from .views import *


urlpatterns=[
    path("Author/", AuthorView.as_view()),
    path("book/", BookView.as_view()),
    path("Feedback", Feedback.as_view()),
]
