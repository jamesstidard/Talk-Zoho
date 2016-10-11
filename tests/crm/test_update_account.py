import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_update_account(crm):
    account    = {
        'ACCOUNTID': '703005000001871015',
        'Account Name': 'The boy right there'}
    account_id = yield crm.accounts.update(account, primary_key='ACCOUNTID')
    assert account_id
