import os

import pytest

from talkzoho import ProjectsClient


@pytest.fixture
def projects(auth_token, scope='session'):
    return ProjectsClient(auth_token=auth_token)


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_PROJECTS_AUTH_TOKEN')


@pytest.fixture
def portal_id(scope='session'):
    return '39178228'


@pytest.fixture
def project_id(scope='session'):
    return '708124000000406005'
