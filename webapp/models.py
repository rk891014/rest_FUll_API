from django.db import models
from s3direct.fields import S3DirectField
class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    image = models.ImageField(upload_to="pictures", blank=True, null=True)

    def __str__(self):
        return self.firstname
