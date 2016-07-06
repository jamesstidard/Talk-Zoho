import pytest

from tornado.web import HTTPError

from tests.projects.fixtures import *  # noqa

from talkzoho.regions import EU
from talkzoho.projects import get_project


@pytest.mark.gen_test
def test_can_get_project(auth_token, portal_id, project_id):
    project = yield get_project(
        auth_token=auth_token,
        region=EU,
        portal_id=portal_id,
        id=project_id)
    assert project['id_string'] == project_id
