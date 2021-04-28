from django.urls import path
from .views import leads_list, leads_detail, leads_create, leads_update, leads_delete
app_name = "leads"

urlpatterns = [
    path('', leads_list, name='leads_list'),
    path('<int:pk>/', leads_detail, name='leads_detail'),
    path('create/', leads_create, name='leads_create'),
    path('update/<int:pk>', leads_update, name='leads_update'),
    path('delete/<int:pk>', leads_delete, name='leads_delete'),
]