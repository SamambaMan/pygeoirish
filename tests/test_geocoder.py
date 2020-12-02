import json
import mock
from pygeoirish.geocoder import (
    assemble_comparison,
    base_filter,
    read_townlands,
    serialize,
    extract_prefered_addresses,
    geocode
)
from .fixtures import (
    fixture_test_assemble_comparison,
    fixture_assemble_comparison_onedistance_nexac,
    fixture_items_base_filter,
    fixture_expected_base_filter,
    fixture_read_townlands,
    fixture_read_townlands_expected,
    fixture_test_serializer_in,
    fixture_test_serializer_out,
    fixture_prefered_exact,
    fixture_prefered_nexact,
    fixture_comparer_basic,
    fixture_geocode_basic,
    fixture_comparer_colision_match,
    fixture_geocode_colision_match,
    fixture_comparer_colision_aproximate,
    fixture_geocode_colision_aproximate,
    fixture_comparer_fullcolision_match,
    fixture_geocode_fullcolision_match,
    fixture_comparer_county,
    fixture_geocode_county
)


def compare_dicts(dicta, dictb):
    dicta = json.dumps(dicta, sort_keys=True)
    dictb = json.dumps(dictb, sort_keys=True)
    return dicta == dictb


def test_assemble_comparison():
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }

    final = assemble_comparison('WICKLOW', 'SOME COUNTY', item)

    assert compare_dicts(
        final,
        fixture_test_assemble_comparison
    )


def test_assemble_comparison_onedistance_nexac():
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }

    final = assemble_comparison('WICKLOW', 'SOME COUNTE', item)

    assert compare_dicts(
        final,
        fixture_assemble_comparison_onedistance_nexac
    )


def test_base_filter():
    english_name = 'NITEROI'
    county = 'RIO DE JANEIRO'

    result = base_filter(
        english_name,
        county,
        fixture_items_base_filter
    )

    assert compare_dicts(
        result,
        fixture_expected_base_filter
    )


@mock.patch(
    'pygeoirish.geocoder._read_townlands',
    return_value=fixture_read_townlands
)
def test_read_townlands(_rt):
    result = read_townlands()

    _rt.assert_called_once()

    assert compare_dicts(
        result,
        fixture_read_townlands_expected
    )


def test_serializer_in():
    output = serialize(fixture_test_serializer_in, 'alevel')

    assert compare_dicts(
        output,
        fixture_test_serializer_out
    )


def test_extract_prefered_addresses_exact():
    result = extract_prefered_addresses(
        fixture_prefered_exact
    )

    assert len(result) == 1


def test_extract_prefered_addresses_nexact():
    result = extract_prefered_addresses(
        fixture_prefered_nexact
    )

    assert len(result) == 2


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_basic
)
def test_basic_geocode():
    result = geocode('Some English Name, Some County')

    assert compare_dicts(
        result,
        fixture_geocode_basic
    )


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_basic
)
def test_basic_geocode_exaustion():
    result = geocode('Some English Name, Doesnt Matters,Some County')

    assert compare_dicts(
        result,
        fixture_geocode_basic
    )


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_colision_match
)
def test_collision_match_geocode():
    result = geocode('Some English Name, Some County')

    assert compare_dicts(
        result,
        fixture_geocode_colision_match
    )


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_colision_aproximate
)
def test_collision_aproximate_geocode():
    result = geocode('Some English Name, Some County')

    assert compare_dicts(
        result,
        fixture_geocode_colision_aproximate
    )


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_fullcolision_match
)
def test_fullcollision_aproximate_geocode():
    result = geocode('Some English Name, Some County')

    assert compare_dicts(
        result,
        fixture_geocode_fullcolision_match
    )


@mock.patch(
    'pygeoirish.geocoder.comparers',
    fixture_comparer_county
)
def test_geocode_county():
    result = geocode("A County")

    assert compare_dicts(
        result,
        fixture_geocode_county
    )
