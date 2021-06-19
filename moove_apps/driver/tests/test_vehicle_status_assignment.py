from moove_apps.user.tests import LoggedInAPITestCase
from django.urls import reverse
from moove_apps.driver.factory import VehicleStatusAssignmentFactory
from moove_apps.driver.models import VehicleStatusAssignment

class VehicleStatusTest(LoggedInAPITestCase):

    fixtures = [
        'user.json',
        'vehicle.json',
        'driver.json'
    ]

    def setUp(self):
        user = self.get_user()
        super(VehicleStatusTest, self).setUp()
        self.url = reverse('driver:vehicle-status-assignment-list')
        self.post_data = {
            "vehicle": 1,
            "status": "Active",
            "effective_start_date": "2020-11-20"
        }
    
    def test_vehicle_assignment_create(self):
        response = self.client.post(self.url, data=self.post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['vehicle'], 1)

    def test_vehicle_assignment_update(self):
        vehicle_status = VehicleStatusAssignmentFactory()
        data = self.post_data.copy()
        data["vehicle"] = vehicle_status.vehicle.id
        data["effective_start_date"] = "2020-11-20"

        url = reverse('driver:vehicle-status-assignment-detail', kwargs={ 'pk': vehicle_status.id})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['effective_start_date'], data['effective_start_date'])

