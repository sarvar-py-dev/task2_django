from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)
    message_num = models.IntegerField(default=0)
    image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return self.title
