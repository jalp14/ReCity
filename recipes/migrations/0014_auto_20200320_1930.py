# Generated by Django 3.0.3 on 2020-03-20 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20200320_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thumbnail',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
