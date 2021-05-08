from django.urls import path
from .views import (
    leads_list, leads_detail, leads_create, leads_update, leads_delete, 
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
    )
app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='leads_detail'),
    path('create/', LeadCreateView.as_view(), name='leads_create'),
    path('update/<int:pk>', LeadUpdateView.as_view(), name='leads_update'),
    path('delete/<int:pk>', LeadDeleteView.as_view(), name='leads_delete'),
]