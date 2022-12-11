from django.http import HttpResponse
from django.shortcuts import render


def sites(request):

    return render(request, 'sites.html')

