from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.


class JUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        :param email:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        :param self:
        :param email:
        :param password:
        :return:
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class JUser(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField(
        verbose_name='email_address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = JUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The User is identified by their email address
        return self.email

    def get_short_name(self):
        # The User is identified by their email address
        return self.email

    def __str__(self):
        return self.email
    #
    #
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     super()

    @property
    def is_staff(self):
        """Is the user a member of the staff?"""
        # All admins are staff.
        return self.is_admin
