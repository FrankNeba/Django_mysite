from django.shortcuts import render

from django.http import HttpResponse


def indexes(request):
    return HttpResponse(" You're at the polls index.")

# Create your views here.
