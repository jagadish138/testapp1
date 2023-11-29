from django.db import models

# Create your models here.
class Companys(models.Model):
    comp_name = models.CharField(max_length=1)

    def __str__(self):
        return  self.comp_name


class Employees(models.Model):
    objects = None
    fullname = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    company = models.ForeignKey(Companys,on_delete=models.CASCADE)
