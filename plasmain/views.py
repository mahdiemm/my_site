from django.shortcuts import render
from django.shortcuts import HttpResponse


def fixed_sections_no_login(request):
    return render(request , 'base.html')