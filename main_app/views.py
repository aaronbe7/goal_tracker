from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import GoalList, Goal, CATEGORIES, Photo 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GoalForm, EditProfileForm, CategoryFilterForm
from django import forms
import uuid
import boto3
from django.urls import reverse
# import popup_forms <-- could maybe be used on the goal details page to copy and create a new form

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/' 
BUCKET  = 'catcollector1205' 


# @popup_forms.handler
# def form_view(request):
#     if request.method == 'POST':
#         form = ApplyForm(request.post)
#         if not form.is_valid():
#             return popup_forms.OpenFormResponse(request, form)
#         # ...
#         # ... FORM PROCESSING GOES HERE ...
#         # ...
#         return popup_forms.CloseFormResponse(request)
#     else:
#         return redirect('failure_url')
#         # or raise Http404
#         # or just popup_forms.CloseFormResponse(request)

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

    # ---------- I'm commenting this part because this won't work in 
    # ---------- Class Based Views.
    # def goallists_detail(request, goallist_id):
    #     goallists = GoalList.objects.get(id=goallist_id)
    #     # instantiate FeedingForm to be rendered in the template
    #     goals = Goal.objects.get(id=goal_id)
    #     return render(request, 'goallist/detail.html', {
    #         'goallists': goallist, 'goals': goal
    #     })
        

def home(request): 
    return render(request, 'main_app/home.html')

def goals_index(request):
    if request.method == "POST":
        goals = Goal.objects.filter(category__icontains=request.POST['category'])
    else: 
        goals = Goal.objects.all()
    return render(request, 'goals/index.html', {
        'goals': goals,
        'user': request.user,
        'CATEGORIES': CATEGORIES,
        'form': CategoryFilterForm
    })

@login_required
def user_goals(request, user_id):
    lists = GoalList.objects.filter(user=request.user)
    return render(request, 'main_app/user_goals.html', { 'lists': lists })

@login_required
def profile(request, user_id):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'main_app/profile.html', {'form': form})
    

# @login_required
# def user_goallists(request, user_id):
#     return render(request, 'main_app/user_goallists.html') <-- not needed since we're listing all goal lists under goals

@login_required
def profile_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url,key=key,user_id=user_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('profile', user_id = user_id)

def delete_user_photo(request, user_id):
    photo = Photo.objects.get(user_id=user_id)
    s3 = boto3.client('s3')
    try:
        s3.delete_object(
            Bucket = BUCKET,
            Key = photo.key
        )
        photo.delete()
    except:
        print('An error occurred deleting file on S3')
    return redirect('profile',user_id)

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

def copy_goal(request):
    print(request.POST)
    goal = Goal.objects.get(id=request.POST['goalid'])
    goallist = GoalList.objects.get(id=request.POST['goallist'])
    print(goal.user)
    newGoal = Goal(
        title = goal.title,
        description = goal.description,
        restricted = False,
        completed = False,
        category = goal.category,
        user = request.user
    )
    newGoal.save()
    goallist.goal.add(newGoal)
    goallist.save()

    return redirect(f'/user/{request.user.id}/goallist/{goallist.id}/')

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
    fields = '__all__'

class GoalDetail(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'goals/detail.html'    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goallist = GoalList.objects.filter(user=self.request.user)
        context['goallist'] = goallist
        return context

class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    def get_success_url(self):
        return reverse('goallist_detail', kwargs={
            'user_id': self.request.user.id,
            'pk': self.object.goallist_set.first().id
        })

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    def get_success_url(self):
            return reverse('goallist_detail', kwargs={
                'user_id': self.request.user.id,
                'pk': self.object.goallist_set.first().id
            })
