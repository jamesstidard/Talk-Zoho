import os

import pytest

from talkzoho import CRMClient
from talkzoho.regions import EU


@pytest.fixture
def crm(auth_token, scope='session'):
    return CRMClient(auth_token=auth_token)


@pytest.fixture
def eu_crm(eu_auth_token, scope='session'):
    return CRMClient(auth_token=eu_auth_token, region=EU)


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_CRM_AUTH_TOKEN')


@pytest.fixture
def eu_auth_token(scope="session"):
    return os.getenv('EU_ZOHO_CRM_AUTH_TOKEN')


@pytest.fixture
def account_id(scope="session"):
    return "703005000000216311"


@pytest.fixture
def contact_id(scope="session"):
    return "703005000001944020"


@pytest.fixture
def product_id(scope="session"):
    return "703005000001647001"


@pytest.fixture
def eu_contact_id(scope="session"):
    return "1770000000501005"
