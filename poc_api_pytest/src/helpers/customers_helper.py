from poc_api_pytest.src.utilities.genericUtilities import generate_random_email_and_password
from poc_api_pytest.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper:

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password='Password1', **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        return self.requests_utility.post('customers', payload=payload)
