from .models import Items
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
  class Meta:
    model = Items
    fields ="__all__"