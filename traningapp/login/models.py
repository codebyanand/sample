from django.db import models

# Create your models here.
from django.db import models


class LoginInfo(models.Model):
    login_number = models.AutoField(db_column='login number', primary_key=True)  # Field renamed to remove unsuitable characters.
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login_info'
