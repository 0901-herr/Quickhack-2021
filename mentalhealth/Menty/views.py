from django.shortcuts import render
from .models import Leaderboard
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        new_name = "You"
        new_score = 0
        new_user = Leaderboard(name =new_name,score = new_score)
        new_user.save()
        return HttpResponse(new_name)
