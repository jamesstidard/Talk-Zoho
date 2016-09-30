import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho.crm import get_account
from talkzoho.utils import wait


@pytest.mark.gen_test
def test_can_get_account(auth_token, account_id):
    account = yield get_account(
        auth_token=auth_token,
        id=account_id)
    assert account['ACCOUNTID'] == account_id


def test_can_get_account_sync(auth_token, account_id):
    account = wait(
        get_account,
        auth_token=auth_token,
        id=account_id)
    assert account['ACCOUNTID'] == account_id
