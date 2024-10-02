from django.shortcuts import render
from django.core.cache import cache 
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
from .models import Countries 

def home(request):
    q = request.GET.get('q')
    
    if q is not None:
        print('in cache',cache.get(q))
        if cache.get(q):
            country = cache.get(q)
            print('data from redis')
            return HttpResponse(country)
        else:
            obj = Countries.objects.get(name__icontains=q)
            cache.set(q, obj, 3600)  # Cache for 1 hour
            print('data from db')
            return HttpResponse(obj)
    else:
        obj = Countries.objects.all()
        return HttpResponse(obj)