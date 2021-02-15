from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)



    def __str__(self):
        return self.title
