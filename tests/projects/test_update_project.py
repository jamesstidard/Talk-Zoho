import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_project(projects, portal_id):
    project_id = yield projects.projects.insert(
        {'name': 'Inserted Project'},
        portal_id=portal_id)
    updated_project = yield projects.projects.update(
        {'id': project_id,
        'name': 'Updated Name',
        'status': 'active'},
        portal_id=portal_id)
    assert updated_project['id'] == project_id
    assert updated_project['name'] == 'Updated Name'
    yield projects.projects.delete(project_id, portal_id=portal_id)
