from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import note_list, note_create


class UrlTests(SimpleTestCase):

    def test_note_list_url_resolves(self):
        url = reverse('note_list')
        self.assertEqual(resolve(url).func, note_list)

    def test_note_create_url_resolves(self):
        url = reverse('note_create')
        self.assertEqual(resolve(url).func, note_create)
