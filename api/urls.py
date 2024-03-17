from ninja import NinjaAPI
from django.urls import path
from django.contrib import admin
from .services.block_service import block_by_id, find_filtered_blocks
from .services.category_service import category_by_id, find_filtered_categories
from .services.menu_service import menu_by_id, find_filtered_menus


api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return {"message": "Hello, world!"}

@api.get("/block/get")
def get_block_by_id(request, item_id: str):
    return block_by_id(request, item_id)

@api.get("/blocks")
def find_blocks(request, page: int, limit: int):
    return find_filtered_blocks(request, page, limit)


@api.get("/menu/get")
def get_menu_by_id(request, item_id: int):
    return menu_by_id(request, item_id)

@api.get("/menus")
def find_menus(request, page: int, limit: int, category_id: str = None):
    return find_filtered_menus(request, category_id, page, limit)

@api.get("/category/get")
def get_category_by_id(request, item_id: str):
    return category_by_id(request, item_id)

@api.get("/categories")
def find_categories(request, page: int, limit: int, category_id: str = None):
    return find_filtered_categories(request, category_id, page, limit)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]