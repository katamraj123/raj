from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # Add this line
from .serializers import ItemSerializer  # Ensure you import your serializer
from .models import Item



import logging

logger = logging.getLogger(__name__)

def example_view(request):
    try:
        # Your code logic here
        logger.info("Example view accessed successfully")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return Response({"error": "An error occurred"}, status=500)


# Create your views here.
class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, item_id):
        item = self.get_object(item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, item_id):
        item = self.get_object(item_id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ItemDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, item_id):
        item = self.get_object(item_id)
        item.delete()
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)