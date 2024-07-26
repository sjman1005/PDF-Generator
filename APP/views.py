from django.shortcuts import render

def index(request):
    return render(request, 'APP/index.html')


def generate(request):
    return render(request, 'APP/generate.html')
