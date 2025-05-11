# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HabitForm
from .models import Habit, Mood, HabitCompletion
from django import forms
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime, timedelta
import json

def home(request):
    # Print all habits in the database
    habits = Habit.objects.all().order_by('-created_at')
    print("Habits in database:", list(habits))
    print("Number of habits:", habits.count())
    
    return render(request, 'tracker/index.html', {'habits': habits})



# Form class
class HabitForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    category = forms.ChoiceField(
        choices=[
            ('health', 'Health'),
            ('fitness', 'Fitness'),
            ('learning', 'Learning'),
            ('personal', 'Personal'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    inspiration = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    frequency = forms.ChoiceField(
        choices=[
            ('daily', 'Daily'),
            ('3', '3 times a week'),
            ('5', '5 times a week'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    required_repetitions = forms.IntegerField(
        min_value=1,
        max_value=100,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'max': '100'
        }),
        help_text="How many repetitions are required per completion?"
    )

    def clean(self):
        cleaned_data = super().clean()
        frequency = cleaned_data.get('frequency')

        if frequency == 'daily':
            cleaned_data['weekly_frequency'] = 7
        elif frequency == '3':
            cleaned_data['weekly_frequency'] = 3
        elif frequency == '5':
            cleaned_data['weekly_frequency'] = 5

        return cleaned_data

# View to show the habit form
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            try:
                # Get the frequency from the hidden input
                frequency = request.POST.get('frequency', 'daily')
                
                # Set weekly_frequency based on frequency
                weekly_frequency = 7 if frequency == 'daily' else int(frequency)
                
                habit = Habit.objects.create(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description'],
                    category=form.cleaned_data['category'],
                    inspiration=form.cleaned_data['inspiration'],
                    frequency=frequency,
                    weekly_frequency=weekly_frequency,
                    required_repetitions=form.cleaned_data['required_repetitions']
                )
                return redirect('home')
            except Exception as e:
                return render(request, 'tracker/add_habit.html', {
                    'form': form,
                    'error': str(e)
                })
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
            return render(request, 'tracker/add_habit.html', {
                'form': form,
                'error': 'Please correct the errors below.'
            })
    else:
        form = HabitForm()
    return render(request, 'tracker/add_habit.html', {'form': form})

def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            try:
                habit.name = form.cleaned_data['name']
                habit.description = form.cleaned_data['description']
                habit.category = form.cleaned_data['category']
                habit.inspiration = form.cleaned_data['inspiration']
                habit.frequency = form.cleaned_data['frequency']
                habit.weekly_frequency = form.cleaned_data['weekly_frequency']
                habit.required_repetitions = form.cleaned_data['required_repetitions']
                habit.save()
                return redirect('home')
            except Exception as e:
                return render(request, 'tracker/edit_habit.html', {'form': form, 'habit': habit, 'error': str(e)})
        else:
            return render(request, 'tracker/edit_habit.html', {'form': form, 'habit': habit, 'error': 'Please correct the errors below.'})
    else:
        form = HabitForm(initial={
            'name': habit.name,
            'description': habit.description,
            'category': habit.category,
            'inspiration': habit.inspiration,
            'frequency': habit.frequency,
            'weekly_frequency': habit.weekly_frequency,
            'required_repetitions': habit.required_repetitions
        })
    return render(request, 'tracker/edit_habit.html', {'form': form, 'habit': habit})

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    if request.method == 'POST':
        habit.delete()
        return redirect('home')
    return render(request, 'tracker/delete_habit.html', {'habit': habit})

def record_mood(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        intensity = request.POST.get('intensity')
        notes = request.POST.get('notes', '')

        if not mood or not intensity:
            return render(request, 'tracker/record_mood.html', {
                'error': 'Please select a mood and intensity level.',
                'mood_choices': Mood.MOOD_CHOICES,
                'mood_definitions': Mood.MOOD_DEFINITIONS
            })

        try:
            intensity = int(intensity)
            if not 1 <= intensity <= 10:
                raise ValueError('Intensity must be between 1 and 10')
        except ValueError:
            return render(request, 'tracker/record_mood.html', {
                'error': 'Invalid intensity level. Please select a number between 1 and 10.',
                'mood_choices': Mood.MOOD_CHOICES,
                'mood_definitions': Mood.MOOD_DEFINITIONS
            })

        Mood.objects.create(
            mood=mood,
            intensity=intensity,
            notes=notes
        )
        return redirect('home')

    return render(request, 'tracker/record_mood.html', {
        'mood_choices': Mood.MOOD_CHOICES,
        'mood_definitions': Mood.MOOD_DEFINITIONS
    })

def edit_mood(request, mood_id):
    mood = get_object_or_404(Mood, id=mood_id)
    if request.method == 'POST':
        mood_type = request.POST.get('mood')
        notes = request.POST.get('notes', '')
        intensity = request.POST.get('intensity', 5)
        
        if mood_type:
            try:
                mood.mood = mood_type
                mood.notes = notes
                mood.intensity = intensity
                mood.save()
                return redirect('track_moods')
            except Exception as e:
                return render(request, 'tracker/edit_mood.html', {'mood': mood, 'error': str(e)})
    return render(request, 'tracker/edit_mood.html', {'mood': mood})

def delete_mood(request, mood_id):
    mood = get_object_or_404(Mood, id=mood_id)
    if request.method == 'POST':
        mood.delete()
        return redirect('track_moods')
    return render(request, 'tracker/delete_mood.html', {'mood': mood})

def track_habits(request):
    habits = Habit.objects.all().order_by('-created_at')
    today = timezone.now().date()
    
    # Get or create habit completions for today
    for habit in habits:
        HabitCompletion.objects.get_or_create(
            habit=habit,
            date=today,
            defaults={'completed_repetitions': 0}
        )
    
    return render(request, 'tracker/track_habits.html', {
        'habits': habits,
        'today': today
    })

def track_moods(request):
    moods = Mood.objects.all().order_by('-timestamp')
    return render(request, 'tracker/track_moods.html', {'moods': moods})

def update_habit_completion(request, habit_id):
    if request.method == 'POST':
        habit = get_object_or_404(Habit, id=habit_id)
        date = request.POST.get('date')
        completed_repetitions = int(request.POST.get('completed_repetitions', 0))
        
        try:
            completion, created = HabitCompletion.objects.get_or_create(
                habit=habit,
                date=date,
                defaults={'completed_repetitions': completed_repetitions}
            )
            
            if not created:
                completion.completed_repetitions = completed_repetitions
                completion.save()
            
            # Calculate weekly progress
            weekly_progress = habit.get_completion_percentage()
            weekly_progress_text = habit.get_weekly_progress_text()
            
            return JsonResponse({
                'status': 'success',
                'weekly_progress': weekly_progress,
                'weekly_progress_text': weekly_progress_text
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

