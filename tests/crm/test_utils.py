from talkzoho.crm.utils import translate_item


def test_replace_null_strings_in_item():
    item = {
        "no": "1",
        "FL": [
            {
                "content": "null",
                "val": "SMOWNERID",
            }
        ]
    }
    item = translate_item(item)
    assert item['SMOWNERID'] is None


def test_single_fl_obj():
    item = {
        "no": "1",
        "FL": {
            "content": "12345",
            "val": "SMOWNERID",
        }
    }
    item = translate_item(item)
    assert item['SMOWNERID']
