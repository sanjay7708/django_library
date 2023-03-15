from django.db import models
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
class Register(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mail=models.CharField(max_length=30)
    phno=models.BigIntegerField(max_length=10)
class Book(models.Model):
    bookname=models.CharField(max_length=100)
    bookauthor=models.CharField(max_length=50)
    book_isbn=models.CharField(max_length=20)
    publish_date=models.CharField(max_length=20)
    book_country=models.CharField(max_length=30)