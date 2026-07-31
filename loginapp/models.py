from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Order(models.Model):

    product_name = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    customer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    address = models.TextField()

    payment_method = models.CharField(max_length=50)

    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
from django.db import models


class Cart(models.Model):
    session_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product_name

    def total_price(self):
        return self.price * self.quantity