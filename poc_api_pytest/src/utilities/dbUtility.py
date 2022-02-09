import pymysql
import logging as logger

from poc_api_pytest.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility:

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], password=self.creds['db_password'], port=3309)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed runing sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict
