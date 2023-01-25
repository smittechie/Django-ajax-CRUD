from django.db import models


# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField()


class Product(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)


class Mobile(models.Model):
    Mobile = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100, default="White")
    RAM = models.CharField(max_length=100, default="2 GB")
    Price = models.IntegerField(default=140000)
