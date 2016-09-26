import pytest

from tornado.web import HTTPError

from tests.support.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.support import filter_accounts


@pytest.mark.gen_test
def test_one_account_is_list(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=1)
    assert len(accounts) == 1
    assert isinstance(accounts, list)


@pytest.mark.gen_test
def test_account_looks_right(auth_token, portal, department):
    [account] = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=1)
    assert 'ACCOUNTID' in account.keys()
    assert len(account.keys()) > 4


@pytest.mark.gen_test
def test_column_whitelist(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        columns=['ACCOUNTID', 'Account Name'])
    account = accounts[0]
    assert 'ACCOUNTID' in account.keys()
    assert 'Account Name' in account.keys()
    assert len(account.keys()) == 2


@pytest.mark.gen_test
def test_search_term(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=1,
        term='IFPL')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_search_term_lower(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=1,
        term='ifpl')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_search_term_partial(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=1,
        term='ifp')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_zero_limit(auth_token, portal, department):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        department=department,
        region=EU,
        portal=portal,
        limit=0)
    assert len(accounts) == 0


@pytest.mark.gen_test
def test_404(auth_token, portal, department):
    with pytest.raises(HTTPError) as excinfo:
        yield filter_accounts(
            auth_token=auth_token,
            department=department,
            region=EU,
            portal=portal,
            offset=40000)
    assert excinfo.value.status_code == 404
