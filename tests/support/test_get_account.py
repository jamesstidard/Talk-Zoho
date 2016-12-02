import pytest

from tornado.web import HTTPError

from tests.support.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_account(support, portal, department, account_id):
    account = yield from support.accounts.get(
        department=department,
        portal=portal,
        id=account_id)
    assert account['ACCOUNTID'] == account_id
