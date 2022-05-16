from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ThingTest(TestCase):
    def test_list_view(self):
        url = reverse('things_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_list_page_templet(self):
        url = reverse('things_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'things_list.html')

    def test_detail_view(self):
        url = reverse()
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_detail_page_templet(self):
        url = reverse('things_detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'things_detail.html')
        