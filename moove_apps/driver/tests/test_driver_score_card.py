from moove_apps.user.tests import LoggedInAPITestCase
from django.urls import reverse
from moove_apps.driver.factory import DriverScoreCardFactory
from moove_apps.driver.models import DriverScoreCard

class DriverScoreCardTest(LoggedInAPITestCase):

    fixtures = [
        'user.json',
        'vehicle.json',
        'driver.json'
    ]

    def setUp(self):
        user = self.get_user()
        super(DriverScoreCardTest, self).setUp()
        self.url = reverse('driver:driver-score-card-list')
        self.post_data = {
            "driver": 1,
            "conctact_type":"offline_driver",
            "reason_offline": ['not available']
        }
    
    def test_driver_score_card_create(self):
        response = self.client.post(self.url, data=self.post_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['driver'], 1)
        self.assertEqual(response.data['conctact_type'], self.post_data['conctact_type'])
        self.assertEqual(response.data['reason_offline'], self.post_data['reason_offline'])

    def test_driver_score_card_update(self):
        driver_score = DriverScoreCardFactory()
        data = self.post_data.copy()
        data["driver"] = driver_score.driver.id

        url = reverse('driver:driver-score-card-detail', kwargs={ 'pk': driver_score.id})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['conctact_type'], self.post_data['conctact_type'])
        self.assertEqual(response.data['reason_offline'], self.post_data['reason_offline'])
