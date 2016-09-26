import pytest

from tornado.web import HTTPError

from tests.crm.fixtures import *  # noqa

from talkzoho.crm import update_account


@pytest.mark.gen_test
def test_can_update_account(auth_token):
    account    = {'ACCOUNTID': '703005000001871015', 'Account Name': 'The boy right there'}
    account_id = yield update_account(account, auth_token=auth_token)
    assert account_id