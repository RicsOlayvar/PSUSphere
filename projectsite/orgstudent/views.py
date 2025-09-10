from django.views.generic.list import ListView
from orgstudent.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
