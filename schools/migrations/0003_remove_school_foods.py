# Generated by Django 4.1.1 on 2022-10-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_school_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='foods',
        ),
    ]
