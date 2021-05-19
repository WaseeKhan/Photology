from django.db import models


# Create your models here.
class Hero(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pic = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images', default='image.svg')

    def __str__(self):
        return self.title

    def get_cat_no(self):
        return self.title.all().count()


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pic = models.ImageField(upload_to='images')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogCat(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    tag = models.CharField(max_length=10)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    blogImg = models.ImageField(upload_to='blogImages', default='image.svg')
    category = models.ForeignKey(BlogCat, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
