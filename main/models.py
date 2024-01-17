from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 55)
    number = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    joined = models.DateField(auto_now_add = True)
    location = models.CharField(max_length=100,default ='',blank= True,null =True)
    quote = models.TextField(max_length=250,default ='',blank= True,null =True,)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name} {self.number}'