from django.db import models

class SiteContent(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.CharField (max_length=400)



class Suggessions(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    suggession = models.TextField(max_length=500)
