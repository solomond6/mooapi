from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, time, timedelta
from django.utils import timezone

from moove_apps.driver.models import Driver
# Create your models here.

class Permission(models.Model):
    """
    Roles permissions
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    """
    control panels user roles
    """

    name = models.CharField(max_length=100)
    permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_admin, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,is_admin=is_admin, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        return self._create_user(email, password, True, **extra_fields)

class User(AbstractBaseUser):
    '''
    Moove user profile
    '''

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    is_active = models.BooleanField(db_column='active', default=True)
    roles = models.ManyToManyField(Role) #control panel user could have many role
    is_admin = models.BooleanField(db_column='isadmin', null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    date_joined = models.DateTimeField(
        db_column='dt', blank=True, null=True, default=timezone.now)

    objects = UserManager()
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def is_staff(self):
        return self.is_admin

    def is_superuser(self):
        return self.is_admin

    def get_full_name(self):
    # The user is identified by their email address
        return self.email

    def get_short_name(self):
    # The user is identified by their email address
        return self.email
    
    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def has_perm(self, perm, object=None):
        # We only use Django Auth permissions within the admin site
        return self.is_active and self.is_admin

    def __str__(self):
        return self.email
    
class DriversTeamCaptain(models.Model):
    """
    Drivers team captains
    """

    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='team_captain')

    def __str__(self):
        return f'{self.driver.name}(Managed by {self.team_captain.name})'

