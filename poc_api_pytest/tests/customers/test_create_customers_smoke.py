import pytest
import logging as logger

from poc_api_pytest.src.helpers.customers_dao import CustomersDAO
from poc_api_pytest.src.helpers.customers_helper import CustomerHelper
from poc_api_pytest.src.utilities.genericUtilities import generate_random_email_and_password


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Testing the customer creation with email and pass only.")
    rand_info = generate_random_email_and_password()

    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify status code of the call
    assert cust_api_info.status_code == 201

    # verify email in the response
    result = cust_api_info.json()
    assert result['email'] == email, f"The expected email is: {email} but got {result['email']}"
    assert result['first_name'] == '', f"name should be empty but got {result['name']}"
    # verify customer is created in DB
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    id_in_api = result['id']
    id_in_db = cust_info[0]['ID']
    import pdb; pdb.set_trace()
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database' \
                                  f'Email: {email}'
