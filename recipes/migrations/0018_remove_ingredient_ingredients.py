# Generated by Django 3.0.3 on 2020-03-29 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20200325_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredients',
        ),
    ]
