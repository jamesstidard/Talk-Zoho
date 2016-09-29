import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.crm import get_contact


@pytest.mark.gen_test
def test_can_get_contact(auth_token, contact_id):
    contact = yield get_contact(
        auth_token=auth_token,
        id=contact_id)
    assert contact['CONTACTID'] == contact_id


@pytest.mark.gen_test
def test_eu_can_get_contact(eu_auth_token, eu_contact_id):
    contact = yield get_contact(
        auth_token=eu_auth_token,
        region=EU,
        id=eu_contact_id)
    assert contact['CONTACTID'] == eu_contact_id
