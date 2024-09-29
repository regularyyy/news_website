from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    
def __str__(self):
    return self.title
