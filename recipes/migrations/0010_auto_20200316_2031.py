# Generated by Django 3.0.3 on 2020-03-16 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20200310_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='recipe',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
    ]
