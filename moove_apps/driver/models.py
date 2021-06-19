from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField
import logging
logger = logging.getLogger(__name__)
# Create your models here.

class Plan(models.Model):
    """
    Drivers plan
    """

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    """
    Vehicle to be assigned to drivers
    """
    
    STATUS_CHOICES = (
       ('Assigned', 'Assigned'),
        ('Not Assigned', 'Not Assigned')
    )# Confirm what the statuses are
    moove_id = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    vin = models.CharField(max_length=100, blank=True, null=True)
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year =  models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    assignment_status = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)


    def __str__(self):
        return self.registration_no

class USSDVehicleAssignment(models.Model):
    vehicle = models.ForeignKey(
    Vehicle, related_name='vehicle_ussd_ref', on_delete=models.CASCADE)
    ussd_ref = models.CharField(max_length=50, blank=True, null=True)
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ussd_ref

class VehicleDevice(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='vehicles', on_delete=models.CASCADE)
    device_type = models.CharField(max_length=100)
    identity =  models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.identity

class Driver(models.Model):
    """
    Drivers
    """

    APPROVAL_CHOICES = (
        ('Approved', 'Approved'),
        ('In Progress', 'In Progress')
    )# Confirm what the statuses are

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    ACTIVE_STATUS = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
        ('Sick/Leave', 'Sick/Leave'),
        ('Resigned', 'Resigned')
    )

    UBER_STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Waitlisted', 'Waitlisted')
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=45, blank=True, null=True)
    drn = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    uber_id = models.CharField(max_length=100, blank=True, null=True) #confirm if it will be an integer
    uber_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    approval_status = models.CharField(max_length=100, choices=APPROVAL_CHOICES, default='In Progress')
    uber_status = models.CharField(max_length=100, choices=UBER_STATUS, default='Active')
    created_date = models.DateField(blank=True, null=True)
    updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class DriverPlanAssignment(models.Model):
    plan = models.ForeignKey(Plan, related_name='plans', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='drivers', on_delete=models.CASCADE)
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.driver.name

class Infraction(models.Model): #Add infractions as a fixture
    """
    Drivers infractions or rules of penalty for misconduct
    """

    STATUS_CHOICES = (
        ('Level one', 'one'),
        ('Level two', 'two'),
         ('Level three', 'three')
    )
    name = models.CharField(max_length=100)
    description =  models.CharField(max_length=255)
    level = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)
    points = models.DecimalField(max_digits=50, decimal_places=5, default=0)

    def __str__(self):
        return f'{self.name}-{self.points}'

