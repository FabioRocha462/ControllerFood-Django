# Generated by Django 4.1.1 on 2022-09-19 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]