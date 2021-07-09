from django.shortcuts import render, HttpResponse

def home_view(request):
    return render(request, 'home.html', {'isim':'kullanici'})


# Create your views here.
