from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Registration.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Registration.objects.filter(email=self.email):
            return True

        return False
    
    def __str__(self):
        return self.first_name


class Category(models.Model):
    cat_image = models.ImageField(upload_to="uploads/category/")
    cat_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_image = models.ImageField(upload_to="uploads/products/")
    product_price = models.IntegerField()
    product_desc = models.CharField(max_length=200, blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    address = models.CharField(max_length=300, null=True, blank=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    customer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name
