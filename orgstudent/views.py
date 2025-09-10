from django.shortcuts import render
from django.views.generic.list import ListView
from orgstudent.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
    
    def get_template_names(self):
        return [self.template_name]
