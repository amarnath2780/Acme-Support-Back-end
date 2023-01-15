from django.urls import path, include
from . import views



urlpatterns = [
    path('detail/<str:pk>/', views.UserView.as_view(), name='user_detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('view/<str:id>/', views.ViewUserView.as_view(), name='user_details'),
]

