from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .validators import validate_file_extension
# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    title = models.CharField(max_length= 200)
    description = models. TextField(null=True, blank = True)
    date_posted = models.DateTimeField(default=timezone.now)
    create =  models.DateTimeField(auto_now_add = True)
    writer = models.CharField(max_length=100,null=True)
    # tuong duong author
    pdf = models.FileField(upload_to="uploads/",null=True,validators=[validate_file_extension])
    # tuong duong book
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_posted']