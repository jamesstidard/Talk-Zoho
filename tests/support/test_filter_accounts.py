import pytest

from tornado.web import HTTPError

from tests.support.fixtures import *  # noqa


@pytest.mark.gen_test
def test_one_account_is_list(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=1)
    assert len(accounts) == 1
    assert isinstance(accounts, list)


@pytest.mark.gen_test
def test_account_looks_right(support, portal, department):
    [account] = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=1)
    assert 'ACCOUNTID' in account.keys()
    assert len(account.keys()) > 4


@pytest.mark.gen_test
def test_column_whitelist(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        columns=['ACCOUNTID', 'Account Name'])
    account = accounts[0]
    assert 'ACCOUNTID' in account.keys()
    assert 'Account Name' in account.keys()
    assert len(account.keys()) == 2


@pytest.mark.gen_test
def test_search_term(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=1,
        term='IFPL')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_search_term_lower(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=1,
        term='ifpl')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_search_term_partial(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=1,
        term='ifp')
    account = accounts[0]
    assert account['Account Name'] == 'IFPL'


@pytest.mark.gen_test
def test_zero_limit(support, portal, department):
    accounts = yield from support.accounts.filter(
        department=department,
        portal=portal,
        limit=0)
    assert len(accounts) == 0


@pytest.mark.gen_test
def test_404(support, portal, department):
    with pytest.raises(HTTPError) as excinfo:
        yield from support.accounts.filter(
            department=department,
            portal=portal,
            offset=40000)
    assert excinfo.value.status_code == 404
