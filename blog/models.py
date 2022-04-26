from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model): #Post table
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to="video/", null=True, verbose_name="", blank=True)


    def __str__(self):
        return self.title + ":" + str(self.videofile)


