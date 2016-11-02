import pytest

from tests.books.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_price_books(books, organization_id):
    price_books = yield books.price_books.filter(
        organization_id=organization_id)
    assert len(price_books) > 0


@pytest.mark.gen_test
def test_one_price_book_is_book(books, organization_id):
    price_books = yield books.price_books.filter(
        organization_id=organization_id,
        limit=1)
    assert len(price_books) == 1
    assert isinstance(price_books, list)
