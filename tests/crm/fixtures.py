import os

import pytest


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
def eu_contact_id(scope="session"):
    return "1770000000501005"
