import pytest

from tests.books.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_account(books, organization_id, price_book_id):
    price_book = yield books.price_books.get(
        organization_id=organization_id,
        id=price_book_id)
    print(price_book)
    assert price_book['pricebook_id'] == price_book_id
