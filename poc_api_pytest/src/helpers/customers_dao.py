import random

from poc_api_pytest.src.utilities.dbUtility import DBUtility


class CustomersDAO:
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM exampledb.wp_users WHERE user_email = '{email}'; "
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_customer_random_user_db(self, qty=1):
        sql = "SELECT * FROM exampledb.wp_users order by rand() LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, qty)