# Generated by Django 3.0.3 on 2020-03-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(upload_to='media'),
        ),
    ]
