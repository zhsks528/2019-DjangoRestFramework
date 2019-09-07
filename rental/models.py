from django.conf import settings
from django.db import models

class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Belonging(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
