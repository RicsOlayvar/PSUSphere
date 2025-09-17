from django.views.generic.list import ListView
from orgstudent.models import Organization
from orgstudent.forms import OrganizationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from orgstudent.models import OrgMember, Student, College, Program 

def forms_page(request):
    return render(request, 'org_form.html')

def get_queryset(self):
    return Organization.objects.all()
 

class HomePageView(ListView):
    model = Organization
    context_object_name ='home'
    template_name = 'home.html'
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = 'organization-update'
        context['delete_url'] = 'organization-delete'
        return context


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'Organization'
        context['page_title'] = 'Add Organization'
        return context

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_list.html'
    success_url = reverse_lazy('organization-list') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'Organization'
        context['page_title'] = 'Edit Organization'
        return context  

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'Organization'
        context['page_title'] = 'Delete Organization'
        return context

# OrgMember Views
class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'org_list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return OrgMember.objects.filter(
                student__firstname__icontains=query
            ) | OrgMember.objects.filter(
                organization__name__icontains=query
            )
        return OrgMember.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = 'orgmember-edit'  
        context['delete_url'] = 'orgmember-delete'
        return context

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'org_del.html'
    success_url = reverse_lazy('orgmember-list')

#Student
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(
                firstname__icontains=query
            ) | Student.objects.filter(
                lastname__icontains=query
            )
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = 'student-edit'
        context['delete_url'] = 'student-delete'
        return context
    

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('student-list')

    

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('student-list')

    

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'org_del.html'
    success_url = reverse_lazy('student-list')


#College
class CollegeListView(ListView):
    model = College
    template_name = 'org_list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return College.objects.filter(
                name__icontains=query
            ) | College.objects.filter(
                description__icontains=query
            )
        return College.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = 'college-edit'  
        context['delete_url'] = 'college-delete'
        return context


class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'org_del.html'
    success_url = reverse_lazy('college-list')

#Progam
class ProgramListView(ListView):
    model = Program
    template_name = 'org_list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Program.objects.filter(
                name__icontains=query
            ) | Program.objects.filter(
                description__icontains=query
            )
        return Program.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_url'] = 'program-edit'  
        context['delete_url'] = 'program-delete'
        return context

class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'org_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'org_del.html'
    success_url = reverse_lazy('program-list')





