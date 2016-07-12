import pytest

from tornado.web import HTTPError

from tests.crm.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.crm import filter_accounts


@pytest.mark.gen_test
def test_can_get_accounts(auth_token):
    accounts = yield filter_accounts(auth_token=auth_token, region=EU)
    assert len(accounts) > 0


@pytest.mark.gen_test
def test_one_account_is_list(auth_token):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        region=EU,
        limit=1)
    assert len(accounts) == 1
    assert isinstance(accounts, list)


@pytest.mark.gen_test
def test_account_looks_right(auth_token):
    [account] = yield filter_accounts(
        auth_token=auth_token,
        region=EU,
        limit=1)
    assert 'ACCOUNTID' in account.keys()
    assert len(account.keys()) > 5


@pytest.mark.gen_test
def test_column_whitelist(auth_token):
    [account] = yield filter_accounts(
        auth_token=auth_token,
        region=EU,
        limit=1,
        columns=['ACCOUNTID', 'Account Name'])
    assert 'ACCOUNTID' in account.keys()
    assert 'Account Name' in account.keys()
    assert len(account.keys()) == 2


@pytest.mark.gen_test
def test_search_term(auth_token):
    [account] = yield filter_accounts(
        auth_token=auth_token,
        region=EU,
        limit=1,
        term='Orbital Foods')
    assert account['Account Name'] == 'Orbital Foods Limited'


@pytest.mark.gen_test
def test_zero_limit(auth_token):
    accounts = yield filter_accounts(
        auth_token=auth_token,
        region=EU,
        limit=0)
    assert len(accounts) == 0


@pytest.mark.gen_test
def test_404(auth_token):
    with pytest.raises(HTTPError) as excinfo:
        yield filter_accounts(auth_token=auth_token, region=EU, offset=4000000)
    assert excinfo.value.status_code == 404
