# Category tree management

This Django project manages hierarchical categories and their similarities using the `django-mptt` library for efficient tree traversal. It includes API endpoints for CRUD operations on categories and similarities, accessible by both ID and name. The project structure is organized with models, serializers, views, and templates, ensuring clean and maintainable code.

Project is done with abstract interpretation. It is made with assumption without knowing the context behind. For example, description for relation of category similarities and categories is abstract, so it is implemented with one of the possible contexts. That's my first experience with Django, so I left some comments to easily remind myself what is the purpose of the implementation in case I forget and consciously left them for the interview, because I generally see it as a good practice - comments like that can ease onboarding/readability/understanding of a new member. 

Uploading project with the data I imported, containing one image and data from scripts in sqllite file. In order to flush the data just execute command at `Flush database in case`. 

### Endpoints

Router Endpoints
```
/api/categories/
/api/similarities/
```
UI Lists
```
/category-list/
/category-similarities-list/
```

Categories Endpoints
```
/updatebyname/<str:name>/
/deletebyname/<str:name>/
/getbyname/<str:name>/
/getbyparentname/<str:parent_name>/
/getallcategories/
/getbylevel/<int:level>/
```

Similarities Endpoints
```
/updatebya/<str:name>/
/deletebya/<str:name>/
/getbya/<str:name>/
/getallsimilarities/
/create/
```

Potential Authentication - currently its commented out, just to make project testing easier and focus on core task implementation. To be functional, additional settings should be put in `REST_FRAMEWORK` in `settings.py`.
```
/token/
/token/refresh/
/register/
```

Simple caching is added to `category-list` just to tackle a bit this opportunity. Config is `CACHES` in `settings.py`.

Basic debugging is managed from `LOGGING` in `settings.py`. Data is dumped into `debug.log` file.

`category_manager/categories/templates` contains basic frontend listing templates of similarities and categories (which is recursive for each parent to child).

`category_manager/categories/management/commands/list_cache.py` is just made to check cache. Really simple command for the purpose.

Admin panel which can check all data and manage it example if it's run on local server - `http://127.0.0.1:8000/admin/categories/category/`.

`category_manager/media/category_images` will be used for static dir holding all the uploaded images.

`toml` file is used for really basic configurations.

### Install required libraries
```commandline
pip install -r requirements.txt
```


### Run the migrations to create the necessary database tables.
```
python manage.py makemigrations / python manage.py makemigrations categories
python manage.py migrate
```

### Create superuser for admin panel
```commandline
python .\manage.py createsuperuser
```


### Run the server
```commandline
python manage.py runserver
```



### Flush database in case
```commandline
python manage.py flush
```


### Run Tests

```commandline
python manage.py test
```


### Interact with API using scripts in context of testing endpoints
In `category_manager/scripts` the files are meant to simulate basic adding/updating/deleting/getting interaction.

`example_category_requests.py` is interacting with categories, categories are randomly named.

`example_similarity_requests.py` is interacting with similarities on top of categories.

`example_rabbit_hole_category_set.py` is adding needed categories and similarities to simulate gathering rabbit holes and rabbit islands.

`rabbit_holes.py` is finding the longest similar category "rabbit hole" and the categories it's comprised of with hardcoded 'A' and 'C'. Also finding the categories in each "rabbit island". That is based on `example_rabbit_hole_category_set.py` inserts. 



### Possible points of improvement
1. Adding more tests, checking all APIs or load/stress tests.
2. Adding more elaborate database
3. Adding authentication
4. More granular logging
5. More robust engine like Gunicorn
6. Infrastructure resource creation automatization in order to be uploaded to cloud
7. Separating blob storage for images
8. Creating image for containerization
