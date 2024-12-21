from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from .forms import *

def LogInView(request):
    if request.method == 'GET':
        return render(request, 'auth.html')
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True},status = 200)
        else:
            return JsonResponse({'success': False},status = 400)

def RegisterView(request):
    register_form = RegistrationForm()
    return render(request, 'register.html', {'form': register_form})
