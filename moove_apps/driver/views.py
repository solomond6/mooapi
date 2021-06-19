import logging
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.conf import settings
from moove_apps.driver.models import Driver, Vehicle, USSDVehicleAssignment, VirtualAccount,\
    DriverVehicleAssignment, DriverPlanAssignment, Plan, DriverStatusAssignment, DriverScoreCard, \
    VehicleStatusAssignment, InfractionRecord
from moove_apps.driver.serializers import DriverSerializer, VehicleSerializer, VehicleDriverAssignmentSerializer, \
    DriverPlanAssignmentSerializer, PlanSerializer, DriverStatusAssignmentSerializer, DriverScoreCardSerializer, \
    VehicleStatusSerializer, InfractionRecordSerializer
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from django.forms import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

logger = logging.getLogger(__name__)
# Create your views here.

class DriverVirtualAccountView(APIView):

    def get(self, request):
        virtual_id = self.request.query_params.get('virtual_id')
        logger.info(virtual_id)
        queryset = VirtualAccount.objects.filter(virtual_id=virtual_id, effective_end_date__isnull=True).last()
        logger.info(queryset)
        if not virtual_id or not queryset:
            return Response(data={'message': 'Vehicle with this virtual Id not found'}, status=status.HTTP_404_NOT_FOUND)  
        queryset = queryset.vehicle.vehicle_assingment.filter(effective_end_date__isnull=True).last()
        if not queryset:
            return Response(data={'message': 'No driver assigned to vehicle'}, status=status.HTTP_404_NOT_FOUND)
        data = DriverSerializer(queryset.driver).data
        return Response(data)

class DriverGtbUssdAccountView(APIView):

    def get(self, request):
        virtual_id = self.request.query_params.get('virtual_id')
        logger.info(virtual_id)
        queryset = USSDVehicleAssignment.objects.filter(effective_end_date__isnull=True, ussd_ref=virtual_id).last()
        if not virtual_id or not queryset:
            return Response(data={'message': f'Vehicle with the ussd ref no. {virtual_id} do not exit'}, status=status.HTTP_404_NOT_FOUND)
        queryset = queryset.vehicle.vehicle_assingment.filter(effective_end_date__isnull=True).last()
        if not queryset:
            return Response(data={'message': f'This vehicle is not assigned to any drivers'}, status=status.HTTP_404_NOT_FOUND)
        data = DriverSerializer(queryset.driver).data
        return Response(data)
        
class DriverGtbAccountDetailView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def validate(self, data, key):
        if not data:
            raise ValidationError(f'{key} Not found')

    def post(self, request):
        vehicle_no = request.data.get('customer_ref')
        merchant_id = request.data.get('merchant_id')

        logger.info(request.user)
        
        self.validate(vehicle_no, 'customerRef')
        self.validate(merchant_id, 'merchantId')

        queryset = USSDVehicleAssignment.objects.filter(effective_end_date__isnull=True, ussd_ref=vehicle_no).last()
        if not queryset:
            return Response(data= {"ResponseCode":"01","ResponseMessage":"Does not exist"})
        reg_number = queryset.vehicle.registration_no
        queryset = queryset.vehicle.vehicle_assingment.filter(effective_end_date__isnull=True).last()
        
        data = {
            'customerName': 'driver not assigned',
            'displayMessage': f'Moove payment System for vehicle no. {reg_number}',
            'responseCode': '00'
        }
        if queryset:
            driver = queryset.driver
            data['customerName'] = driver.name
        return Response(data)

class AvailableDriversAPIlView(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        non_free_vehicle_id = DriverVehicleAssignment.objects.filter(effective_end_date=None).values_list('vehicle_id', flat=True)
        queryset = Vehicle.objects.exclude(pk__in=non_free_vehicle_id)
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        return Response(data=VehicleSerializer(queryset, many=True).data)

class DriverVehicleAssignmentModelView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = VehicleDriverAssignmentSerializer
    queryset = DriverVehicleAssignment.objects.all()

class DriverPlanAssignmentModelView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = DriverPlanAssignmentSerializer
    queryset = DriverPlanAssignment.objects.all()

class DriverStatusAssignmentModelView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = DriverStatusAssignmentSerializer
    queryset = DriverStatusAssignment.objects.all()

class PlanAPIlView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Plan.objects.all()
        return Response(data=PlanSerializer(queryset, many=True).data)

class DriverScoreCardModelView(viewsets.ModelViewSet):
    serializer_class = DriverScoreCardSerializer
    queryset = DriverScoreCard.objects.all()

class VehicleStatusModelView(viewsets.ModelViewSet):
    serializer_class = VehicleStatusSerializer
    queryset = VehicleStatusAssignment.objects.all()

class InfractionRecordModelView(viewsets.ModelViewSet):
    serializer_class = InfractionRecordSerializer
    queryset = InfractionRecord.objects.all()
