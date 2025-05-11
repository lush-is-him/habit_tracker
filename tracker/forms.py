# tracker/forms.py
from django import forms

CATEGORY_CHOICES = [
    ('health', '🧘 Health'),
    ('fitness', '🏋️ Fitness'),
    ('learning', '📚 Learning'),
    ('personal', '🌱 Personal'),
]

FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('3', '3 times a week'),
    ('5', '5 times a week'),
]

class HabitForm(forms.Form):
    name = forms.CharField(label="Habit Name", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'e.g., Morning Jog',
        'class': 'input'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'What do you hope to achieve with this habit?',
        'class': 'input'
    }))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.HiddenInput())
    inspiration = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'e.g., David Goggins',
        'class': 'input'
    }))
    frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
