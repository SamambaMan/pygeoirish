import json
from pygeoirish.geocoder import (
    assemble_comparison,
    base_filter
)
from pprint import pprint


def test_assemble_comparison():
    fixture = {
        "cdist": 0, 
        "distance": 0, 
        "edist": 0, 
        "equals": True, 
        "exact": True, 
        "fullitem": {
            "County": "Some County", 
            "English_Name": "Wicklow"
        }, 
        "item_county": "SOME COUNTY", 
        "item_english_name": "WICKLOW",
        "query_county": "SOME COUNTY",
        "query_english_name": "WICKLOW"
    }
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }
    
    final = assemble_comparison('WICKLOW', 'SOME COUNTY', item)

    dictA_str = json.dumps(final, sort_keys=True)
    dictB_str = json.dumps(fixture, sort_keys=True)

    assert dictA_str == dictB_str


def test_assemble_comparison_onedistance_nexac():
    fixture = {
        "cdist": 1, 
        "distance": 1, 
        "edist": 0, 
        "equals": True, 
        "exact": False, 
        "fullitem": {
            "County": "Some County", 
            "English_Name": "Wicklow"
        }, 
        "item_county": "SOME COUNTY", 
        "item_english_name": "WICKLOW",
        "query_county": "SOME COUNTE",
        "query_english_name": "WICKLOW"
    }
    item = {
        'English_Name': 'Wicklow',
        'County': 'Some County'
    }
    
    final = assemble_comparison('WICKLOW', 'SOME COUNTE', item)

    dictA_str = json.dumps(final, sort_keys=True)
    dictB_str = json.dumps(fixture, sort_keys=True)

    assert dictA_str == dictB_str


def test_base_filter():
    fixture_items = [
        {
            "County": "Some County", 
            "English_Name": "Wicklow"
        },
        {
            "County": "Rio de Janeiro", 
            "English_Name": "Niteroi"
        }
    ]

    english_name = 'NITEROI'
    county = 'RIO DE JANEIRO'

    result = base_filter(
        english_name,
        county,
        fixture_items
    )

    fixture_expected = [
        {
            'cdist': 0,
            'distance': 0,
            'edist': 0,
            'equals': True,
            'exact': True,
            'fullitem': {
                'County': 'Rio de Janeiro',
                'English_Name': 'Niteroi'
            },
            'item_county': 'RIO DE JANEIRO',
            'item_english_name': 'NITEROI',
            'query_county': 'RIO DE JANEIRO',
            'query_english_name': 'NITEROI'}
    ]

    dictA_str = json.dumps(result, sort_keys=True)
    dictB_str = json.dumps(fixture_expected, sort_keys=True)

    assert dictA_str == dictB_str