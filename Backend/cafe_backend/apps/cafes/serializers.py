from rest_framework import serializers
from . models import Cafe


class CafeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ["id", "name", "cafe_ID", "Description", "Owner"]
        read_only_fields = ["owner", "id"]
