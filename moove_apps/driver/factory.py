import factory
from moove_apps.driver.models import Driver, Vehicle, DriverVehicleAssignment, DriverStatusAssignment, \
    DriverScoreCard, VehicleStatusAssignment

class DriverFactory(factory.DjangoModelFactory):
    class Meta:
        model = Driver

    name = factory.Sequence(lambda n: 'Driver %s' % n)
    email = factory.Sequence(lambda n: 'Driver@email.co%s' % n)

class VehicleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vehicle

    moove_id = factory.Sequence(lambda n: 'moove %s' % n)
    registration_no = factory.Sequence(lambda n: '324w %s' % n)

class DriverVehicleAssignmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = DriverVehicleAssignment

    vehicle = VehicleFactory()
    driver = DriverFactory()
    effective_start_date = '2020-11-30'

class DriverStatusAssignmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = DriverStatusAssignment

    status = "Active"
    driver = DriverFactory()
    effective_start_date = '2020-11-30'

class DriverScoreCardFactory(factory.DjangoModelFactory):
    class Meta:
        model = DriverScoreCard

    conctact_type = "offline_driver"
    driver = DriverFactory()

class VehicleStatusAssignmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = VehicleStatusAssignment

    status = "Active"
    vehicle = VehicleFactory()
    effective_start_date = '2020-11-30'
