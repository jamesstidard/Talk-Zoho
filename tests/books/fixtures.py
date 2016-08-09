import os

import pytest


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_BOOKS_AUTH_TOKEN')


@pytest.fixture
def organization_id(scope='session'):
    return '20000146105'


@pytest.fixture
def price_book_id(scope="session"):
    return "39000000244369"
