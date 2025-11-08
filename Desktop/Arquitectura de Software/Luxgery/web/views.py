from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def services(request):
    return render(request, "services.html")  # ✅ Nueva vista


def about(request):
    return render(request, "about.html")


def testimonios(request):
    return render(request, "testimonios.html")


def contacto(request):
    return render(request, "contacto.html")
