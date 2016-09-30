import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho import crm


@pytest.mark.gen_test
def test_can_upload_contact_file(auth_token, contact_id, file_url):
    file_id = yield crm.upload_file(
        id=contact_id,
        url=file_url,
        module='Contacts',
        auth_token=auth_token)
    yield crm.delete_file(
        id=file_id,
        module='Contacts',
        auth_token=auth_token)
