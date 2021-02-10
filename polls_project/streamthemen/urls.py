from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vote", views.vote, name="vote"),
    path("topic-add", views.topic_new, name="topic_new"),
    path("topic-edit", views.topic_edit, name="topic_edit"),
    path("topic-delete", views.topic_delete, name="topic_delete"),
]
