from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here:

# def home(request):
#     return HttpResponse("Hello World!")

# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

# Class Based View for home method(view):
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    login_url = '/admin'
    template_name = 'home/authorized.html'

def home2(request):
    return HttpResponse("This is the app2")
