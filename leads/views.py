from django.shortcuts import render
from django.http import HttpResponse
from .models import Agent
# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    agent = Agent.objects.all().first()
    data = {
        'data': agent
    }
    
    return render(request, "leads/index.html", context=data)