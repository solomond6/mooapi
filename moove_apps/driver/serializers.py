import logging
from datetime import datetime
from django.db.models import Q
from rest_framework import serializers
from moove_apps.driver.models import Driver, Vehicle, DriverVehicleAssignment, DriverPlanAssignment, Plan, \
    DriverStatusAssignment, DriverScoreCard, VehicleStatusAssignment, InfractionRecord
from moove_apps.driver.utils import check_effective_date
logger = logging.getLogger(__name__)

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleDriverAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverVehicleAssignment
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Checks coherence of input data.
        '''
        try:
            logger.info(validated_data)
            vehicle = validated_data.get('vehicle')
            driver = validated_data.get('driver')
            vehicle_exist = vehicle.vehicle_assingment.filter(effective_end_date=None).last()
            if vehicle_exist:
                message = f'Vehicle with drn {vehicle.registration_no} already assigned to driver {vehicle_exist.driver.drn}'
                raise serializers.ValidationError(message)
            check_effective_date(validated_data)
        except Exception as ex:
            raise ex
        return super(VehicleDriverAssignmentSerializer, self).create(validated_data)
     
    def update(self, instance, validated_data):
        """
        new update
        """
        check_effective_date(validated_data)
        return super(VehicleDriverAssignmentSerializer, self).update(instance,
                                                    validated_data)

class DriverPlanAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPlanAssignment
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Checks coherence of input data.
        '''
        check_effective_date(validated_data)
        return super(DriverPlanAssignmentSerializer, self).create(validated_data)
     
    def update(self, instance, validated_data):
        """
        new update
        """
        check_effective_date(validated_data)
        return super(DriverPlanAssignmentSerializer, self).update(instance,
                                                    validated_data)

class DriverStatusAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverStatusAssignment
        fields = '__all__'
    
    def create(self, validated_data):
        '''
        Checks coherence of input data.
        '''
        check_effective_date(validated_data)
        return super(DriverStatusAssignmentSerializer, self).create(validated_data)
     
    def update(self, instance, validated_data):
        """
        new update
        """
        check_effective_date(validated_data)
        return super(DriverStatusAssignmentSerializer, self).update(instance,
                                                    validated_data)
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class DriverScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverScoreCard
        fields = '__all__'

class VehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStatusAssignment
        fields = '__all__'

    def create(self, validated_data):
        '''
        Checks coherence of input data.
        '''
        check_effective_date(validated_data)
        return super(VehicleStatusSerializer, self).create(validated_data)
     
    def update(self, instance, validated_data):
        """
        new update
        """
        check_effective_date(validated_data)
        return super(VehicleStatusSerializer, self).update(instance,
                                                    validated_data)
                                        
class InfractionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfractionRecord
        fields = '__all__'
