from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import uuid


class SpaUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """ Creates a user woth given password and a given email. """

        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """ Creates and saves a superuser with the given email and password. """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class SpaUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    objects = SpaUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

def jwt_get_secret_key(user_model):
    return user_model.jwt_secret