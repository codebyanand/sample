# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StudentInfo(models.Model):
    id_no = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_info'

class LoginInfo(models.Model):
    login_number = models.AutoField(db_column='login number', primary_key=True)  # Field renamed to remove unsuitable characters.
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login_info'

