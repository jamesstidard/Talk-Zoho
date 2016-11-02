import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_get_project(projects, portal_id, project_id):
    project = yield projects.projects.get(project_id, portal_id=portal_id)
    assert project['id_string'] == project_id
