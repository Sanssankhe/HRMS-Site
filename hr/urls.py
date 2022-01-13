from django.contrib import admin
from django.urls import path, include
from hr import views
from django.contrib.auth.views import LoginView, LogoutView

admin.site.site_header = "SMS PVT.Ltd"
admin.site.site_title = "Welcome to HR Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Employee', views.employee, name='Employee'),
    path('task', views.task, name='task'),
    path('leave', views.leave, name='leave'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='Register'),
    path('dashboard', views.dash, name= 'Dashboard' ),
    path('log', views.log, name='log'),
]