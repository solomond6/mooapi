from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from moove_apps.driver.models import Vehicle, VirtualAccount, USSDVehicleAssignment

class Command(BaseCommand):
    help = 'Virtual account and ussd assignment'

    def handle(self, *args, **options):
        vehicles = Vehicle.objects.all()
        code = 100000
        print(f'Found {vehicles.count()} vehicles')
        for vehicle in vehicles:
            VirtualAccount.objects.create(vehicle=vehicle, virtual_id=f'9900{code}')
            USSDVehicleAssignment.objects.create(vehicle=vehicle, ussd_ref=f'{code}')
            code += 1
            print(f'virtual id added for vehicle {vehicle.registration_no}')
