from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
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

# using forms.Form

# def leads_create(request):
#     '''
#         creates lead    
#     '''
#     form = LeadForm()
#     agent = Agent.objects.first()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
        
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             print(cleaned_data)
#             Lead.objects.create(
#                 first_name = cleaned_data['first_name'],
#                 last_name = cleaned_data['last_name'],
#                 age = cleaned_data['age'],
#                 agent = agent
#             )
#             return redirect('leads:leads_list')

#     context = {
#         'form': form
#     }
#     return render(request, 'leads/leads_create.html', context)

#   using forms.ModelForm


def leads_create(request):
    '''
        creates lead    
    '''
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('leads:leads_list')

    context = {
        'form': form
    }
    return render(request, 'leads/leads_create.html', context)

def leads_update(request, pk):
    '''
        updates lead
    '''
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(instance=lead,data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('leads:leads_list')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/leads_update.html', context)

def leads_delete(request, pk):
    '''
        deletes a record
    '''
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leads_list')