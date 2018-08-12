from django.db import models

class Chicken(models.Model):
    name = models.CharField(default='Chickenstuff', max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.description
    def summary(self):
        return self.description[:100]
