from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    checked = models.BooleanField()
    checked_date = models.DateTimeField(blank=True, null=True)
    created_data = models.DateTimeField(default=timezone.now)
    due_data = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(default=1)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title