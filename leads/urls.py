from django.urls import path
from .views import leads_list, leads_detail

app_name = "leads"

urlpatterns = [
    path('', leads_list, name='leads_list'),
    path('<pk>/', leads_detail, name='leads_detail'),
]