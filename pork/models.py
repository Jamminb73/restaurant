from django.db import models

class Pork(models.Model):
    name = models.CharField(default='Porkstuff', max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.description
    def summary(self):
        return self.description[:100]
