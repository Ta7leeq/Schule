# Generated by Django 5.0.4 on 2024-05-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fill_the_gaps', '0006_alter_gaps_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaps',
            name='image',
            field=models.CharField(default='default_value', max_length=100, null=True),
        ),
    ]