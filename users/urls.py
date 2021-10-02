from django.urls import path, include
from .views import UserListView
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
]

