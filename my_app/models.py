from django.db import models

# Create your models here.
class Brand (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Madel (models.Model):
    name=models.CharField(max_length=50)
    brand=models.ForeignKey(Brand, models.DO_NOTHING,null=True, blank=True )
    def __str__(self):
        return self.name

class Product (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    color = models.CharField(max_length=20)
    memory = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    madel = models.ForeignKey(Madel, models.DO_NOTHING)

    def __str__(self):
        return f"{self.title} {self.description} {self.color} {self.memory}"