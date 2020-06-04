from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, Photo, Thumbnail, Menu, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RecipeForm, RecipeManualForm, MenuCreateForm, RecipeEditPhotoForm, RecipeEditThumbnailForm, CommentForm, RecipeEditForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views import View
from django.shortcuts import redirect
from django.conf import settings
import datetime
from taggit.models import Tag
from django.http import JsonResponse
import json
from django.contrib import messages


#---------------------------INDEX/HOMEPAGE---------------------------#
def IndexView(request):
    template = 'components/index.html'
    context = {
        'tag_list' : Tag.objects.all(),
        'recipe_list': Recipe.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date'),
        'menu_list': Menu.objects.all()
    }
    return render(request, template, context)

#---------------------------ALL RECIPES---------------------------#
class RecipeAll(DetailView):
    def get(self, request):
        template_name = 'recipes/RecipeAll.html'
        context = {
            'recipe_list': Recipe.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')
        }
        return render(request, template_name, context)
    
def RecipeCategory(request, cat_id):
    template = 'recipes/RecipeCategory.html'
    context = {
        'category_name': Tag.objects.get(id=cat_id),
        'recipe_list': Recipe.objects.filter(categories__id=cat_id).order_by('-creation_date'),
    }
    return render(request, template, context)

#----------------------PROFILE & SETTINGS ----------------------#
def ProfileView(request):
    template = 'components/profile.html'
    context = {
        'user_recipes': Recipe.objects.filter(author=request.user, creation_date__lte=timezone.now()).order_by('-creation_date'),
        'user_menus': Menu.objects.filter(
            author=request.user,
            creation_date__lte=timezone.now()).order_by('-creation_date'),
    }
    return render(request, template, context)

def UserSettings(request):
    model = request.user
    template = 'recipes/UserSettings.html'
    context={ 'user': model }
    return render(request, template, context)

class ChangeUsername(UpdateView):
    model = User
    template_name = 'recipes/UserEditUsername.html'
    fields = ['username']
    success_url = '/recipes/profile/settings'

def ChangePassword(request):
    template_name = 'recipes/PasswordChange.html' 
    success_url = '/recipes/profile/settings'

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(success_url)
    else:
        form = PasswordChangeForm(user=request.user)
        context={'form':form}
        return render(request, template_name, context)

def DeleteUser(request):
    model = request.user
    template_name = 'recipes/UserDelete.html'
    success_url = '/recipes'

    if request.method == 'POST':
        model.delete()
        return redirect(success_url)
    else:
        context = {}
        return render(request, template_name, context)


