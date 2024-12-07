# Generated by Django 5.1.2 on 2024-10-26 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_education_end_year_alter_education_start_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('institute', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField()),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('headings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.education_headings')),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
    ]
