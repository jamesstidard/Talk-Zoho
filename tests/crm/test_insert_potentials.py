import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_insert_potential(crm):
    potential = {'Potential Name': '2SFG Foxes Uttoxeter Transmitters'}
    potential_id = yield crm.potentials.insert(potential)
    assert potential_id
