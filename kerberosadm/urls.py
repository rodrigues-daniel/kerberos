from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'Data Control Admin'
admin.site.site_title = 'Data Control Admin'
admin.site.index_title = 'Data Control Admin'

urlpatterns = [
    # ex: /polls/
    path('', views.index,name="current_datetime"),
    # ex: /polls/5/
    ]
