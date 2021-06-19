# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Users, UserRoles, UserPermissions, UserRolePermissions, UserGroups, UserGroupings

admin.site.register(Users)
admin.site.register(UserRoles)
admin.site.register(UserPermissions)
admin.site.register(UserRolePermissions)
admin.site.register(UserGroups)
admin.site.register(UserGroupings)
