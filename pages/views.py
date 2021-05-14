from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):

    print('test')

    return render(request, 'web/home.html', {})