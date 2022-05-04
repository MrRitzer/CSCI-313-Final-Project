from django.urls import path

from . import views

urlpatterns = [
    path('', views.courses_view, name='index'),
]