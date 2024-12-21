from django.db import models

class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=100)
    deptloc=models.CharField(max_length=100)

class Employee(models.Model):
    emp_ID=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_job=models.CharField(max_length=100)
    emp_mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    emp_hiredate=models.DateField()
    emp_sal=models.DecimalField(max_digits=100,decimal_places=3)
    emp_comm=models.DecimalField(max_digits=10,decimal_places=3,null=True,blank=True)
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)

# Create your models here.

