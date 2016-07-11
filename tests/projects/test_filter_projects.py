import pytest

from tornado.web import HTTPError

from tests.projects.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.projects import filter_projects


@pytest.mark.gen_test
def test_can_get_accounts(auth_token, portal_id):
    accounts = yield filter_projects(
        auth_token=auth_token,
        region=EU,
        portal_id=portal_id)
    assert len(accounts) > 0
