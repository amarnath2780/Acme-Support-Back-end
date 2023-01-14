from django.urls import path,include
from rest_framework import routers
from superuser import views as superuser

router = routers.DefaultRouter()



urlpatterns = [
    path('user/', include('accounts.urls')),
    path('create-department/' , superuser.CreateDepartment.as_view(), name='create-department')
]

urlpatterns += router.urls