from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


###################### class based views demonstration starts here ##################

class SignUpView(generic.CreateView):
    template_name = 'leads/leads_signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

    # def get_context_data(self, **kwargs):
    #     context = super(SignUpView, self).get_context_data(**kwargs)
    #     context['user_create'] = context['form']
    #     return context


class LandingPageView(generic.TemplateView):
    template_name = "landing_page.html"


class LeadListView(generic.ListView):
    queryset = Lead.objects.all()
    # model = Lead
    template_name = "leads/leads_list.html"
    # default context object passed is "object_list" --to override this
    context_object_name = 'leads'


def leads_list(request):
    '''
        returns all the lead
    '''
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }

    return render(request, "leads/leads_list.html", context=context)


class LeadDetailView(generic.DetailView):
    queryset = Lead.objects.all()
    context_object_name = "lead"
    template_name = "leads/leads_detail.html"


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


class LeadCreateView(generic.CreateView):
    form_class = LeadModelForm
    template_name = "leads/leads_create.html"

    def get_success_url(self):
        return reverse("leads:leads_list")

    def form_valid(self, form):
        send_mail(
            "Test message from gmail",
            str(form.cleaned_data),
            settings.EMAIL_HOST_USER,
            ['c0824340@mylambton.ca']
        )
        return super(LeadCreateView, self).form_valid(form)


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


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/leads_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:leads_list")


def leads_update(request, pk):
    '''
        updates lead
    '''
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(instance=lead, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('leads:leads_list')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/leads_update.html', context)


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/leads_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:leads_list")


def leads_delete(request, pk):
    '''
        deletes a record
    '''
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leads_list')
