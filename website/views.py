from django.shortcuts import render

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def education_view(request):
    return render(request, 'website/education.html')

def skills_view(request):
    return render(request, 'website/skills.html')

def projects_view(request):
    return render(request, 'website/projects.html')

def contact_view(request):
    return render(request, 'website/contact.html')
