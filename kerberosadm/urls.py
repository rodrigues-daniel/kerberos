from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.first_view, name='first_view'),
    # ex: /polls/5/
    ]
