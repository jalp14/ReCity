# Generated by Django 3.0.3 on 2020-03-16 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20200316_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
    ]
