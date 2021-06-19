from rest_framework import serializers

from .models import Users, UserRoles, UserPermissions, UserRolePermissions, UserGroups, UserGroupings

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'


class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermissions
        fields = '__all__'


class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = '__all__'


class UserGroupingsSerializer(serializers.ModelSerializer):
    # group = UserGroupsSerializer()
    # user = UsersSerializer()
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )

    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = UserGroupings
        # fields = ('id', 'group', 'user')
        fields = '__all__'