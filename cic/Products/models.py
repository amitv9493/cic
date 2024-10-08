from django.conf import settings
from django.db import models

from cic.Master.models import ProductCategory


class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_status = models.BooleanField(default=True)
    Product_Serial_No = models.CharField(max_length=100)

    Product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    Product_image = models.ImageField(upload_to="products/")

    Product_Specification = models.TextField()
    Product_description = models.CharField(max_length=100)

    Product_Assigned_User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    Product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
