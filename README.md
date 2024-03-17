1)run requirements file: pip install -r requirements.txt

2)update database configuration file:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Luka1234!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



run the application: python manage.py runserver
admin page: http://127.0.0.1:8000/admin/
create super user for admin page: python manage.py createsuperuser

endpoints:
http://127.0.0.1:8000/api/block/get?item_id=abc ბლოკის წამოღება აიდის მიხედვით
http://127.0.0.1:8000/api/blocks?page=1&limit=1 ყველა ბლოკის წამოღება

http://127.0.0.1:8000/api/menu/get?item_id=1 მენიუს წამოღება აიდის მიხედვით(order)
http://127.0.0.1:8000/api/menus?page=1&limit=1&category_id=abc ყველა მენიუების წამოღება 

http://127.0.0.1:8000/api/category/get?item_id=abc კატეგორიის წამოღება აიდის მიხედვით
http://127.0.0.1:8000/api/categories?limit=10&page=1&category_id=abc ყველა კატეგორიის წამოღება 
