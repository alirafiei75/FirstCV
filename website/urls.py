from django.urls import path
from website.views import *

urlpatterns = [
    path('', index_view, name = 'index'),
    path('about', about_view, name = 'about'),
    path('education', education_view, name = 'education'),
    path('skills', skills_view, name = 'skills'),
    path('projects', projects_view, name = 'projects'),
    path('contact', contact_view, name = 'contact'),
]
