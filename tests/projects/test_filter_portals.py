import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_filter_portals(projects):
    portals = yield projects.portals.filter(limit=1)
    assert isinstance(portals, list)
