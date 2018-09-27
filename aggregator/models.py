from django.db import models

# Create your models here.


class expense_table(models.Model):
    category = models.TextField()
    amount = models.FloatField()
    date = models.DateField()
