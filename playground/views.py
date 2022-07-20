from django.shortcuts import render
from django.http import HttpResponse

a = 1
c = 3
d = 4


def check():
    e = 5
    return e


def say_hello(request):
    z = check()
    b = 2
    return render(request, 'hello.html', {'name': 'Nastenka'})
    # return HttpResponse('Hello World')
