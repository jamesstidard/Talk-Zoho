import pytest

from tests.projects.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_filter_projects(projects, portal_id):
    projects = yield projects.projects.filter(portal_id=portal_id, limit=1)
    assert isinstance(projects, list)


@pytest.mark.gen_test
def test_filter_projects_looks_right(projects, portal_id):
    [project] = yield projects.projects.filter(portal_id=portal_id, limit=1)
    assert 'bug_count' in project
    assert 'milestone_count' in project
