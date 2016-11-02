import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_filter_users(projects, portal_id):
    users = yield projects.users.filter(portal_id=portal_id, limit=1)
    assert isinstance(users, list)


@pytest.mark.gen_test
def test_filter_user_looks_right(projects, portal_id):
    [user] = yield projects.users.filter(portal_id=portal_id, limit=1)
    assert 'email' in user
    assert 'name' in user
    assert 'role' in user
