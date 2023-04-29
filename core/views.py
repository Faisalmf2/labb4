from django.shortcuts import render

TAX_RATE = 15

def index(request):
    return render(request, "index.html")

def calculate(request, number):
    total = number - 0.15*number
    return render(request, "result.html", {"total":total})

def taxrate(request):
    return render(request, "taxrate.html", {"taxrate":TAX_RATE})