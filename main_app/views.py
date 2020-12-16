from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import GoalList

# Create your views here.
class CreateList(CreateView):
    model = GoalList
    fields = '__all__'

class UpdateList(UpdateView):
    model = GoalList
    fields = '__all__'

class DeleteList(DeleteView):
    model = GoalList
    success_url = '/goals/'

class GoalsList(ListView):
    model = GoalList
    print('Placeholder')

class GoalListDetails(DetailView):
    model = GoalList
    print('Placeholder')

def home(request):
    return render(request, 'main_app/home.html')

def user_goals(request, user_id):
    return render(request, 'main_app/user_goals.html')

def add_goal(request, user_id, list_id):
    return render(request, 'main_app/add_goal.html')