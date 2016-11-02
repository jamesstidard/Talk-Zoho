import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_access_alias(eu_crm):
    eu_crm.use_module_aliases = True
    [requirement] = yield eu_crm.scorecard_requirements.filter(limit=1)
