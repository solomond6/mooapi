from moove_apps.user.tests import LoggedInAPITestCase
from django.urls import reverse
from moove_apps.driver.factory import DriverScoreCardFactory
from moove_apps.driver.models import DriverGPA

class DriverInfractions(LoggedInAPITestCase):

    fixtures = [
        'user.json',
        'vehicle.json',
        'driver.json',
        'infractions.json'
    ]

    def setUp(self):
        user = self.get_user()
        super(DriverInfractions, self).setUp()
        self.url = reverse('driver:driver-infraction-list')
        self.post_data = {
            "driver": 1,
            "infractions":1,
            "date": "2021-01-18"
        }
    
    def test_infraction_create(self):
        response = self.client.post(self.url, data=self.post_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        current_driver_gpa = DriverGPA.objects.get(pk=1)
        self.assertEqual(current_driver_gpa.current_gpa, 4)


    