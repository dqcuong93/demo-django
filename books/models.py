from django.db import models
from django.contrib.auth.models import User
from .search import BookIndex


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    # Add indexing method to Book
    def indexing(self):
        obj = BookIndex(
            index={'id': self.id},
            title=self.title,
            content=self.content,
            created_at=self.created_at,
            user=self.user.username,
        )
        obj.save()
        return obj.to_dict(include_meta=True)
