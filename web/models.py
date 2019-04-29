from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=36,verbose_name="书名")
    price = models.IntegerField(verbose_name="价格")
    publish = models.CharField(max_length=30,verbose_name="出版社")

    def __str__(self):
        return self.title
