# Generated by Django 5.0.6 on 2024-05-23 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer_questions', '0003_exercise_exercise_type_exercise_fach_exercise_thema_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]
