import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_insert_project(projects, portal_id):
    project_id = yield projects.projects.insert({
        'name': 'Test Project',
        'portal_id': portal_id})
    assert project_id
