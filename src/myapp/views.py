
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "intro": "Hello this is a Preview Deployment"
    }
    return render(request, "index.html", context)
