from django.db import models
class Reg(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    conf_password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    emailid=models.EmailField()
    mobileno=models.IntegerField()

