from django.db import models

from authapp.models import LocalUser


class Profession(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    user = models.ForeignKey(LocalUser,on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Course(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField( blank=True, null=True)
    end_date = models.DateTimeField( blank=True, null=True)
    level = models.DateTimeField( blank=True, null=True)
    file_certificate = models.FileField(upload_to='Course_certificates', blank=True)
    url_certificate = models.CharField(max_length=255, blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(default=0,blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    profession = models.ForeignKey(Profession,on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

class Comment(models.Model):
    text = models.CharField(max_length=128, blank=True, null=True)
    task = models.ForeignKey(Task,on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)