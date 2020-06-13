from django.db import models

# Create your models here.
class adminUsers(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.CharField(max_length=15,null=True)
    password = models.CharField(max_length=200,null=True)
    password1 = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name