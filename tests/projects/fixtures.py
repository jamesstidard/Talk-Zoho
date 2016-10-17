import os

import pytest

from talkzoho import ProjectsClient
from talkzoho.regions import EU


@pytest.fixture
def projects(auth_token, scope='session'):
    return ProjectsClient(auth_token=auth_token, region=EU)


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_PROJECTS_AUTH_TOKEN')


@pytest.fixture
def portal_id(scope='session'):
    return '20000147202'


@pytest.fixture
def project_id(scope='session'):
    return '195000000138025'
