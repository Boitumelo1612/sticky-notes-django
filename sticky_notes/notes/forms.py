from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # explicit is safer than '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short title (max 200 chars)'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Write your note here...'
            }),
        }
        help_texts = {
            'title': 'Give the note a short, descriptive title.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        if len(title) > 200:
            raise forms.ValidationError(
                'Title must be 200 characters or fewer.'
            )
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        # Example: prevent purely whitespace notes
        if content == '':
            return content  # allow empty content if desired; otherwise
        # raise error
        # Optional: add sanitization here if you accept HTML
        return content
