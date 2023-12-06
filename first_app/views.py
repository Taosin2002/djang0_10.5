from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={
        "list":['i','am','a','student','of','phitron'],
        "birthday" : datetime.datetime.now(),
    }
    return render(request, 'home.html',d)