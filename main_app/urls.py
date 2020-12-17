from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/signup/', views.signup, name='signup'),
    path('goals/', views.goals_index, name="index"),
    path('user/<int:user_id>/goals/', views.user_goals, name="user_goals"),
    path('user/<int:user_id>/goallist/create', views.CreateList.as_view(), name="create_goallist"),
    path('user/<int:user_id>/goallist/<int:pk>/update/', views.UpdateList.as_view(), name='goallist_update'),
    path('user/<int:user_id>/goallist/<int:pk>/delete/', views.DeleteList.as_view(), name='goallist_delete'),
    path('user/<int:user_id>/goallist/<int:pk>/', views.GoalListDetail.as_view(), name='goallist_detail'),
    path('goals/create', views.GoalCreate.as_view(), name="create_goal"),
    # path('user/<int:user_id>/goals/<int:pk>/update/', views.UpdateGoal.as_view(), name='goal_update'),
    # path('user/<int:user_id>/goals/<int:pk>/delete/', views.DeleteGoal.as_view(), name='goal_delete'),                
    path('goals/<int:pk>/', views.GoalDetail.as_view(), name='goals_detail'),
    # path('user/<int:user_id>/goals/<int:list_id>/add_goal', views.add_goal, name="add_goal"),
]
