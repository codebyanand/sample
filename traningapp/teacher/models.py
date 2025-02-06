from django.db import models

# Create your models here.
from django.db import models


class TeachersReg(models.Model):
    idteachers_reg = models.AutoField(db_column='idteachers reg', primary_key=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=45)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='Phonenumber', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers_reg'

