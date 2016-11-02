import pytest

from tornado.web import HTTPError

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_accounts(crm):
    accounts = yield crm.accounts.filter()
    assert len(accounts) > 0


@pytest.mark.gen_test
def test_one_account_is_list(crm):
    accounts = yield crm.accounts.filter(limit=1)
    assert len(accounts) == 1
    assert isinstance(accounts, list)


@pytest.mark.gen_test
def test_account_looks_right(crm):
    [account] = yield crm.accounts.filter(limit=1)
    assert 'ACCOUNTID' in account.keys()
    assert len(account.keys()) > 5


@pytest.mark.gen_test
def test_column_whitelist(crm):
    [account] = yield crm.accounts.filter(
        limit=1,
        columns=['ACCOUNTID', 'Account Name'])
    assert 'ACCOUNTID' in account.keys()
    assert 'Account Name' in account.keys()
    assert len(account.keys()) == 2


@pytest.mark.gen_test
def test_search_term(crm):
    [account] = yield crm.accounts.filter(limit=1, term='4 Solo Ltd')
    assert account['Account Name'] == '4 Solo Ltd'


@pytest.mark.gen_test
def test_zero_limit(crm):
    accounts = yield crm.accounts.filter(limit=0)
    assert len(accounts) == 0


@pytest.mark.gen_test
def test_404(crm):
    with pytest.raises(HTTPError) as excinfo:
        yield crm.accounts.filter(offset=4000000)
    assert excinfo.value.status_code == 404
