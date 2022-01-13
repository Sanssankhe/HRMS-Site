from django.contrib import admin
from django.urls import path, include
from apphr import views

admin.site.site_header = "SMS PVT.Ltd"
admin.site.site_title = "Welcome to HR Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('home', views.home, name='home'),
]