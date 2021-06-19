from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime, time, timedelta
from django.utils import timezone


class UserGroupings(models.Model):
    group = models.ForeignKey('UserGroups', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user_groupings'


class UserGroups(models.Model):
    name = models.CharField(max_length=105, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserPermissions(models.Model):
    name = models.CharField(max_length=105, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    parent_permission_id = models.IntegerField(blank=True, null=True)
    controller = models.CharField(max_length=105, blank=True, null=True)
    method = models.CharField(max_length=105, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user_permissions'


class UserRolePermissions(models.Model):
    permission = models.ForeignKey(UserPermissions, models.DO_NOTHING)
    role = models.ForeignKey('UserRoles', models.DO_NOTHING)
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user_role_permissions'


class UserRoles(models.Model):
    name = models.CharField(max_length=105, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    parent_role_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    first_name = models.CharField(max_length=105, blank=True, null=True)
    last_name = models.CharField(max_length=105, blank=True, null=True)
    email = models.CharField(max_length=105, blank=True, null=True)
    phone_number = models.CharField(max_length=105, blank=True, null=True)
    role = models.ForeignKey(UserRoles, models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=105, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified_by = models.CharField(max_length=105, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
