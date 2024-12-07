# Generated by Django 5.1.2 on 2024-10-27 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_projects_headings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Programming Task', 'Programming Task'), ('Graphics Task', 'Graphics Task'), ('Other', 'Other')], max_length=40)),
                ('thumbnail', models.ImageField(null=True, upload_to='project_thumbnails/', verbose_name='')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(null=True, upload_to='project_media/', verbose_name='')),
                ('pic_description', models.CharField(blank=True, max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projects')),
            ],
            options={
                'verbose_name_plural': 'Project Media',
            },
        ),
    ]