class InfractionRecord(models.Model):
    """
    Drivers who has committed one or more of the infractions
    """

    driver = models.ForeignKey(Driver, related_name='infractions', on_delete=models.CASCADE)
    infractions = models.ForeignKey(Infraction, related_name='infractionRecords', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.infractions.level


class DriverGPA(models.Model):
    """
    Current drivers ratings
    """

    driver = models.ForeignKey(Driver, related_name='gpa', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    current_gpa = models.DecimalField(max_digits=50, decimal_places=8, default=5)
    total_deduction = models.DecimalField(max_digits=50, decimal_places=8, default=0)

    def __str__(self):
        return f'{self.driver.name}-{self.current_gpa}'

class UberPayment(models.Model):
    """
    Drivers uber payments
    """
    driver = models.ForeignKey(Driver, related_name='uber_payments', blank=True, null=True, on_delete=models.CASCADE)
    trip_time = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    date_extract = models.DateField(blank=True, null=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    driver_uuid = models.CharField(max_length=255, blank=True, null=True)
    trip_uuid = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    disclaimer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

class Reconcilliation(models.Model):
    """
    drivers reconcilliation
    """

    driver = models.ForeignKey(Driver, related_name='reconcilliations', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    week_of = models.DateField(blank=True, null=True)
    earning = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    cash_collected =  models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    pos_receipt_url = models.CharField(max_length=50)# Will this be uploaded to external service?
    amount_owed = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    balance_brought = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.earning

class NigerianBank(models.Model):
    """
    Nigerian Bank
    """

    STATUS_CHOICES = (
        ('Commercial Bank', 'Commercial Bank'),
        ('Others', 'Others')
    )
    bank_name = models.CharField(max_length=100)
    institution_type = models.CharField(max_length=100, choices=STATUS_CHOICES, null=True)
    head_office_routing_code = models.CharField(max_length=100)
    swift_bic_address =  models.CharField(max_length=100)
    bank_identifier = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    area = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.bank_name

class DriverBankAccount(models.Model):
    """
    Driver Nigerian Bank
    """

    driver = models.ForeignKey(Driver, related_name='accounts', on_delete=models.CASCADE)
    bank_name = models.ForeignKey(NigerianBank, related_name='banks', on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.account_name

class VehicleStatusAssignment(models.Model):
    """
    Assign drivers to vehicles
    """
    VEHICLE_STATUS = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
        ('Accident', 'Accident'),
        ('In Repair', 'In Repair')
    )

    vehicle = models.ForeignKey(
        Vehicle, related_name='status_assingment', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=VEHICLE_STATUS, default='Active')
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.driver.name}-{self.vehicle.moove_id}'

class DriverVehicleAssignment(models.Model):
    """
    Assign drivers to vehicles
    """

    driver = models.ForeignKey(
        Driver, related_name='driver_assingment', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(
        Vehicle, related_name='vehicle_assingment', on_delete=models.CASCADE)
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.driver.name}-{self.vehicle.moove_id}'

class DriverStatusAssignment(models.Model):
    """
    Assign drivers to status
    """

    driver = models.ForeignKey(
        Driver, related_name='driver_status', on_delete=models.CASCADE)

    status = models.CharField(max_length=100, choices=Driver.ACTIVE_STATUS, default='Inactive')
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.driver.name}-{self.vehicle.moove_id}'

class VirtualAccount(models.Model):
    """
    VirtualAccount
    """
    vehicle = models.ForeignKey(
        Vehicle, related_name='vehicle_virtual_account', null=True, blank=True, on_delete=models.CASCADE)
    virtual_id = models.CharField(max_length=100)
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.vehicle.registration_no}-{self.virtual_id}'

class DriverDailyMetric(models.Model):
    """
    Driver metrics
    """

    driver = models.ForeignKey(
        Driver, related_name='metrics', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    total_earned = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    net_earnings = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    trips = models.IntegerField(null=True, blank=True)
    fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    wait_time = models.IntegerField(null=True, blank=True)
    toll = models.IntegerField(null=True, blank=True)
    uber_fee = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    cash_collected = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    tips = models.CharField(max_length=100, null=True, blank=True)
    cancellation = models.IntegerField(null=True, blank=True)
    adjusted_fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    surge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    airport_surcharge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    cash_payment_count = models.IntegerField(null=True, blank=True)
    card_payment_count = models.IntegerField(null=True, blank=True)
    duration_online = models.TimeField(null=True, blank=True)
    rating = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    acceptance_rate = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    cancellation_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.date

class PosSystem(models.Model):
    """
    PosSystem
    """

    pos_terminal_id = models.CharField(max_length=100)
    vehicle = models.OneToOneField(Vehicle, related_name='pos', on_delete=models.CASCADE)
    effective_start_date = models.DateField(default=timezone.now)
    effective_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.pos_terminal_id

class POSNotification(models.Model):
    terminal_id = models.ForeignKey(PosSystem, on_delete=models.CASCADE)
    transaction_reference = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    retrieval_ref_no = models.CharField(max_length=255, blank=True, null=True)
    masked_pan = models.CharField(max_length=255, blank=True, null=True)
    card_scheme = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    status_code = models.CharField(max_length=255, blank=True, null=True)
    status_desc = models.CharField(max_length=255, blank=True, null=True)
    addnl_info = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    stan = models.CharField(max_length=255, blank=True, null=True)
    card_expiry = models.CharField(max_length=255, blank=True, null=True)
    card_hash = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_reference

class POSReversal(models.Model):
    terminal_id = models.ForeignKey(PosSystem, on_delete=models.CASCADE)
    transaction_reference = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    retrieval_ref_no = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    stan = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_reference


class POSTerminal(models.Model):
    terminal_id = models.ForeignKey(PosSystem, on_delete=models.CASCADE)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.serial_no

class UberDriverPerformance(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    net_fares = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_hour_online = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_km_on_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    trips = models.IntegerField(null=True, blank=True)
    hours_online = models.TimeField(null=True, blank=True)
    trips_per_hour = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    distance_per_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    rating = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    lifetime_rating = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    acceptance = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    driver_cancellation_rate = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class DriverScoreCard(models.Model):
    CONTACT_CHOICES = (
        ('offline_driver', 'Offline Driver(Outbound)'),
        ('kpi_check', 'KPIs Check(Outbound)'),
        ('inbound', 'Inbound')
    )

    ATTENTION_CHOICE = (
        ('Yes', "Yes"),
         ('No', "No")
    )
    driver = models.ForeignKey(
        Driver, related_name='driver_score_card', on_delete=models.CASCADE, blank=True, null=True)
    conctact_type = models.CharField(max_length=100, choices=CONTACT_CHOICES)
    team_captain = models.CharField(max_length=100, blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    reason_offline = models.JSONField(default=list)
    immediate_attention = models.CharField(max_length=100, choices=ATTENTION_CHOICE, blank=True, null=True)
    kpi_not_met = models.JSONField(default=list)
    reason_target_not_met = models.JSONField(default=list)
    comment = models.TextField(blank=True, null=True)
    

class UberAllDriver(models.Model):
    driver = models.ForeignKey(
        Driver, related_name='uber_all_drivers', on_delete=models.CASCADE, blank=True, null=True)
    bank_deposit = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_driver_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    trips = models.IntegerField(null=True, blank=True)
    fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    wait_time = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    toll = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    surge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    collection = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    payouts = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    other_promotion = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    tip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    airport_charge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee_collection = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    adjusted_fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee_collection_return = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name

class DriverMetric(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    driver_earnings = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    cash_collected = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    promotion = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    tip = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    total_trip_count = models.IntegerField(null=True, blank=True)
    cash_trip_count = models.IntegerField(null=True, blank=True)
    uber_fee_collection = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    per_trip = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    per_hour_online = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    per_km_on_trip = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    trips_per_hour = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    distance_per_trip = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    rating = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    lifetime_rating = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    acceptance = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    driver_cancellation_rate = models.DecimalField(max_digits=50, decimal_places=8, blank=True, null=True)
    hours_online = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.fullname

class UberReconciliaition(models.Model):
    bank_deposit = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_driver_id = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    trips = models.IntegerField(null=True, blank=True)
    fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    wait_time = models.IntegerField(null=True, blank=True)
    toll = models.IntegerField(null=True, blank=True)
    surge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    collection = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    payouts = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    other_promotion = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    tip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    airport_charge = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee_collection = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    adjusted_fare = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    uber_fee_collection_return = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    performance_date = models.DateField(null=True, blank=True)
    driver_id = models.IntegerField(null=True, blank=True)
    all_driver_name = models.CharField(max_length=255, blank=True, null=True)
    performance_name = models.CharField(max_length=255, blank=True, null=True)
    all_drivers_date = models.DateField(null=True, blank=True)
    net_fares = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_hour_online = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    per_km_on_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    trips_y = models.IntegerField(null=True, blank=True)
    hours_online = models.TimeField(null=True, blank=True)
    trips_per_hour = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    distance_per_trip = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    rating = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    lifetime_rating = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    acceptance = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    driver_cancellation_rate = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    master_uber_id = models.CharField(max_length=255, blank=True, null=True)
    payments_date = models.DateField(null=True, blank=True)
    cash_transactions = models.IntegerField(null=True, blank=True)
    cash_amount = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    pos_terminal_id = models.CharField(max_length=255, blank=True, null=True)
    pos_transaction_date = models.DateField(null=True, blank=True)
    pos_transaction_count = models.IntegerField(null=True, blank=True)
    agg_pos_amount = models.DecimalField(max_digits=50, decimal_places=8, null=True, blank=True)
    master_drn = models.CharField(max_length=255, blank=True, null=True)
    driver_name = models.CharField(max_length=255, blank=True, null=True)
    driver_email = models.CharField(max_length=255, blank=True, null=True)
    driver_phone_number = models.CharField(max_length=255, blank=True, null=True)
    reconciliation_date = models.DateField(null=True, blank=True)
    reconciliaition_instance = models.IntegerField(null=True, blank=True)
    master_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bank_deposit

class UberCredential(models.Model):
    drn = models.CharField(max_length=255, null=True, blank=True)
    driver_id = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    picture = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=50, decimal_places=2, default=0, null=True, blank=True)
    activation_status = models.CharField(max_length=255, null=True, blank=True)
    access_token = models.TextField(null=True, blank=True)
    token_type = models.CharField(max_length=255, null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    refresh_token = models.TextField(null=True, blank=True)
    scope = models.CharField(max_length=255, null=True, blank=True)
    auth_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

@receiver(pre_save, sender=VirtualAccount, dispatch_uid="add virtual account")
def add_virtual_account_assignment(sender, instance, **kwargs):
    if not instance.pk:
       instance.vehicle.vehicle_virtual_account.filter(effective_end_date=None).update(effective_end_date=datetime.now())

@receiver(pre_save, sender=USSDVehicleAssignment, dispatch_uid="add driver assignment")
def add_ussd_assignment(sender, instance, **kwargs):
    if not instance.pk:
        instance.vehicle.vehicle_ussd_ref.filter(effective_end_date=None).update(effective_end_date=datetime.now())

@receiver(pre_save, sender=DriverPlanAssignment, dispatch_uid="add plan assignment")
def add_plan_assignment(sender, instance, **kwargs):
    if not instance.pk:
       instance.driver.drivers.filter(effective_end_date=None).update(effective_end_date=instance.effective_start_date)

@receiver(pre_save, sender=DriverStatusAssignment, dispatch_uid="status assignment")
def add_status_assignment(sender, instance, **kwargs):
    if not instance.pk:
       instance.driver.driver_status.filter(effective_end_date=None).update(effective_end_date=instance.effective_start_date)

@receiver(pre_save, sender=DriverVehicleAssignment, dispatch_uid="add driver assignment")
def add_driver_assignment(sender, instance, **kwargs):
    if not instance.pk:
        instance.driver.driver_assingment.filter(effective_end_date=None).update(effective_end_date=instance.effective_start_date)

@receiver(pre_save, sender=InfractionRecord, dispatch_uid="update_driver_gpa")
def create_or_update_driver_gpa(sender, instance, **kwargs):
    current_driver_gpa = DriverGPA.objects.filter(driver=instance.driver).first()
    if current_driver_gpa:
        point = instance.infractions.points
        if instance.pk:
            #update infractions
            initial_instance = InfractionRecord.objects.get(pk=instance.pk)
            point -= initial_instance.infractions.points
        current_driver_gpa.current_gpa -= point
        current_driver_gpa.total_deduction += point
        current_driver_gpa.save()
    else:
        # Assumes 5 is the max point
        current_gpa = 5 - instance.infractions.points
        DriverGPA.objects.create(driver=instance.driver, date=datetime.now(), current_gpa=current_gpa, total_deduction=instance.infractions.points)

@receiver(post_delete, sender=InfractionRecord)
def deduct_driver_gpa(sender, instance, *args, **kwargs):
    """ deduct driver gpa when record is deleted """
    current_driver_gpa = DriverGPA.objects.filter(driver=instance.driver).first()
    current_driver_gpa.current_gpa += instance.infractions.points
    current_driver_gpa.total_deduction -= instance.infractions.points
    current_driver_gpa.save()
