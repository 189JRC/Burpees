from django.shortcuts import render

def timer(request):
    return render(request, "timer/index.html")