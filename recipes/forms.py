import datetime
from django import forms
from django.forms import ModelForm
from .models import Recipe, Photo, Menu, Comment
from dal import autocomplete
from django.conf import settings
from taggit.forms import *


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_title']

   # creation_date = datetime.timezone.now()


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your comment here...', 'rows' : '4', 'cols': '50'}))
    class Meta:
        model = Comment
        fields = ('content',)

class RecipeEditPhotoForm(forms.Form):
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

class RecipeEditThumbnailForm(forms.Form):
    thumbnail = forms.ImageField(required=False)

class RecipeManualForm(forms.Form):
    recipe_title = forms.CharField(max_length=50)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    thumbnail = forms.ImageField(required=False)
    categories_names = TagField()
    ingredient_field_count = forms.CharField(widget=forms.HiddenInput())
    instructions = forms.CharField(max_length=2500, widget=forms.Textarea(attrs={'style':'resize:none;'}))
    descriptions = forms.CharField( widget=forms.Textarea(attrs={'style':'resize:none;'}))

    def clean_photo(self, *args, **kwargs):
        photos = self.files.getlist('photo')
        
        #Prevents NoneType error.
        if(photos == None):
            size = 0
        else:
            size = len(photos)

        if(size > settings.FILE_UPLOAD_LIMIT):
            raise forms.ValidationError('Upload Limit Reached. Upload Limit is ' + str(settings.FILE_UPLOAD_LIMIT) + ' and you have uploaded ' + str(size) + '.')
        
        return photos

class RecipeEditForm(forms.ModelForm):
    descriptions = forms.CharField( widget=forms.Textarea(attrs={'style':'resize:none;'}))

    class Meta:
        model = Recipe
        fields = ['recipe_title', 'categories', 'descriptions'] 


class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['title', 'recipes']

