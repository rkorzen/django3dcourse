from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ksiazka"
        verbose_name_plural = "ksiazki"
