from rest_framework import serializers
from .models import Item  # Ensure this import points to your Item model

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # or specify the fields you want to serialize
