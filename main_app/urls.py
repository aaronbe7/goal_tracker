from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/signup/', views.signup, name='signup'),
    path('goals/', views.goals_index, name="index"),
    path('user/<int:user_id>/goals/', views.user_goals, name="user_goals"),
    # path('user/<int:user_id>/goallists/', views.user_goallists, name="user_goallists"),  <-- not needed since listing lists all in user_goals
    path('user/<int:user_id>/goallist/create', views.CreateGoalList.as_view(), name="create_goallist"),
    path('user/<int:user_id>/goallist/<int:pk>/update/', views.GoalListUpdate.as_view(), name='goallist_update'),
    path('user/<int:user_id>/goallist/<int:pk>/delete/', views.GoalListDelete.as_view(), name='goallist_delete'),
    path('user/<int:user_id>/goallist/<int:pk>/', views.GoalListDetail.as_view(), name='goallist_detail'),
    path('goals/create', views.GoalCreate.as_view(), name="create_goal"),
    path('user/<int:user_id>/', views.profile, name='profile'),  
    path('user/<int:user_id>/photo', views.profile_photo, name='profile_photo'),
    path('user/<int:user_id>/delete', views.delete_user_photo, name='profile_photo_delete'),
    path('user/<int:user_id>/goals/<int:pk>/update/', views.GoalUpdate.as_view(), name='goal_update'),
    path('user/<int:user_id>/goals/<int:pk>/delete/', views.GoalDelete.as_view(), name='goal_delete'),
    path('user/<int:user_id>/goallist/<int:goallist_id>/goals/<int:pk>/', views.GoalDetail.as_view(), name='goals_detail'),
    path('user/<int:user_id>/goals/<int:list_id>/add_goal', views.add_goal, name="add_goal"),
    path('goals/copy_goal', views.copy_goal, name="create_goalcopy"),
]
