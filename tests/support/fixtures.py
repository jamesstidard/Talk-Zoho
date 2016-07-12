import os

import pytest


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_SUPPORT_AUTH_TOKEN')


@pytest.fixture
def portal(scope='session'):
    return 'a2zcloud'


@pytest.fixture
def department(scope='session'):
    return 'A2Z Cloud - Customer Tickets'


@pytest.fixture
def account_id(scope='session'):
    return '40000000277224'
