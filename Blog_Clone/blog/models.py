from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # Content can be as long as it wants
    date_posted = models.DateTimeField(default=timezone.now)
   # auto_now_add=True will keep the date it was created and wont change it
    author = models.ForeignKey(User, on_delete=models.CASCADE)
   # CASCADE will delete the posts of the author if the author is deleted

    def __str__(self):
        return self.title
