import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_quotes(crm):
    accounts = yield crm.quotes.filter()
    assert len(accounts) > 0
