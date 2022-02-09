import os


class CredentialsUtility:

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("The API creds must be a env variables")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The Database creds must be a env variables")
        else:
            return {'db_user': db_user, 'db_password': db_password}