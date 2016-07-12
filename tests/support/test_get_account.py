import pytest

from tornado.web import HTTPError

from tests.support.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.support import get_account


@pytest.mark.gen_test
def test_can_get_account(auth_token, portal, department, account_id):
    account = yield get_account(
        auth_token=auth_token,
        region=EU,
        portal=portal,
        department=department,
        id=account_id)
    assert account['ACCOUNTID'] == account_id
