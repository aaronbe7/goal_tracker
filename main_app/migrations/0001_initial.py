<<<<<<< HEAD
# Generated by Django 3.1.4 on 2020-12-15 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 3.1.4 on 2020-12-16 00:10

from django.db import migrations, models
>>>>>>> main


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> main
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('restricted', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('goaldate', models.DateField(verbose_name='set goal date')),
                ('completiondate', models.DateField(verbose_name='completion date')),
                ('category', models.ManyToManyField(to='main_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='GoalList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('decription', models.TextField(max_length=250)),
                ('restricted', models.BooleanField(default=False)),
                ('goal', models.ManyToManyField(to='main_app.Goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
            name='GoalList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('decription', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('restricted', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('goaldate', models.DateField(verbose_name='set goal date')),
                ('completiondate', models.DateField(verbose_name='completion date')),
                ('category', models.ManyToManyField(to='main_app.Category')),
>>>>>>> main
            ],
        ),
    ]
