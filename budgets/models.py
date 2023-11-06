from django.db import models
from django.conf import settings

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='budgets'
    )
    name = models.CharField(max_length=100, default=f"{user.name}'s Budget")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Income(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    net_amount = models.IntegerField(default=0)
    frequency = [
        ('bw', 'Biweekly'),
        ('mo', 'Monthly'),
        ('we', 'Weekly'),
        ('sm', 'Semimonthly'),
    ]
    start_date = models.DateField()

class AdditionalIncome(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    net_amount = models.FloatField(default=0)
    date = models.DateField()

class RecurringExpense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    frequency = [
        ('mo', 'Monthly'),
        ('we', 'Weekly'),
        ('bw', 'Biweekly'),
    ]
    amount = models.FloatField(default=0)
    start_date = models.DateField()

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    date = models.DateField()

