# Generated by Django 5.1.2 on 2024-10-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_certificates_headings_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire_Button_Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='hire_button/', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Hire Button Picture',
            },
        ),
    ]