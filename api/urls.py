from django.urls import path,include
from rest_framework import routers
from superuser import views as superuser
from ticket import views as ticket

router = routers.DefaultRouter()
router.register(r'all-department', superuser.ViewAllDepartments, basename="view-departments")


urlpatterns = [
    path('user/', include('accounts.urls')),
    path('create-department/' , superuser.CreateDepartment.as_view(), name='create-department'),
    path('update-department/' , superuser.UpdateDepartment.as_view(), name='update-department'),
    path('delete-department/<str:id>/' , superuser.DeleteDepartment.as_view(), name='delete-department'),
    path('create-ticket/' , ticket.CreateTicketsView.as_view(), name='create-ticket'),
    path('update-ticket/<str:id>/' , ticket.UpdateTicketView.as_view(), name='update-ticket'),
]

urlpatterns += router.urls