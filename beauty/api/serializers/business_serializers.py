"""The module includes serializers for Business model."""
from rest_framework import serializers

from api.models import Business


class BusinessesSerializer(serializers.ModelSerializer):
    """Serializer for business base fields."""

    name = serializers.CharField(max_length=20)
    type = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=500)

    class Meta:
        """Meta for OwnerBusinessesSerializer class."""

        model = Business
        fields = ("name", "type", "address")


class BusinessAllDetailSerializer(serializers.ModelSerializer):
    """Serializer for specific business."""

    owner_name = serializers.SerializerMethodField()
    created_at = serializers.ReadOnlyField()
    address = serializers.CharField(max_length=500)

    def get_owner_name(self, obj):
        """Return full name of business owner."""
        return f'{obj.owner.first_name} {obj.owner.last_name}'

    class Meta:
        """Meta for BusinessDetailSerializer class."""

        model = Business
        fields = ("owner_name", "created_at", "logo", "name", "type", "address", "description",)


class BusinessDetailSerializer(serializers.ModelSerializer):
    """Serializer for specific business."""

    address = serializers.CharField(max_length=500)

    class Meta:
        """Meta for BusinessDetailSerializer class."""

        model = Business
        fields = ("logo", "name", "type", "address", "description",)