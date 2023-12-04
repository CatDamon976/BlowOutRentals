
from django.db import models
from django.core.validators import MinLengthValidator

class States(models.Model):
    abbrev = models.CharField(max_length=2, primary_key=True)
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return self.state_name


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.OneToOneField(States, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=9, validators=[MinLengthValidator(5)])
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Orders(models.Model):
    description = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CustomerOrders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order ID: {self.order.id}, Customer: {self.customer.last_name}, {self.customer.first_name}"

