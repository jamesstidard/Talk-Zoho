import pytest

from tests.books.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.books import get_price_book


@pytest.mark.gen_test
def test_can_get_account(auth_token, organization_id, price_book_id):
    price_book = yield get_price_book(
        organization_id=organization_id,
        auth_token=auth_token,
        region=EU,
        id=price_book_id)
    print(price_book)
    assert price_book['pricebook_id'] == price_book_id
