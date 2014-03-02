from django.db import models

class Person(models.Model):
    id = models.BigIntegerField(primary_key=True)
    regist_time = models.DateTimeField(blank=True, null=True)
    active_time = models.DateTimeField(blank=True, null=True)
    active_state = models.NullBooleanField()
    email = models.CharField(unique=True, max_length=64)
    old_email = models.CharField(max_length=64, blank=True)
    password = models.CharField(max_length=32, blank=True)
    province = models.SmallIntegerField(blank=True, null=True)
    city = models.SmallIntegerField(blank=True, null=True)
    sex = models.NullBooleanField()
    phone = models.CharField(max_length=16, blank=True)
    idcard = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = 'person'

class Company(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    dept = models.TextField(blank=True) # This field type is a guess.
    brief = models.TextField(blank=True)
    class Meta:
        db_table = 'company'
