import pytest

from tests.crm.fixtures import *  # noqa

from talkzoho.crm import insert_potential


@pytest.mark.gen_test
def test_can_insert_potential(auth_token):
    potential = {
        'Potential Name': '2SFG Foxes Uttoxeter Transmitters'}
    potential_id = yield insert_potential(
        record=potential,
        auth_token=auth_token)
    assert potential_id
