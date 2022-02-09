import requests
import logging as logger
import os
import json
from poc_api_pytest.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1

from poc_api_pytest.src.utilities.credentialsUtility import CredentialsUtility


class RequestsUtility:

    def __init__(self):
        self.wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(self.wc_creds['wc_key'], self.wc_creds['wc_secret'])

    def post(self, endpoint, payload=None, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), auth=self.auth, headers=headers)
        logger.debug(f"POST API response: {rs_api.json()}")
        return rs_api

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint
        rs_api = requests.get(url=url, data=json.dumps(payload), auth=self.auth, headers=headers)
        logger.debug(f"GET API response: {rs_api.json()}")
        return rs_api
