import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_contact(crm, contact_id):
    contact = yield crm.contacts.get(contact_id)
    assert contact['CONTACTID'] == contact_id


@pytest.mark.gen_test
def test_eu_can_get_contact(eu_crm, eu_contact_id):
    contact = yield eu_crm.contacts.get(eu_contact_id)
    assert contact['CONTACTID'] == eu_contact_id
