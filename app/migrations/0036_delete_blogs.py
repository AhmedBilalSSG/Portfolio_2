# Generated by Django 5.1.2 on 2024-11-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_blogs_heading'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]