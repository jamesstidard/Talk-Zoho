from talkzoho.crm.crm_client import ModuleMap
from talkzoho.crm.utils import translate_item, make_module_id_name


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


def test_make_module_id_name_default_module():
    module_map = ModuleMap(
        canonical_name='Potentials',
        singular_alias='Opportunity',
        plural_alias='Opportunities')
    assert 'POTENTIALID' == make_module_id_name(module_map)
