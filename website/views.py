from django.shortcuts import render
from .models import Service, Project



def home(request):

    services = Service.objects.all()[:3]
    projects = Project.objects.all()[:3]

    context = {
        "services": services,
        "projects": projects,
    }

    return render(
        request,
        "website/home.html",
        context
    )



def about(request):

    return render(
        request,
        "website/about.html"
    )



def services(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(
        request,
        "website/services.html",
        context
    )



def projects(request):

    projects = Project.objects.all()

    context = {
        "projects": projects
    }

    return render(
        request,
        "website/projects.html",
        context
    )



def contact(request):
    return render(request, "website/contact.html")