# Generated by Django 5.1.2 on 2024-10-25 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_skills_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='skill',
        ),
    ]