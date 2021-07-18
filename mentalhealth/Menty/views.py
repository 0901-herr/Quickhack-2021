from django.shortcuts import render
from .models import Leaderboard
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

