
from django.views.generic.list import ListView
from orgstudent.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5    
