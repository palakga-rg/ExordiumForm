from django.db import models


class Member(models.Model):
    Fname1=models.CharField(max_length=50)
    Fname2=models.CharField(max_length=50)
    Lname1=models.CharField(max_length=50)
    Lname2=models.CharField(max_length=50)
    Roll1=models.IntegerField(max_length=12)
    Roll2=models.IntegerField(max_length=12)
    Phone1=models.IntegerField(max_length=10)
    Phone2=models.IntegerField(max_length=10)
    Email1=models.EmailField(max_length=70)
    Email2=models.EmailField(max_length=70)
    Q1=models.CharField(max_length=300)
    Q2=models.CharField(max_length=300)
    

    def __str__(self):
        return self.Fname1 + ' '+self.Fname2