from django.db import models
from users.models import Users
# Create your models here.

class Videos(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    verbose_name = models.CharField(max_length=30)
    visibility = models.BooleanField(default= True)
    rated = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add= True)
    video = models.FileField(upload_to='uploads/videos/%Y/%m/%d/', default='default.mp3')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name