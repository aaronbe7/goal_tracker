from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class GoalList(models.Model):
    title = models.CharField(max_length=150)    
    decription = models.TextField(max_length=250)
    goal = models.ManyToManyField(Goal)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restricted = models.BooleanField(default=False) # this may not be the correct syntax, so let me know if you find a better way

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwags={'goallist_id': self.id})


class Goal(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    category = models.ManyToManyField(Category)
    restricted = models.BooleanField(default=False) # this may not be the correct syntax, so let me know if you find a better way
    completed = models.BooleanField(default=False) # this may not be the correct syntax, so let me know if you find a better way
    goaldate = models.DateField('set goal date')
    completiondate = models.DateField('completion date')

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('goals_detail', kwargs={'pk': self.id})

class Category(models.Model):
    title = models.CharField(max_length=25)
    goallist = models.ManyToManyField(GoalList)
    goal = models.ManyToManyField(Goal)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return self.title





