from modules.models import Category
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.core.paginator import Paginator

def category_by_id(request, item_id):
    try:
        category = Category.objects.get(id=item_id)
        serialized_category = category_serializer(category).data
        return JsonResponse(serialized_category)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)

class category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'logo', 'parent']

def find_filtered_categories(request, category_id, page, limit):
    try:

        all_categories = Category.objects.all()
        if category_id:
            all_categories = all_categories.filter(parent=category_id)
        paginator = Paginator(all_categories, limit)
        categories_page = paginator.get_page(page)

        serialized_categories = []
        for category in categories_page:
            serialized_category = category_serializer(category).data
            serialized_categories.append(serialized_category)

        return JsonResponse(
            {"categories": serialized_categories, "page": page, "limit": limit, "total_pages": paginator.num_pages})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Categories not found"}, status=404)