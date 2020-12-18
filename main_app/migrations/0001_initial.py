# Generated by Django 3.1.4 on 2020-12-18 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Work/Career', 'Work/Career'), ('Finance', 'Finance'), ('Social', 'Social'), ('Family', 'Family'), ('Intellectual', 'Intellectual'), ('Health/Fitness', 'Health/Fitness'), ('Spiritual', 'Spiritual'), ('Education', 'Education'), ('Travel/Adventure', 'Travel/Adventure'), ('Hobbies', 'Hobbies'), ('Others', 'Others')], default='Work/Career', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('restricted', models.BooleanField(default=False)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('goaldate', models.DateField(blank=True, null=True, verbose_name='set goal date')),
                ('completiondate', models.DateField(blank=True, null=True, verbose_name='completion date')),
                ('category', models.ManyToManyField(blank=True, to='main_app.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoalList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('restricted', models.BooleanField(default=False)),
                ('goal', models.ManyToManyField(to='main_app.Goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
