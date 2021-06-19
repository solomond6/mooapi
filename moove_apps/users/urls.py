from django.conf.urls import url
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Moove API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

app_name = 'users'

urlpatterns = [
    # url(r'^users/$', views.users_list, name='users_list'),
    # url("users/(\d+)/$", views.users_detail, name="users_detail")
    url(r'^users/$',  views.UsersList.as_view(), name='users_list'),
    url("users/(\d+)/$", views.UserDetail.as_view(), name="users_detail"),
    url(r'^userroles/$',  views.UserRolesList.as_view(), name='user_roles'),
    url(r'^userpermissions/$',  views.UserPermissionsList.as_view(), name='user_permissions'),
    url(r'^usergroups/$',  views.UserGroupsList.as_view(), name='user_groups'),
    url(r'^usergroupings/$',  views.UserGroupingsList.as_view(), name='user_groups'),
    url("groupmembers/(\d+)/$", views.UserGroupMembersDetail.as_view(), name="groupmembers"),
    url(r'^api/docs/', schema_view, name='api-doc')
]