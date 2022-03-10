from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snack


class SnacksTests(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username="tester", email="tester@email.com", password="pass")
    self.snack = Snack.objects.create(
      name = 'Gardettos', purchaser = self.user, description = 'breadsticks is yum')

  def test_string_representation(self):
    self.assertEqual(str(self.snack), 'Gardettos')

  def test_snack_name(self):
    self.assertEqual(f'{self.snack.name}', 'Gardettos')

  def test_list_page_status_code(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_list_page_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')
    self.assertTemplateUsed(response, 'base.html')