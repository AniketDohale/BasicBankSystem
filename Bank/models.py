from django.db import models

# Create your models here.


class Customers(models.Model):
    cust_id = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    cust_email = models.EmailField()
    cust_phone = models.IntegerField()
    cust_amount = models.IntegerField()

    def __str__(self):
        return self.first_name


class Transfer(models.Model):
    from_cust = models.CharField(max_length=120)
    to_cust = models.CharField(max_length=120)
    cust_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.from_cust
