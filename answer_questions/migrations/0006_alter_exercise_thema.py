# Generated by Django 5.0.6 on 2024-05-24 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer_questions', '0005_fach_alter_exercise_exercise_type_exercise_fach_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='Thema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises_thema', to='answer_questions.thema'),
        ),
    ]