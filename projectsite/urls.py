"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from orgstudent.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from orgstudent.views import(
    OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, 
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,)


def home(request):
    return render(request, 'home.html')
def forms_page(request):
    return render(request, 'org_form.html')

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('index.html', home, name='home-function'),
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/',OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<int:pk>/edit/',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('forms/', forms_page, name='forms-page'),
  


# OrgMember
    path('orgmembers/', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/edit/', OrgMemberUpdateView.as_view(), name='orgmember-edit'),
    path('orgmembers/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

     # Student
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # College
    path('colleges/', CollegeListView.as_view(), name='college-list'),
    path('colleges/add/', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/edit/', CollegeUpdateView.as_view(), name='college-edit'),
    path('colleges/<int:pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Program
    path('programs/', ProgramListView.as_view(), name='program-list'),
    path('programs/add/', ProgramCreateView.as_view(), name='program-add'),
    path('programs/<int:pk>/edit/', ProgramUpdateView.as_view(), name='program-edit'),
    path('programs/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]

