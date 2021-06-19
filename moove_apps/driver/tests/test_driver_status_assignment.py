from moove_apps.user.tests import LoggedInAPITestCase
from django.urls import reverse
from moove_apps.driver.factory import DriverStatusAssignmentFactory
from moove_apps.driver.models import DriverStatusAssignment

class DriverStatusAssignmentTest(LoggedInAPITestCase):

    fixtures = [
        'user.json',
        'vehicle.json',
        'driver.json'
    ]

    def setUp(self):
        user = self.get_user()
        super(DriverStatusAssignmentTest, self).setUp()
        self.url = reverse('driver:status-assignment-list')
        self.post_data = {
            "driver": 1,
            "status": "Active",
            "effective_start_date": "2020-11-20"
        }

    def test_driver_status_assignment_create(self):
        response = self.client.post(self.url, data=self.post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['driver'], 1)
    
    def test_driver_vehicle_assignment_update(self):
        driver_status_assignment = DriverStatusAssignmentFactory()
        data = { 'effective_end_date': '2020-11-30', 'effective_start_date': driver_status_assignment.effective_start_date}

        url = reverse('driver:status-assignment-detail', kwargs={ 'pk': driver_status_assignment.id})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['effective_end_date'], data['effective_end_date'])

    def test_previous_efective_end_date_automatically_populated_on_create(self):
        driver_status_assignment = DriverStatusAssignmentFactory()
        self.assertEqual(driver_status_assignment.effective_end_date, None)
        
        data = self.post_data.copy()
        data['driver'] = driver_status_assignment.driver.id
        response = self.client.post(self.url, data=data, format='json')
        previous = DriverStatusAssignment.objects.get(pk=driver_status_assignment.pk)

        self.assertEqual(previous.effective_end_date.strftime("%Y-%m-%d"), response.data['effective_start_date'])
