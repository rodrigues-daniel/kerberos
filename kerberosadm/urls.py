from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'TCE - DIN - DBA - Permissions - Admin'
admin.site.site_title = 'TCE - DIN - DBA - Permissions - Admin'
admin.site.index_title = 'TCE - DIN - DBA - Permissions - Admin'

urlpatterns = [
    # ex: /polls/
    path('', views.first_view, name='first_view'),
    # ex: /polls/5/
    ]
