from django.db import models

# Create your models here.

class paper(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=5,null=True,blank=True)
    id_no = models.CharField(max_length=5,null=True,blank=True)
    pattern = models.CharField(max_length=100,null=True,blank=True)
    level = models.CharField(max_length=5,null=True,blank=True)
    language = models.CharField(max_length=100,null=True,blank=True)
    testtype = models.CharField(max_length=100,null=True,blank=True)
    testdate = models.CharField(max_length=100,null=True,blank=True)
    papertype = models.CharField(max_length = 50,null=True,blank=True)
    remarks = models.CharField(max_length = 250,null=True,blank=True)
    is_test_added = models.BooleanField(default=False)
    is_solution_added = models.BooleanField(default=False)
    question_path = models.CharField(max_length = 250,null=True,blank=True)
    solution_path = models.CharField(max_length = 250,null=True,blank=True)
    question_extracted = models.BooleanField(default=False)
