

# Create your tests here.
from django.test import TestCase
from notes.models import Note

class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "This is a test note")

    def test_string_representation(self):
        note = Note.objects.create(
            title="My Note",
            content="Content"
        )
        self.assertEqual(str(note), "My Note")