#---------------------------RECIPE---------------------------#
class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipes/RecipeDetail.html'

    def get(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        form = CommentForm(request.POST or None)
        print(model.categories.names)
        context = {'recipe': model, 'form': form, 'current_user' : self.request.user.id, 'comments' : Comment.objects.filter(recipe=pk, reply=None).order_by('.id')}

        return render(request, self.template_name, context)

    def post(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        form = CommentForm(request.POST or None)
        context = {'recipe': model,'form': form}

        if form.is_valid():
            content = request.POST.get("content")
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(recipe=model, author=self.request.user, content=content, reply=comment_qs)
            comment.save()

        else:
            form = CommentForm()

        context = {
            'recipe' : model,
            'comments' : Comment.objects.filter(recipe=pk, reply=None).order_by('.id'),
            'form' : form
        }

        if request.is_ajax():
            html = render_to_string('recipes/RecipeComments.html', context, request=request)
            return JsonResponse({'form': html})

        return render(request, 'recipes/RecipeDetail.html', context)

class RecipeDelete(DeleteView):
    template_name = 'recipes/RecipeDelete.html'
    success_url = '/recipes'

    def get(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        context = {'recipe': model, 'form': RecipeEditPhotoForm()}
        return render(request, self.template_name, context)

    # Check if the current user is authorized to delete this recipe.
    def authorization(self, request, recipe_pk):
        print('Recipe id: ', recipe_pk)
        print('User id: ', request.user.id, 'Author id: ', Recipe.objects.get(pk = recipe_pk).author_id)
        if(request.user.id == Recipe.objects.get(pk = recipe_pk).author_id):
            print('authorization true')
            return True
        print('authorization false')
        return False

    # Redirect user.
    def dispatch(self, request, *args, **kwargs):
        if(not self.authorization(request, self.kwargs['pk'])):
            print('Redirecting to /recipes')
            return redirect('/recipes')
        return super().dispatch(request, *args, **kwargs)

class RecipeEdit(UpdateView):
    model = Recipe
    template_name = 'recipes/RecipeEdit.html'
    form_class = RecipeEditForm
    success_url = '/recipes'

    def post(self, request, pk):
        return HttpResponseRedirect(self.success_url + '/recipe/'+str(pk))

    # Check if the current user is authorized to edit this recipe.
    def authorization(self, request, recipe_pk):
        print('Recipe id: ', recipe_pk)
        print('User id: ', request.user.id, 'Author id: ', Recipe.objects.get(pk = recipe_pk).author_id)
        if(request.user.id == Recipe.objects.get(pk = recipe_pk).author_id):
            print('authorization true')
            return True
        print('authorization false')
        return False

    # Redirect user.
    def dispatch(self, request, *args, **kwargs):
        if(not self.authorization(request, self.kwargs['pk'])):
            print('Redirecting to /recipes')
            return redirect('/recipes/')
        return super().dispatch(request, *args, **kwargs)

class RecipeEditPhoto(View):
    template_name = 'recipes/RecipeEditPhoto.html'

    def get(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        form = RecipeEditPhotoForm()
        context = {'recipe': model, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        form = RecipeEditPhotoForm(request.POST, request.FILES)
        context = {'recipe':model, 'form': form}
        photos = Photo.objects.filter(recipe=pk)
        in_memory_files = request.FILES.getlist('photo')
        length_of_files = len(in_memory_files) + len(photos)

        print('length of files:', length_of_files, ', in_memory_files:',len(in_memory_files), ', existing photos:', len(photos))

        if(length_of_files < settings.FILE_UPLOAD_LIMIT + 1):
            if(form.is_valid):
                for f in in_memory_files:
                    photo = Photo(image = f,recipe = model)
                    photo.save()
                    print(photo.image.name, ": ", photo.image.url)
        else:
            messages.error(request, 'Total number of images exceeded. Users can only have ', settings.FILE_UPLOAD_LIMIT, 'images.')

        return HttpResponseRedirect('/recipes/recipe/'+str(pk)+'/edit-photo')

    # Check if the current user is authorized to edit this recipe.
    def authorization(self, request, recipe_pk):
        print('Recipe id: ', recipe_pk)
        print('User id: ', request.user.id, 'Author id: ', Recipe.objects.get(pk = recipe_pk).author_id)
        if(request.user.id == Recipe.objects.get(pk = recipe_pk).author_id):
            print('authorization true')
            return True
        print('authorization false')
        return False

    # Redirect user.
    def dispatch(self, request, *args, **kwargs):
        if(not self.authorization(request, self.kwargs['pk'])):
            print('Redirecting to /recipes')
            return redirect('/recipes/')
        return super().dispatch(request, *args, **kwargs)

class RecipeEditThumbnail(View):
    template_name = 'recipes/RecipeEditThumbnail.html'

    def get(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        context = {'recipe': model, 'form': RecipeEditThumbnailForm()}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        model = Recipe.objects.get(pk=pk)
        form = RecipeEditThumbnailForm(request.POST, request.FILES)
        context = {'recipe':model, 'form': form}
        thumbnails = Thumbnail.objects.filter(recipe=pk)
        length_of_files = len(thumbnails)

        print('length of files:', length_of_files)

        if(length_of_files > 0):
            for t in thumbnails:
                t.delete()

        if(form.is_valid):
            tmp_thumbnail = request.FILES.get('thumbnail', None)
            if(not tmp_thumbnail == None):
                thumbnail = Thumbnail(image=tmp_thumbnail, recipe=model)
                thumbnail.save()
                print(thumbnail.image.name, ": ", thumbnail.image.url)

        return HttpResponseRedirect('/recipes/recipe/'+str(pk)+'/edit-thumbnail')

    # Check if the current user is authorized to edit this recipe.
    def authorization(self, request, recipe_pk):
        print('Recipe id: ', recipe_pk)
        print('User id: ', request.user.id, 'Author id: ', Recipe.objects.get(pk = recipe_pk).author_id)
        if(request.user.id == Recipe.objects.get(pk = recipe_pk).author_id):
            print('authorization true')
            return True
        print('authorization false')
        return False

    # Redirect user.
    def dispatch(self, request, *args, **kwargs):
        if(not self.authorization(request, self.kwargs['pk'])):
            print('Redirecting to /recipes')
            return redirect('/recipes/')
        return super().dispatch(request, *args, **kwargs)

@login_required(login_url="/recipes/login")
def RecipeCreate(request):
    if request.method == "POST":
        form = RecipeManualForm(request.POST, request.FILES)
        length_of_files = len(request.FILES.getlist('photo'))
        print("The length of photo: ", length_of_files)

        if form.is_valid():

            # Create Recipe
            r = Recipe.objects.create(
                recipe_title=form.cleaned_data['recipe_title'],
                creation_date=datetime.date.today(),
                author=request.user,
                instructions=form.cleaned_data['instructions'],
                descriptions=form.cleaned_data['descriptions']
            )

            # Create Ingredient
            count = int(request.POST.get('ingredient_field_count'))
            for i in range(count):
                tmpQty = request.POST.get('qty{i}'.format(i = i))
                tmpIng = request.POST.get('ing{i}'.format(i = i))

                print("Quantity : " + tmpQty)
                print("Ingredient : " + tmpIng)

                r.ingredient_set.create(
                    recipe=Recipe.objects.get(pk=r.id),
                    ingredient_name= tmpQty + ' ' + tmpIng
                )
                i = i + 1

            # Get files from ImageField. Save them.
            for f in request.FILES.getlist('photo'):
                photo = Photo(image = f,recipe = Recipe.objects.get(pk=r.id))
                photo.save()
                print(photo.image.name, ": ", photo.image.url)

            tmp_thumbnail = request.FILES.get('thumbnail', None)
            if(not tmp_thumbnail == None):
                thumbnail = Thumbnail(image=tmp_thumbnail, recipe=Recipe.objects.get(pk=r.id))
                thumbnail.save()
                print(thumbnail.image.name, ": ", thumbnail.image.url)


            categories_names = form.cleaned_data['categories_names']
            for categories_name in categories_names:
                r.categories.add(categories_name)

            # Redirect to recipes details once form is submitted.
            return HttpResponseRedirect('/recipes/recipe/'+str(r.id)+'/')
        else:
            print("Form is not valid. Errors with the following: ")
            print(form.errors)
    else :
        form = RecipeManualForm()
    return render(request, "recipes/RecipeNew.html", {'form': form})

#---------------------------MENU---------------------------#

def MenuDetail(request, pk):
    template_name = 'menus/MenuDetail.html'
    context = {
        'recipe_list': Menu.objects.get(pk=pk).recipes.all(),
        'menu': Menu.objects.get(pk=pk)
    }
    return render(request, template_name, context)

class MenuEdit(UpdateView):
    model = Menu
    template_name = 'menus/MenuEdit.html'
    # fields = ['__all__']
    fields = ['title', 'recipes']
    def get_success_url(self):
        menu_id=self.kwargs['pk']
        return reverse_lazy('recipes:menu_detail', kwargs={'pk': menu_id})

class MenuCreate(CreateView):
    template_name = 'menus/MenuNew.html'
    form_class = MenuCreateForm
    def get_success_url(self):
        return reverse_lazy('recipes:index')

class MenuDelete(DeleteView):
    model = Menu
    template_name = 'menus/MenuDelete.html'
    def get_success_url(self):
        return reverse_lazy('recipes:index')

class MenuList(ListView):
    template_name = 'menus/MenuList.html'
    context_object_name = 'menu_list'
    def get_queryset(self):
        return Menu.objects.all()

#---------------------------AJAX---------------------------#

def delete_photo_ajax(request):
    print('delete photo ajax called')

    #Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    photo_id = json_data['photo_id']

    print('photo id: ', photo_id)
    if not photo_id == None:
        Photo.objects.get(id=photo_id).delete()
        data = {'success':True}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to delete photo.'
    return JsonResponse(data)

def delete_thumbnail_ajax(request):
    print('delete thumbnail ajax called')

    #Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    thumbnail_id = json_data['thumbnail_id']

    print('thumbnail id: ', thumbnail_id)

    if not thumbnail_id == None:
        Thumbnail.objects.get(id=thumbnail_id).delete()
        data = {'success':True}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to delete photo.'
    return JsonResponse(data)

def delete_ingredient_ajax(request):
    print('delete ingredient ajax called')

    #Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    ingredient_id = json_data['ingredient_id']

    print('ingredient id: ', ingredient_id)
    if not ingredient_id == None:
        ingredient = Ingredient.objects.get(id=ingredient_id)
        recipe = ingredient.recipe
        ingredient.delete()
        
        #Convert to html to re-render
        context = {"recipe":recipe}
        ingredients_html = render_to_string('recipes/RecipeIngredientsTable.html', context, request=request)

        data = {'success':True, 'recipe':ingredients_html}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to delete ingredient.'
    return JsonResponse(data)

def update_ingredient_ajax(request):
    print('update ingredient ajax called')

    #Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    ingredient_id = json_data['ingredient_id']
    ingredient_title = json_data['ingredient_title']

    print('ingredient id: ', ingredient_id)
    print('ingredient title: ', ingredient_title)
    if not ingredient_id == None and not ingredient_title == None:
        Ingredient.objects.filter(id=ingredient_id).update(ingredient_name=ingredient_title)
        ingredient = Ingredient.objects.get(id=ingredient_id)
        
        #Convert to html to re-render
        context = {"recipe":ingredient.recipe}
        ingredients_html = render_to_string('recipes/RecipeIngredientsTable.html', context, request=request)

        data = {'success':True, 'recipe':ingredients_html}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to update ingredient.'
    return JsonResponse(data)

def add_ingredient_ajax(request):
    print('add ingredient ajax called')

    #Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    recipe_id = json_data['recipe_id']
    ingredient_title = json_data['ingredient_title']

    print(recipe_id)
    print(ingredient_title)
    if not ingredient_title == None and not recipe_id == None:
        recipe = Recipe.objects.get(id=recipe_id)
        ingredient = Ingredient(ingredient_name=ingredient_title, recipe=recipe)
        ingredient.save()

        #Convert to html to re-render
        context = {"recipe":recipe}
        ingredients_html = render_to_string('recipes/RecipeIngredientsTable.html', context, request=request)

        data = {'success':True, 'recipe':ingredients_html}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to update ingredient.'
    return JsonResponse(data)

def update_instructions_ajax(request):
    print('update instructions ajax called')

    # Decode JSON and extract variables.
    data = request.body.decode('utf-8')
    json_data = json.loads(data)
    recipe_id = json_data['recipe_id']
    instructions = json_data['instructions']

    print(recipe_id)
    print(instructions)
    if not instructions == None and not recipe_id == None:
        Recipe.objects.filter(id=recipe_id).update(instructions=instructions)
        recipe = Recipe.objects.get(id=recipe_id)

        # Convert to html to re-render
        context = {"recipe":recipe}
        instructions_html = render_to_string('recipes/RecipeInstructions.html', context, request=request)

        data = {'success':True, 'recipe':instructions_html}
    else:
        data = {'success':False}
    if(not data['success']):
        data['error_msg'] = 'failed to update ingredient.'
    return JsonResponse(data)