from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):

    features = Feature.objects.all()

    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'
    # feature1.is_true = True

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.details = 'Very safe and stable'
    # feature2.is_true = True

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.details = 'Anyone can use'
    # feature3.is_true = False

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.details = 'Cheaper then you think'
    # feature4.is_true = True

    # context = {
    #     'name': 'John Doe',
    #     'age': 45,
    #     'nationality': 'British',
    #     'app': 'myapp2',
    #     'feature1': feature1,
    #     'feature2': feature2,
    #     'feature3': feature3,
    #     'feature4': feature4,
    # }

    # features = [feature1, feature2, feature3, feature4]

    # return render(request, 'myapp2_templates/index.html', context)
    return render(request, 'myapp2_templates/index.html', {'features': features})


def greetings(request):
    name = request.GET['name']
    return render(request, 'myapp2_templates/greetings.html', context={'name':name})


def counter(request):
    text = request.POST['text']
    words_counter = len(text.split())
    return render(request, 'myapp2_templates/counter.html', context={'words_counter':words_counter})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords are different')
            return redirect('register')
    else:
        return render(request, 'myapp2_templates/register.html')