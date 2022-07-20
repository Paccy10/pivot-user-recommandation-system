from django.db import models


class User(models.Model):

    user_id = models.BigIntegerField(unique=True, null=False)
    screen_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "users"
