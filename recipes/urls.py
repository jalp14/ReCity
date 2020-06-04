from django.conf.urls import url
from django.urls import path, include, reverse
from .views import *
from accounts import views as account_views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'recipes'
urlpatterns = [
    # GENERAL
    path('', IndexView, name='index'),
    path('profile/', ProfileView, name='profile'),
    path('profile/settings', UserSettings, name='settings'),
    path('profile/settings/<int:pk>/change-username', ChangeUsername.as_view(), name='change_username'),
    path('profile/settings/change-password', ChangePassword, name='change_password'),
    path('profile/settings/delete-account', DeleteUser, name='delete_account'),

    # RECIPES
    path('all/', RecipeAll.as_view(), name='all'),
    path('<int:cat_id>/', RecipeCategory, name='category'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/new/', RecipeCreate, name='recipe_new'),
    path('recipe/<int:pk>/edit', RecipeEdit.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/edit-photo', RecipeEditPhoto.as_view(), name='recipe_edit_photo'),
    path('recipe/<int:pk>/edit-thumbnail', RecipeEditThumbnail.as_view(), name='recipe_edit_thumbnail'),
    path('recipe/<int:pk>/delete', RecipeDelete.as_view(), name='recipe_delete'),

    #AJAX
    path('recipe/delete-photo-ajax/', delete_photo_ajax, name='delete_photo_ajax'),
    path('recipe/delete-thumbnail-ajax/', delete_thumbnail_ajax, name='delete_thumbnail_ajax'),
    path('recipe/delete-ingredient-ajax/', delete_ingredient_ajax, name='delete_ingredient_ajax'),
    path('recipe/update-ingredient-ajax/', update_ingredient_ajax, name='update_ingredient_ajax'),
    path('recipe/add-ingredient-ajax/', add_ingredient_ajax, name='add_ingredient_ajax'),
    path('recipe/update-instructions-ajax/', update_instructions_ajax, name='update_instructions_ajax'),

    # MENUS
    path('menu/all', MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>/', MenuDetail, name='menu_detail'),
    path('menu/new/', MenuCreate.as_view(), name='menu_new'),
    path('menu/<int:pk>/edit', MenuEdit.as_view(), name='menu_edit'),
    path('menu/<int:pk>/delete', MenuDelete.as_view(), name='menu_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)