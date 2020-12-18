from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = (
    ('0', 'Other'),
    ('1', 'Work/Career'),
    ('2', 'Finance'),
    ('3', 'Social'),
    ('4', 'Family'),
    ('5', 'Intellectual'),
    ('6', 'Health/Fitness'), 
    ('7', 'Spiritual'),
    ('8', 'Education'),
    ('9', 'Travel/Adventure'),
    ('10', 'Hobbies'),
)

class Goal(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    category = models.CharField(max_length=250)
    restricted = models.BooleanField(default=False) # this may not be the correct syntax, so let me know if you find a better way
    completed = models.BooleanField(default=False, blank=True) # this may not be the correct syntax, so let me know if you find a better way
    goaldate = models.DateField(
        verbose_name = 'set goal date',
        blank = True,
        null = True
         )
    completiondate = models.DateField(
        verbose_name = 'completion date',
        blank = True,
        null = True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goals_detail', kwargs={'pk': self.id})

class GoalList(models.Model):
    title = models.CharField(max_length=150)    
    description = models.TextField(max_length=250)
    goal = models.ManyToManyField(Goal)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restricted = models.BooleanField(default=False) # this may not be the correct syntax, so let me know if you find a better way

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goallist_detail', kwargs={'user_id': self.user_id ,'pk': self.pk})
    
    def get_success_url(self):
        return reverse('user_goallists', kwargs={'user_id': self.request.user.id})






