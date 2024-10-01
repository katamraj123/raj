from django.core.cache import cache
from rest_framework.views import APIView


class ItemDetailView(APIView):
    def get(self, request, item_id):
        cache_key = f"item_{item_id}"
        item = cache.get(cache_key)

        if not item:
            item = Item.objects.filter(id=item_id).first()
            if not item:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            cache.set(cache_key, item, timeout=300)  # cache for 5 minutes

        serializer = ItemSerializer(item)
        return Response(serializer.data)
