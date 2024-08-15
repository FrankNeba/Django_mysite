from django.urls import path

from . import views

urlpatterns = [
    path("login", views.indexes, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('question', views.question, name='question'),
    path('choice', views.choice, name='choice')
]