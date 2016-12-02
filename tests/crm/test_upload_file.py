import pytest

from tests.crm.fixtures import *  # noqa


@pytest.mark.gen_test
def test_can_add_and_delete_file(crm):
    [potential] = yield from crm.potentials.filter(limit=1)
    file_url    = 'https://www.google.com'
    file_id     = yield from crm.potentials.upload_file(
        record_id=potential['POTENTIALID'],
        url=file_url)
    yield from crm.potentials.delete_file(file_id)
