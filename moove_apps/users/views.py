# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from .models import Users, UserRoles, UserRolePermissions, UserPermissions, UserGroups, UserGroupings
from .serializers import UsersSerializer, UserRolesSerializer, UserPermissionsSerializer, UserGroupingsSerializer, UserGroupsSerializer
from django.conf.urls import url

class UsersList(APIView):
    def get(self, request):
        users = Users.objects.all()[:20]
        data = UsersSerializer(users, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UsersSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserRolesList(APIView):
    def get(self, request):
        userroles = UserRoles.objects.all()[:20]
        data = UserRolesSerializer(userroles, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserRolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserRolesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPermissionsList(APIView):
    def get(self, request):
        userpermissions = UserPermissions.objects.all()[:20]
        data = UserPermissionsSerializer(userpermissions, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserPermissionsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGroupsList(APIView):
    def get(self, request):
        usergroups = UserGroups.objects.all()[:20]
        data = UserGroupsSerializer(usergroups, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserGroupsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGroupingsList(APIView):
    def get(self, request):
        usergroupings = UserGroupings.objects.all()[:20]
        data = UserGroupingsSerializer(usergroupings, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserGroupingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserGroupingsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(Users, pk=pk)
        data = UsersSerializer(user).data
        return Response(data)


class UserGroupMembersDetail(APIView):
    def get(self, request, pk):
        users = get_object_or_404(UserGroupings, group=pk)
        data = UserGroupingsSerializer(users).data
        return Response(data)

def users_list(request):
    MAX_OBJECTS = 20
    users = Users.objects.all()[:MAX_OBJECTS]
    data = {"results": list(users.values("first_name"))}
    return JsonResponse(data)


def users_detail(request, pk):
    user = get_object_or_404(Users, pk=pk)
    data = {"results": {
        "first_name": user.first_name,
        "last_name": user.last_name
    }}
    return JsonResponse(data)
