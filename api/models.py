from django.db import models

class Product(models.Model):
    user_id = models.IntegerField()
    shop_id = models.IntegerField()
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rate = models.IntegerField()
    download_count = models.IntegerField()
    is_submitted = models.CharField(max_length=1)
    tags = models.CharField(max_length=255)
    
    class Meta:
        db_table = "products"
