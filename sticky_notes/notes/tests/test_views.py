from django.test import TestCase
from django.urls import reverse
from ..models import Note


class NoteViewsTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Sample Note",
            content="Sample content"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Note")

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update_view(self):
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {'title': 'Updated', 'content': 'Updated content'}
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated')

    def test_note_delete_view(self):
        response = self.client.post(
            reverse('note_delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)
