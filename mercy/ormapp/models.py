from django.db import models
from django.contrib import admin
class Book(models.Model):
   bookid=models.IntegerField(primary_key=True);
   bookname=models.CharField(max_length=30);
   authorname=models.CharField(max_length=20);
   bookprize=models.IntegerField();
   contemail=models.EmailField();
class BookAdmin(admin.ModelAdmin):
   list_display=("bookid","bookname","authorname","bookprize","contemail");