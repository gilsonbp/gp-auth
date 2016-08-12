from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.db import models
from django.utils import timezone

__author__ = "Gilson Paulino"
__copyright__ = "Copyright 2016"
__email__ = "gilsonbp@gmail.com"


class UserManager(BaseUserManager):
    def create_user(self, login, name, password=None):
        if not login:
            raise ValueError('Users must have a login.')

        user = self.model(
            login=login,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, name, password):
        user = self.create_user(
            login=login,
            name=name,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=50, verbose_name='Login', unique=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.CharField(max_length=200, verbose_name='E-mail', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Is active?',
                                    help_text='Only active users can access the system.')
    is_staff = models.BooleanField(default=False, verbose_name='Member of the team?',
                                   help_text='Determines whether the user can access the administrator environment.')

    date_joined = models.DateTimeField('Registration date', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'login'

    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return '%s' % self.name

    get_full_name.short_description = 'Complete Name'

    def get_short_name(self):
        return self.name

    get_short_name.short_description = 'Name'

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
