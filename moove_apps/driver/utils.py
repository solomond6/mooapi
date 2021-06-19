from datetime import datetime
from rest_framework import serializers

def check_effective_date(validated_data):
    start_date = validated_data.get('effective_start_date')
    end_date = validated_data.get('effective_end_date')
    if (start_date > datetime.date(datetime.now())) or (end_date and end_date > datetime.date(datetime.now())):
        raise serializers.ValidationError('Start date and/or end date cannot be greater than today date')
    if end_date and start_date > end_date:
        raise serializers.ValidationError('Start date cannot be greater than end date')
