from rest_framework.test import APITransactionTestCase
from moove_apps.user.models import User

class LoggedInAPITestCase(APITransactionTestCase):
    """
    A test case in which a given user is logged in in setup, and the user is logged out in teardown.
    """

    # Default pk of user to log in
    user_pk = 1

    def get_user(self):
        '''
        Get the user to log in.
        '''
        return User.objects.filter(pk=self.user_pk).get()

    def setUp(self):
        user = self.get_user()
        self.client.force_authenticate(user=user)

    def tearDown(self):
        self.client.force_authenticate(user=None)
