from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.

def leads_list(request):
    '''
        returns all the lead
    '''
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    
    return render(request, "leads/leads_list.html", context=context)

def leads_detail(request, pk):
    '''
        returns lead with respect to pk
    '''
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/leads_detail.html', context=context)