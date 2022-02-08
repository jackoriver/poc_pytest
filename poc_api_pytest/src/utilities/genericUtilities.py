import logging as logger
import random
import string


def generate_random_email_and_password(domain='poc.com', email_prefix='testuser'):
    logger.debug("Generating random email and password")

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_lowercase, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")
    return random_info