from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import Task
from .models import Leaderboard

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        your_leaderboard = Leaderboard(name="You", score="0 Tasks")
        your_leaderboard.save()

        # random_lst = []
        # for i in range(3):
        #     random_num = random.randrange(1, 11)
        #     if random_num not in random_lst:
        #         random_lst.append(random_num)

        all_tasks = Task.objects.all()
        tasks = all_tasks

        # for task in all_tasks:
        #     if int(task['task_id']) in random_lst:
        #         tasks['task_id'] = task

        print(tasks)

        return HttpResponse({"tasks":tasks})
