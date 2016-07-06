import os

import pytest


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_PROJECTS_AUTH_TOKEN')


@pytest.fixture
def portal_id(scope='session'):
    return '20000147202'


@pytest.fixture
def project_id(scope='session'):
    return '195000000138025'
