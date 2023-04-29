from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team.html')

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpView(CreateView):
    class UserForm(UserCreationForm):
        class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
