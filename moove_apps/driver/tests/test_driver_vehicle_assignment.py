from moove_apps.user.tests import LoggedInAPITestCase
from django.urls import reverse
from moove_apps.driver.factory import DriverVehicleAssignmentFactory
from moove_apps.driver.models import DriverVehicleAssignment

class DriverVehicleAssignmentTest(LoggedInAPITestCase):

    fixtures = [
        'user.json',
        'vehicle.json',
        'driver.json'
    ]

    def setUp(self):
        user = self.get_user()
        super(DriverVehicleAssignmentTest, self).setUp()
        self.url = reverse('driver:vehicle-assignment-list')
        self.post_data = {
            "driver": 1,
            "vehicle": 1,
            "effective_start_date": "2020-11-20"
        }


    def test_get_available_vehicle_returns_200(self):
        url = reverse('driver:available-vehicles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_driver_vehicle_assignment_create(self):
        response = self.client.post(self.url, data=self.post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['driver'], 1)
    
    def test_driver_vehicle_assignment_update(self):
        driver_vehicle_assignment = DriverVehicleAssignmentFactory()
        data = { 'effective_end_date': '2020-11-30', 'effective_start_date': driver_vehicle_assignment.effective_start_date}

        url = reverse('driver:vehicle-assignment-detail', kwargs={ 'pk': driver_vehicle_assignment.id})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['effective_end_date'], data['effective_end_date'])

    def test_previous_efective_end_date_automatically_populated_on_create(self):
        driver_vehicle_assignment = DriverVehicleAssignmentFactory()
        self.assertEqual(driver_vehicle_assignment.effective_end_date, None)
        
        data = self.post_data.copy()
        data['vehicle'] = 2
        response = self.client.post(self.url, data=data, format='json')
        previous = DriverVehicleAssignment.objects.get(pk=driver_vehicle_assignment.pk)

        self.assertEqual(previous.effective_end_date.strftime("%Y-%m-%d"), response.data['effective_start_date'])


