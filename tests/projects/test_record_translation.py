from datetime import datetime, date

from talkzoho.projects.utils import to_zoho_value


def test_datetime_to_correct_format():
    now = datetime(year=2016, month=2, day=1, hour=4, minute=30)
    assert '02-01-2016' == to_zoho_value(now)


def test_date_to_correct_format():
    now = date(year=2016, month=2, day=1)
    assert '02-01-2016' == to_zoho_value(now)


def test_id_list_to_correct_format():
    ids = ['1', '2', '3']
    assert '1,2,3' == to_zoho_value(ids)
