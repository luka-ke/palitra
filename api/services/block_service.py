from modules.models import Block, Menu
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.core.paginator import Paginator


def block_by_id(request, block_id):
    try:
        block = Block.objects.get(id=block_id)
        serialized_block = block_serializer(block).data
        return JsonResponse(serialized_block)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Block not found"}, status=404)


class block_serializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'title', 'articles', 'vizualType', 'position', 'display_title']



def find_filtered_blocks(request, page, limit):
    try:

        all_blocks = Block.objects.all()

        paginator = Paginator(all_blocks, limit)
        blocks_page = paginator.get_page(page)

        serialized_blocks = []
        for block in blocks_page:
            serialized_block = block_serializer(block).data
            serialized_blocks.append(serialized_block)

        return JsonResponse(
            {"blocks": serialized_blocks, "page": page, "limit": limit, "total_pages": paginator.num_pages})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Block not found"}, status=404)
