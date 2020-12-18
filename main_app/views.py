from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import GoalList, Goal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GoalForm
from django import forms
from django.urls import reverse

# Create your views here.
class CreateGoalList(LoginRequiredMixin, CreateView):
    model = GoalList
    fields = ['title', 'description', 'restricted']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user) 
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class GoalListUpdate(LoginRequiredMixin, UpdateView):
    model = GoalList
    fields = ['title', 'description', 'restricted']


class GoalListDelete(LoginRequiredMixin, DeleteView):
    model = GoalList
    def get_success_url(self):
        return reverse('user_goals', kwargs={'user_id': self.request.user.id})



class GoalsList(LoginRequiredMixin, ListView):
    model = GoalList

class GoalListDetail(LoginRequiredMixin, DetailView):
    model = GoalList
    template_name = 'goallist/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = GoalForm(initial={'user': self.request.user})
        form.fields['user'].widget = forms.HiddenInput()
        form.fields['completiondate'].widget = forms.HiddenInput()
        context["form"] = form
        return context

    def goallists_detail(request, cat_id):
        goallists = GoalList.objects.get(id=goallist_id)
        # instantiate FeedingForm to be rendered in the template
        goals = Goal.objects.get(id=goal_id)
        return render(request, 'goallist/detail.html', {
            'goallists': goallist, 'goals': goal
        })
        

def home(request):
    return render(request, 'main_app/home.html')

def goals_index(request):
    return render(request, 'goals/index.html')

@login_required
def user_goals(request, user_id):
    lists = GoalList.objects.filter(user=request.user)
    return render(request, 'main_app/user_goals.html', { 'lists': lists })

# @login_required
# def user_goallists(request, user_id):
#     return render(request, 'main_app/user_goallists.html') <-- not needed since we're listing all goal lists under goals


@login_required
def add_goal(request, user_id, list_id):
    return render(request, 'main_app/add_goal.html')

@login_required
def add_goal(request, user_id, list_id):
    form = GoalForm(request.POST)
    if form.is_valid():
        new_goal = form.save(commit=False)
        new_goal.save()
        GoalList.objects.get(id=list_id).goal.add(new_goal)
    return redirect('goallist_detail', user_id = user_id, pk=list_id)

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



class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['title', 'description', 'category']
    


class GoalDetail(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'goals/detail.html'    

class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = '__all__'
    

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    success_url = '/goals/'

