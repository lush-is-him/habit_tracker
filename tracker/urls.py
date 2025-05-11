# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_habit/', views.add_habit, name='add_habit'),
    path('edit_habit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete_habit/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('record_mood/', views.record_mood, name='record_mood'),
    path('edit_mood/<int:mood_id>/', views.edit_mood, name='edit_mood'),
    path('delete_mood/<int:mood_id>/', views.delete_mood, name='delete_mood'),
    path('track_habits/', views.track_habits, name='track_habits'),
    path('track_moods/', views.track_moods, name='track_moods'),
    path('update_habit_completion/<int:habit_id>/', views.update_habit_completion, name='update_habit_completion'),
]

#path('track-moods/', views.track_moods, name='track_moods'),