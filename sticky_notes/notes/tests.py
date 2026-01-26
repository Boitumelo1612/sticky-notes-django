from django.test import TestCase
from django.urls import reverse
from .models import Note


# Create your tests here.
class NoteTests(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note",
                                        content="Test Content")

    def test_list_notes(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_create_note(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.last().title, 'New Note')

    def test_update_note(self):
        response = self.client.post(reverse('note_update',
                                            args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        response = self.client.post(reverse('note_delete',
                                            args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
