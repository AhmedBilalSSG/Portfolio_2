# Generated by Django 5.1.2 on 2024-10-26 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_capabilities_headings_remove_capabilities_main_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education_Headings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(blank=True, max_length=200)),
                ('sub_title', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Education Headings',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('headings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.education_headings')),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
    ]