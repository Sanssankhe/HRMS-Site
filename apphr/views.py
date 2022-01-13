from django.shortcuts import render, HttpResponse
from apphr import models

# Create your views here.
def hr(request):
    return render(request, 'index.html')