import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho.crm import insert_account, delete_account


@pytest.mark.gen_test
def test_can_delete_account(auth_token):
    account    = {'Account Name': 'DELETE ME'}
    account_id = yield insert_account(account, auth_token=auth_token)
    result     = yield delete_account(id=account_id, auth_token=auth_token)
    assert result is True
