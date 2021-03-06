from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=1)
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    def __str__(self):
        return self.description