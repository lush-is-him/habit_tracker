# tracker/models.py
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=[
        ('health', 'Health'),
        ('fitness', 'Fitness'),
        ('learning', 'Learning'),
        ('personal', 'Personal'),
    ])
    inspiration = models.CharField(max_length=100, blank=True)
    frequency = models.CharField(max_length=20, choices=[
        ('daily', 'Daily'),
        ('3', '3 times a week'),
        ('5', '5 times a week'),
    ])
    weekly_frequency = models.IntegerField(
        default=1,
        help_text="How many times per week should this habit be completed?"
    )
    required_repetitions = models.IntegerField(
        default=1,
        help_text="How many repetitions are required per completion?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_completion_percentage(self):
        """Calculate the completion percentage for the current week"""
        today = timezone.now().date()
        start_of_week = today - timezone.timedelta(days=today.weekday())
        end_of_week = start_of_week + timezone.timedelta(days=6)
        
        completions = HabitCompletion.objects.filter(
            habit=self,
            date__range=[start_of_week, end_of_week]
        )
        
        # Count total completions across the week
        total_completions = sum(completion.completed_repetitions for completion in completions)
        
        # For daily habits, we need 7 completions (one per day)
        if self.frequency == 'daily':
            target = 7
        else:
            # For non-daily habits, use weekly_frequency
            target = self.weekly_frequency
        
        return min(100, (total_completions / target) * 100)

    def get_weekly_progress_text(self):
        """Get the text representation of weekly progress"""
        today = timezone.now().date()
        start_of_week = today - timezone.timedelta(days=today.weekday())
        end_of_week = start_of_week + timezone.timedelta(days=6)
        
        completions = HabitCompletion.objects.filter(
            habit=self,
            date__range=[start_of_week, end_of_week]
        )
        
        total_completions = sum(completion.completed_repetitions for completion in completions)
        
        if self.frequency == 'daily':
            return f"{total_completions}/7 days"
        else:
            return f"{total_completions}/{self.weekly_frequency} times"

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed_repetitions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('habit', 'date')

    def __str__(self):
        return f"{self.habit.name} - {self.date} ({self.completed_repetitions} reps)"

class Mood(models.Model):
    MOOD_CHOICES = [
        # Positive Emotions
        ('excited', 'Excited'),
        ('happy', 'Happy'),
        ('joyful', 'Joyful'),
        ('grateful', 'Grateful'),
        ('content', 'Content'),
        ('calm', 'Calm'),
        ('relaxed', 'Relaxed'),
        ('peaceful', 'Peaceful'),
        ('energetic', 'Energetic'),
        ('motivated', 'Motivated'),
        ('proud', 'Proud'),
        ('hopeful', 'Hopeful'),
        
        # Neutral Emotions
        ('tired', 'Tired'),
        ('bored', 'Bored'),
        ('indifferent', 'Indifferent'),
        ('focused', 'Focused'),
        ('curious', 'Curious'),
        ('contemplative', 'Contemplative'),
        
        # Challenging Emotions
        ('stressed', 'Stressed'),
        ('anxious', 'Anxious'),
        ('worried', 'Worried'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('frustrated', 'Frustrated'),
        ('overwhelmed', 'Overwhelmed'),
        ('lonely', 'Lonely'),
        ('disappointed', 'Disappointed'),
        ('guilty', 'Guilty'),
        ('ashamed', 'Ashamed'),
        ('jealous', 'Jealous'),
        ('irritable', 'Irritable'),
        ('nervous', 'Nervous'),
    ]

    MOOD_DEFINITIONS = {
        # Positive Emotions
        'excited': 'Feeling enthusiastic and eager about something',
        'happy': 'Feeling pleasure and contentment',
        'joyful': 'Feeling great delight and happiness',
        'grateful': 'Feeling thankful and appreciative',
        'content': 'Feeling satisfied and at ease',
        'calm': 'Feeling peaceful and free from agitation',
        'relaxed': 'Feeling free from tension and anxiety',
        'peaceful': 'Feeling tranquil and serene',
        'energetic': 'Feeling full of vitality and enthusiasm',
        'motivated': 'Feeling driven and determined to achieve something',
        'proud': 'Feeling a sense of achievement and self-respect',
        'hopeful': 'Feeling optimistic about the future',
        
        # Neutral Emotions
        'tired': 'Feeling in need of rest or sleep',
        'bored': 'Feeling uninterested or lacking stimulation',
        'indifferent': 'Feeling neither positive nor negative',
        'focused': 'Feeling concentrated and attentive',
        'curious': 'Feeling interested in learning or knowing more',
        'contemplative': 'Feeling thoughtful and reflective',
        
        # Challenging Emotions
        'stressed': 'Feeling mental or emotional strain',
        'anxious': 'Feeling worried or uneasy about something',
        'worried': 'Feeling concerned about potential problems',
        'sad': 'Feeling sorrow or unhappiness',
        'angry': 'Feeling strong displeasure or hostility',
        'frustrated': 'Feeling upset or annoyed due to inability to change something',
        'overwhelmed': 'Feeling unable to cope with demands',
        'lonely': 'Feeling isolated or lacking companionship',
        'disappointed': 'Feeling let down or dissatisfied',
        'guilty': 'Feeling responsible for wrongdoing',
        'ashamed': 'Feeling embarrassed or humiliated',
        'jealous': "Feeling resentful of someone else's advantages",
        'irritable': 'Feeling easily annoyed or impatient',
        'nervous': 'Feeling anxious or apprehensive'
    }

    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    intensity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_mood_display()} ({self.intensity}/10) - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    def get_definition(self):
        return self.MOOD_DEFINITIONS.get(self.mood, '')
