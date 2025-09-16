from django.views.generic.list import ListView
from orgstudent.models import Organization
from orgstudent.forms import OrganizationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
#from .models import OrgMember, Student, College, Program

def forms_page(request):
    return render(request, 'org_form.html')



class HomePageView(ListView):
    model = Organization
    context_object_name ='home'
    template_name = 'home.html'
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5 

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')   

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')






