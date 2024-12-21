# urls.py in accounts app
from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user_register'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutAPIView.as_view(), name='user_logout'),
]
