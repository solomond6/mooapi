from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django import forms
import logging
from moove_apps.driver.models import Driver, Plan, Vehicle, InfractionRecord, Infraction, \
    DriverGPA, Reconcilliation, UberPayment, NigerianBank, DriverBankAccount, DriverVehicleAssignment, \
    PosSystem, DriverDailyMetric, DriverPlanAssignment, VirtualAccount, USSDVehicleAssignment, \
    POSNotification, POSReversal, POSTerminal, VehicleDevice

from django.contrib.admin.models import LogEntry

logger = logging.getLogger(__name__)
# Register your models here p.
@admin.register(DriverGPA)
class DriverGPAAdmin(ImportExportModelAdmin):
    search_fields = (
       'driver__name', 'current_gpa',
    )

@admin.register(InfractionRecord)
class InfractionRecordAdmin(ImportExportModelAdmin):
    pass

class DriverVehicleAssignmentInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DriverVehicleAssignmentInlineForm, self).__init__(*args, **kwargs)
        free_vehicle_id = DriverVehicleAssignment.objects.filter(effective_end_date=None).values_list('vehicle_id', flat=True)
        free_vehicles = Vehicle.objects.exclude(pk__in=free_vehicle_id).values_list('id', flat=True)
        if self.instance.id:
            free_vehicles = list(free_vehicles)
            free_vehicles.append(self.instance.vehicle.id)
            logger.info(free_vehicles)
        queryset = Vehicle.objects.filter(Q(pk__in=free_vehicles) | Q(vehicle_assingment=None)).distinct()
        self.fields['vehicle'].queryset = queryset.order_by('registration_no')
class DriverVehicleAssignmentAdminInline(admin.StackedInline):
    model = DriverVehicleAssignment
    form = DriverVehicleAssignmentInlineForm
    extra = 0
    fields = ["vehicle", "effective_start_date", "effective_end_date"]

class DriverPlanAdminInline(admin.StackedInline):
    model = DriverPlanAssignment
    extra = 0
    fields = ["plan", "effective_start_date", "effective_end_date"]

class DriverInfractionInline(admin.StackedInline):
    model = InfractionRecord
    extra = 0
    fields = ['infractions', 'get_point', 'date']
    readonly_fields = ['get_point']

    def get_point(self, obj=None):
        if obj.pk:
            return obj.infractions.points
    get_point.short_description =  _("Infraction Points Deducted")
    get_point.allow_tags = True

class VehicleUSSDAccountInlineForm(forms.ModelForm):
    def clean(self):
        ussd_ref = self.cleaned_data.get('ussd_ref')
        exist = USSDVehicleAssignment.objects.filter(effective_end_date=None, ussd_ref=ussd_ref).exclude(pk=self.instance.id).first()
        if exist and not self.instance.effective_end_date:
            raise forms.ValidationError(f'{ussd_ref} already exist and active in vehicle {exist.vehicle.registration_no}')
        
        return super(VehicleUSSDAccountInlineForm, self).clean()

class VehicleVirtualAccountInlineForm(forms.ModelForm):
    def clean(self):
        virtual_id = self.cleaned_data.get('virtual_id')
        exist = VirtualAccount.objects.filter(effective_end_date=None, virtual_id=virtual_id).exclude(pk=self.instance.id).first()

        if exist and not self.instance.effective_end_date:
            raise forms.ValidationError(f'{virtual_id} already exist and active in vehicle {exist.vehicle.registration_no}')
        
        return super(VehicleVirtualAccountInlineForm, self).clean()

class VehicleUSSDAccountInline(admin.StackedInline):
    model = USSDVehicleAssignment
    form = VehicleUSSDAccountInlineForm
    extra = 0
    field = ['ussd_ref', 'effective_start_date', 'effective_end_date']

class VehicleDeviceInline(admin.StackedInline):
    model = VehicleDevice
    extra = 0
    field = ['device_type', 'identity', 'model', 'brand']

class VehicleVirtualAccountInline(admin.StackedInline):
    model = VirtualAccount
    form = VehicleVirtualAccountInlineForm
    extra = 0
    field = ['virtual_id', 'effective_start_date', 'effective_end_date']

class DriverAdmin(admin.ModelAdmin):
    search_fields = (
       'name', 'email', 'phone', 'drn', 'uber_name'
    )

    inlines = [DriverPlanAdminInline, DriverInfractionInline, DriverVehicleAssignmentAdminInline]

class VehicleAdmin(admin.ModelAdmin):
    search_fields = (
       'registration_no', 'make', 'model', 'color', 'year', 'assignment_status',
    )

    list_filter = (
        'assignment_status',
    )

    inlines = [VehicleUSSDAccountInline, VehicleVirtualAccountInline, VehicleDeviceInline]

# @admin.register(DriverVehicleAssignment)
# class DriverVehicleAssignmentAdmin(admin.ModelAdmin):
#     search_fields = (
#        'driver__name', 'effective_start_date', 'effective_end_date', 'vehicle__moove_id'
#     )

# @admin.register(DriverPlanAssignment)
# class DriverPlanAssignmentAdmin(admin.ModelAdmin):
#     search_fields = (
#        'driver__name', 'effective_start_date', 'effective_end_date', 'plan__name'
#     )     

# @admin.register(DriverDailyMetric)
# class DriverDailyMetricAdmin(admin.ModelAdmin):
#     search_fields = (
#        'date', 'trips', 'fare', 'driver__name',
#     )

#     list_filter = (
#      'date',
#     )

admin.site.register(LogEntry)
admin.site.register(Plan)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Infraction)
admin.site.register(PosSystem)
admin.site.register(VehicleDevice)
