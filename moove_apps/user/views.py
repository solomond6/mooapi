from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HealthCheckView(ViewSet):
    """ Health check """
    def get(self, request):
        return Response(status=HTTP_200_OK)
