from django.core.validators import RegexValidator
from django.db import models


class Member(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    account = models.CharField(null=False, max_length=12, validators=[alphanumeric])
    username = models.CharField(null=False, max_length=8)
    email = models.EmailField()
    is_staff = models.IntegerField()

    class Meta:
        db_table = "member"
