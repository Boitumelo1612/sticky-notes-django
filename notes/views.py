# notes/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Note
from django.shortcuts import render


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Note.objects.create(title=title, content=content)

    notes = Note.objects.all()
    return render(request, "notes/home.html", {"notes": notes})


class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 20


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:list')


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')
