import pytest

from tornado.web import HTTPError

from tests.books.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.books import filter_price_books


@pytest.mark.gen_test
def test_can_get_price_books(auth_token, organization_id):
    price_books = yield filter_price_books(
        auth_token=auth_token,
        region=EU,
        organization_id=organization_id)
    assert len(price_books) > 0


@pytest.mark.gen_test
def test_one_price_book_is_book(auth_token, organization_id):
    price_books = yield filter_price_books(
        auth_token=auth_token,
        region=EU,
        organization_id=organization_id,
        limit=1)
    assert len(price_books) == 1
    assert isinstance(price_books, list)
