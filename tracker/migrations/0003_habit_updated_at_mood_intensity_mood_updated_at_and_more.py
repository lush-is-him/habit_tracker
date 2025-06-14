# Generated by Django 5.2 on 2025-05-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mood',
            name='intensity',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5),
        ),
        migrations.AddField(
            model_name='mood',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mood',
            name='mood',
            field=models.CharField(choices=[('joyful', 'Joyful'), ('grateful', 'Grateful'), ('peaceful', 'Peaceful'), ('hopeful', 'Hopeful'), ('inspired', 'Inspired'), ('confident', 'Confident'), ('excited', 'Excited'), ('proud', 'Proud'), ('loved', 'Loved'), ('energetic', 'Energetic'), ('content', 'Content'), ('optimistic', 'Optimistic'), ('motivated', 'Motivated'), ('focused', 'Focused'), ('creative', 'Creative'), ('neutral', 'Neutral'), ('contemplative', 'Contemplative'), ('balanced', 'Balanced'), ('calm', 'Calm'), ('mindful', 'Mindful'), ('anxious', 'Anxious'), ('stressed', 'Stressed'), ('frustrated', 'Frustrated'), ('sad', 'Sad'), ('angry', 'Angry'), ('lonely', 'Lonely'), ('tired', 'Tired'), ('overwhelmed', 'Overwhelmed'), ('disappointed', 'Disappointed'), ('confused', 'Confused'), ('worried', 'Worried'), ('irritable', 'Irritable'), ('nervous', 'Nervous'), ('insecure', 'Insecure'), ('exhausted', 'Exhausted')], max_length=20),
        ),
    ]
