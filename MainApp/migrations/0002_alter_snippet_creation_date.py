# Generated by Django 4.1.1 on 2023-07-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
