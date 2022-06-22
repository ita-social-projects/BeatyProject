"""This module is for testing DELETE method that is used to inactivate Business."""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from api.models import Business
from .factories import BusinessFactory, CustomUserFactory
from ..serializers.business_serializers import BusinessGetAllInfoSerializers


class TestDeleteBusiness(TestCase):
    """This class represents a Test case for the making Business inactive.

    All the needed information is submitted in the setUp method.
    """

    def setUp(self) -> None:
        """This method adds needed info for tests."""
        self.owner = CustomUserFactory(first_name="OwnerUser")
        self.user1 = CustomUserFactory.create(is_active=True)

        self.business1 = BusinessFactory.create(name="Business1", owner=self.owner)
        self.business2 = BusinessFactory.create(name="Business2", owner=self.owner)

        self.serializer = BusinessGetAllInfoSerializers

        self.client = APIClient()
        self.client.force_authenticate(user=self.owner)

    def test_delete_business(self):
        """Business can make himself inactive."""
        response = self.client.delete(
            path=reverse(
                "api:business-detail",
                kwargs={"pk": self.business1.id},
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Business.objects.get(pk=1).is_active)

    def test_delete_business_by_other_user(self):
        """Business can't become inactive by another user."""
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(
            path=reverse(
                "api:business-detail",
                kwargs={"pk": self.business2.id},
            ),
        )
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Business.objects.get(pk=self.business2.id).is_active)
