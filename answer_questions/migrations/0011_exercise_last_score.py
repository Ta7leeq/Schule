# Generated by Django 5.0.6 on 2024-10-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer_questions', '0010_exercise_last_time_exercise_next_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='last_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
