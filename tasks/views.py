from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def planner(request):
    return render(request, 'planner/planner.html')
