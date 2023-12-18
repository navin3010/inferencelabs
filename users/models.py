from django.db import models
from django.contrib import auth

User = auth.get_user_model()

# class UserProfileDetails(models.Model):
#     # user = models.OneToOneField(
#     #     User, on_delete=models.CASCADE,
#     # )
#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255)
#     email = models.CharField(max_length = 255)
#     password = models.CharField(max_length = 255)


