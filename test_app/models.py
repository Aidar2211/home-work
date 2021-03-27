from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product_Name(models.Model):
    title = models.CharField(verbose_name='title', max_length=150)
    description = models.TextField(verbose_name='Description of product: ')
    price = models.CharField(verbose_name='price', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product_Name, on_delete=models.CASCADE,
                                verbose_name='name of product')
    name = models.CharField(max_length=80, verbose_name='user name')
    body = models.TextField(verbose_name='text')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




