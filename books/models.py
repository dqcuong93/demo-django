from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
