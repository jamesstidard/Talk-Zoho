import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_delete_account(crm):
    account    = {'Account Name': 'DELETE ME'}
    account_id = yield crm.accounts.insert(account)
    result     = yield crm.accounts.delete(account_id)
    assert result is True
