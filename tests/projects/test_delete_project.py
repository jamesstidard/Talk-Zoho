import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_cant_delete_user(projects, portal_id):
    # Deleting user with wrong id always returns true (CRM API limitation)
    # Pull projects down to lowest common denominator for unified interface.
    success = yield projects.projects.delete('123456789', portal_id=portal_id)
    assert success
