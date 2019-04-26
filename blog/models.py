from django.db import models
from datetime import datetime
# Create your models here.
class Posts(models.Model):
    title =  models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name_plural = "Posts"
    def __str__(self):
        return self.title