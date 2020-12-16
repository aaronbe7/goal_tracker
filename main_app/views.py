from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import GoalList, Goal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateList(LoginRequiredMixin, CreateView):
    model = GoalList
    fields = ['title', 'description', 'restricted']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user) 
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class UpdateList(LoginRequiredMixin, UpdateView):
    model = GoalList
    fields = '__all__'

class DeleteList(LoginRequiredMixin, DeleteView):
    model = GoalList
    success_url = '/goals/'

class GoalsList(LoginRequiredMixin, ListView):
    model = GoalList
    print('Placeholder')

class GoalListDetails(LoginRequiredMixin, DetailView):
    model = GoalList
    print('Placeholder')

def home(request):
    return render(request, 'main_app/home.html')

def goals_index(request):
    return render(request, 'goals/index.html')

@login_required
def user_goals(request, user_id):
    return render(request, 'main_app/user_goals.html')

@login_required
def add_goal(request, user_id, list_id):
    return render(request, 'main_app/add_goal.html')

def goallist_detail(request, goallist_id):
    goallist = GoalList.objects.get(id=goallist_id)
    goal = Goal.objects.get(id=goal_id)
    return render(request, 'goallist/detail.html', {
        'goallist': goallist, 'goal': goal
    })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('goal_list')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)