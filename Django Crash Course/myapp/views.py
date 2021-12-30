from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'John Doe',
        'age': 45,
        'nationality': 'British',
        'app': 'myapp'
    }
    return render(request, 'myapp_templates/index.html', context)

def greetings(request):
    name = request.GET['name']
    return render(request, 'myapp_templates/greetings.html', context={'name':name})

def counter(request):
    text = request.GET['text']
    words_counter = len(text.split())
    return render(request, 'myapp_templates/counter.html', context={'words_counter':words_counter})