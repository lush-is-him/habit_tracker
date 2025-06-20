# Generated by Django 5.2 on 2025-05-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('joyful', 'Joyful'), ('grateful', 'Grateful'), ('peaceful', 'Peaceful'), ('neutral', 'Neutral'), ('anxious', 'Anxious'), ('sad', 'Sad')], max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
