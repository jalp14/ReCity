from datetime import datetime 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.conf import settings

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=50)
    instructions = models.CharField(max_length=2500, default = "")
    creation_date = models.DateTimeField('date created', default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    categories = TaggableManager(help_text="A comma-separated list of tags.")
    instructions = models.CharField(max_length=2500)
    descriptions = models.CharField(max_length=200, default="")

    def __str__(self):
         return self.recipe_title

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    content = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.recipe.recipe_title, self.author.username)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default='1')
    ingredient_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ingredient_name

class Photo(models.Model):
    image = models.ImageField(upload_to='media', default = None)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None)

class Thumbnail(models.Model):
    image = models.ImageField(upload_to='media', default=None)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=None)

class Menu(models.Model):
    title = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    creation_date = models.DateTimeField('created', default=datetime.now)
    recipes = models.ManyToManyField(Recipe, through='MenuRecipe')

class MenuRecipe(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)