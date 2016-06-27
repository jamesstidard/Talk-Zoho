import pytest

from tornado.web import HTTPError

from tests.books.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.books import filter_price_lists


@pytest.mark.gen_test
def test_can_get_price_lists(auth_token, organization_id):
    price_lists = yield filter_price_lists(
        auth_token=auth_token,
        region=EU,
        organization_id=organization_id)
    assert len(price_lists) > 0


@pytest.mark.gen_test
def test_one_price_list_is_list(auth_token, organization_id):
    price_lists = yield filter_price_lists(
        auth_token=auth_token,
        region=EU,
        organization_id=organization_id,
        limit=1)
    assert len(price_lists) == 1
    assert isinstance(price_lists, list)
