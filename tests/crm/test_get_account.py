import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho.utils import wait


@pytest.mark.gen_test
def test_can_get_account(crm, account_id):
    account = yield crm.accounts.get(account_id)
    assert account['ACCOUNTID'] == account_id


def test_can_get_account_sync(crm, account_id):
    account = wait(crm.accounts.get, account_id)
    assert account['ACCOUNTID'] == account_id
