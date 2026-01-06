from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.title or f'Note {self.pk}'
