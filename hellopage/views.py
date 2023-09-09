from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {
        "task" : tasks,
    }
    return render(request, "index.html", context)