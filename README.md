# ReCity
## Web App for Recipes

A web app that allows you to view different types of recipes and shared by other users. You can also create your own recipes and share them with other users.

## Key Features 
- View/Create/Edit Recipes
- Nutritional Data for each recipe
- Create Menus consisting of multiple recipes
- Easy to navigate UI
- Tag based filtering to see recipes from a particular cuisine 
- Dark Mode :)
- Slick homepage 

![](ccgapp_preview.gif)

Credit to Raffi Maurer and Tahmid Uddin for the demo snippet

## Important 
To run the app successfully on your device you will need to do the following : 

- You will need to set up a S3 bucket, RDS Database and signup for Nutrionix API
- Once you have done that you will need to enter all the access id/keys in the specified strings in the settings.py file located at recipe_cca/settings.py

## Usage

To start the app : ``python manage.py runserver``


## Guide to files inside /recipes

**admin.py**	Changes to Django admin interface

**apps.py**		Configure app + sub-apps

**models.py**	Model schema + methods

**tests.py**		Test cases

**urls.py**		URL patterns / routes

**views.py**		Generate views


## Contributions
- Jalp Desai 
- Tahmid Uddin (https://github.com/TahmidU)
- Raffi Maurer (https://github.com/raffimaurer)

