import os

import pytest

from talkzoho.regions import EU
from talkzoho.crm import filter_accounts


@pytest.mark.gen_test
def test_can_get_accounts():
    # Update record name
    token    = os.getenv('ZOHO_CRM_AUTH_TOKEN')
    accounts = yield filter_accounts(auth_token=token, region=EU)
    assert len(accounts) > 0
