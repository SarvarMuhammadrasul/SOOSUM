from django.db import models

# Create your models here.
from django.db import models
# Create your models here.


class Info(models.Model):
    logo = models.ImageField()
    text_uz = models.TextField()
    text_ru = models.TextField()
    


class SocialMedia(models.Model):
    img = models.ImageField()
    link = models.CharField(max_length=255)


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Product(models.Model):
    img = models.ImageField()
    text_uz = models.CharField(max_length=255)
    text_ru = models.CharField(max_length=255)
    price = models.IntegerField()


class AboutProduct(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField()


class UnityProduct(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField()


class AboutCompany(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    photo = models.ImageField()


class WhoUse(models.Model):
    title_uz = models.TextField()
    title_ru = models.TextField()


class HowToUse(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru= models.TextField()
    img = models.ImageField()

class Fact(models.Model):
    number = models.IntegerField()
    text_uz = models.TextField()
    text_ru = models.TextField()