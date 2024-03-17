from modules.models import Menu
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.core.paginator import Paginator


def menu_by_id(request, menu_id):
    try:
        menu = Menu.objects.get(order=menu_id)
        serialized_menu = menu_serializer(menu).data
        return JsonResponse(serialized_menu)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Menu not found"}, status=404)


class menu_serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['order', 'name']

def find_filtered_menus(request, category_id, page, limit):
    try:

        all_menus = Menu.objects.all()
        if category_id:
            all_menus = all_menus.filter(category=category_id)
        paginator = Paginator(all_menus, limit)
        menus_page = paginator.get_page(page)

        serialized_menus = []
        for menu in menus_page:
            serialized_menu = menu_serializer(menu).data
            serialized_menus.append(serialized_menu)

        return JsonResponse(
            {"menus": serialized_menus, "page": page, "limit": limit, "total_pages": paginator.num_pages})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Menus not found"}, status=404)