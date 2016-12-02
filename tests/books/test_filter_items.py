import pytest

from tests.books.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_items(books, organization_id):
    items = yield books.items.filter(organization_id=organization_id)
    assert len(items) > 0


@pytest.mark.gen_test
def test_one_item_is_item(books, organization_id):
    items = yield books.items.filter(
        organization_id=organization_id,
        limit=1)
    assert len(items) == 1
    assert isinstance(items, list)
