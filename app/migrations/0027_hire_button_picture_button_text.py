# Generated by Django 5.1.2 on 2024-10-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_hire_button_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire_button_picture',
            name='button_text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
