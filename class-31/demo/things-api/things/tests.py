from django.test import TestCase
from .models import Thing
from django.contrib.auth import get_user_model


# Create your tests here.
class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_thing = Thing.objects.create(name="rake", wner=testuser1, description="Better than shovel for leaves.")
        test_thing.save()

    def test_things_model(self):
        thing = Thing.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(actual_description, "Better than shovel for leaves.")
