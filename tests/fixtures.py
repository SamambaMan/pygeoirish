fixture_test_assemble_comparison = {
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

fixture_assemble_comparison_onedistance_nexac = {
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

fixture_items_base_filter = [
    {
        "County": "Some County",
        "English_Name": "Wicklow"
    },
    {
        "County": "Rio de Janeiro",
        "English_Name": "Niteroi"
    }
]

fixture_expected_base_filter = [
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

fixture_read_townlands = [
    {'English_Name': "one or another"},
    {'English_Name': "a single one"},
]

fixture_read_townlands_expected = [
    {'English_Name': 'one'},
    {'English_Name': 'another'},
    {'English_Name': 'a single one'}
]
