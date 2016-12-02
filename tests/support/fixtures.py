import os

import pytest

from talkzoho import SupportClient
from talkzoho.regions import EU


@pytest.fixture
def support(scope="session"):
    return SupportClient(
        auth_token=os.getenv('ZOHO_SUPPORT_AUTH_TOKEN'),
        region=EU)


@pytest.fixture
def portal(scope='session'):
    return 'a2zcloud'


@pytest.fixture
def department(scope='session'):
    return 'A2Z Cloud - Customer Tickets'


@pytest.fixture
def account_id(scope='session'):
    return '40000000277224'
