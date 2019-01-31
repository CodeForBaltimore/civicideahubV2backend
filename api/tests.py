from django.test import TestCase
from .models import Idea
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    """This class defines the test suite for the idea model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username='testuser')
        self.idea_name = "Write world class code"
        self.idea = Idea(name=self.idea_name, owner=user)

    def test_model_can_create_an_idea(self):
        """Test the idea model can create a idea."""
        old_count = Idea.objects.count()
        self.idea.save()
        new_count = Idea.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')

        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.idea_data = {'name': 'Clean up litter', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.idea_data,
            format="json")

    def test_api_can_create_an_idea(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        new_client = APIClient()
        response = new_client.get('/ideas/', kwargs={'pk': 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_an_idea(self):
        idea = Idea.objects.get()
        response = self.client.get(
                        reverse('details', kwargs={'pk': idea.id})
                        ,format='json'
                    )      

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, idea)

    def test_api_can_update_idea(self):
        idea = Idea.objects.get()
        change_idea = {'name' : 'Something new'}
        response = self.client.put(
            reverse('details', kwargs={'pk': idea.id}),
            change_idea, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_idea(self):
        idea = Idea.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': idea.id}),
            format = 'json',
            follow = True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        