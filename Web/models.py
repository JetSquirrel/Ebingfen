from django.db import models

# Create your models here.
class college(models.Model):
    name = models.CharField(u'学院', max_length=20)
    title = models.CharField(u'标题', max_length=20)
    url = models.CharField(u'地址', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class active(models.Model):
    title = models.CharField(u'标题', max_length=20)
    url = models.CharField(u'地址', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class tinker(models.Model):
    title = models.CharField(u'标题', max_length=20)
    url = models.CharField(u'地址', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class banner(models.Model):
    title = models.CharField(u'标题', max_length=20)
    url = models.CharField(u'地址', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    ban = models.ImageField()
    def __str__(self):
        return self.title