from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'new': 'news'})


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    return render(request, 'result.html', {'result': val1 + val2})
