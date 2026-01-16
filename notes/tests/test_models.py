from django.test import TestCase
from ..models import Note


class NoteModelTest(TestCase):

    def test_create_note(self):
        note = Note.objects.create(
            title="Test Note",
            body="This is a test note"
        )
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.body, "This is a test note")
        self.assertIsNotNone(note.id)

    def test_string_representation(self):
        note = Note.objects.create(
            title="My Note",
            content="Content"
        )
        self.assertEqual(str(note), "My Note")
