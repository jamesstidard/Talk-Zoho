import os

import pytest

from talkzoho import BooksClient


@pytest.fixture
def books(auth_token, scope='session'):
    return BooksClient(auth_token=auth_token)


@pytest.fixture
def auth_token(scope="session"):
    return os.getenv('ZOHO_BOOKS_AUTH_TOKEN')


@pytest.fixture
def organization_id(scope='session'):
    return '40529048'


@pytest.fixture
def price_book_id(scope="session"):
    return "95830000001120003"
