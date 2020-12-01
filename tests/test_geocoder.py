import json
import mock
from pygeoirish.geocoder import (
    assemble_comparison,
    base_filter,
    read_townlands,
)
from .fixtures import (
    fixture_test_assemble_comparison,
    fixture_assemble_comparison_onedistance_nexac,
    fixture_items_base_filter,
    fixture_expected_base_filter,
    fixture_read_townlands,
    fixture_read_townlands_expected
)


def test_assemble_comparison():
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }

    final = assemble_comparison('WICKLOW', 'SOME COUNTY', item)

    dictA_str = json.dumps(final, sort_keys=True)
    dictB_str = json.dumps(
        fixture_test_assemble_comparison,
        sort_keys=True
    )

    assert dictA_str == dictB_str


def test_assemble_comparison_onedistance_nexac():
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }

    final = assemble_comparison('WICKLOW', 'SOME COUNTE', item)

    dictA_str = json.dumps(final, sort_keys=True)
    dictB_str = json.dumps(
        fixture_assemble_comparison_onedistance_nexac,
        sort_keys=True
    )

    assert dictA_str == dictB_str


def test_base_filter():
    english_name = 'NITEROI'
    county = 'RIO DE JANEIRO'

    result = base_filter(
        english_name,
        county,
        fixture_items_base_filter
    )

    dictA_str = json.dumps(result, sort_keys=True)
    dictB_str = json.dumps(
        fixture_expected_base_filter,
        sort_keys=True
    )

    assert dictA_str == dictB_str


@mock.patch(
    'pygeoirish.geocoder._read_townlands',
    return_value=fixture_read_townlands
)
def test_read_townlands(_rt):
    result = read_townlands()

    _rt.assert_called_once()

    dictA_str = json.dumps(
        result, sort_keys=True)
    dictB_str = json.dumps(
        fixture_read_townlands_expected,
        sort_keys=True
    )

    assert dictA_str == dictB_str
