from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('login/', views.login_api)
]
