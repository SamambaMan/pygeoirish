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

fixture_test_serializer_in = [
    {
        'fullitem': {
            'ITM_E': 676967,
            'ITM_N': 666141
        },
        'Countie': 'Test countie 1'
    },
    {
        'fullitem': {
            'ITM_E': 682308,
            'ITM_N': 680683
        },
        'Countie': 'Test countie 2'
    },
    {
        'fullitem': {
            'ITM_E': 679583,
            'ITM_N': 670627
        },
        'Countie': 'Test countie 3'
    }
]

fixture_test_serializer_out = [
    {
        'Countie': 'Test countie 1',
        'fullitem': {'ITM_E': 676967, 'ITM_N': 666141},
        'geo': (52.74086090887284, -6.860173125636178),
        'level': 'alevel'
    },
    {
        'Countie': 'Test countie 2',
        'fullitem': {'ITM_E': 682308, 'ITM_N': 680683},
        'geo': (52.87074497504706, -6.777435463419953),
        'level': 'alevel'
    },
    {
        'Countie': 'Test countie 3',
        'fullitem': {'ITM_E': 679583, 'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'level': 'alevel'
    }
]

fixture_prefered_exact = [
    {'exact': True},
    {'exact': False}
]

fixture_prefered_nexact = [
    {'exact': False},
    {'exact': False}
]

fixture_comparer_basic = [([
    {
        'County': 'Some County',
        'English_Name': 'Some English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    },
    {
        'County': 'Other County',
        'English_Name': 'Other English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    }
], 'basic')]


fixture_geocode_basic = [
    {
        'cdist': 0,
        'distance': 0,
        'edist': 0,
        'equals': True,
        'exact': True,
        'fullitem': {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627
        },
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOME COUNTY',
        'item_english_name': 'SOME ENGLISH NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'
    }
]

fixture_comparer_colision_match = [([
    {
        'County': 'Some County',
        'English_Name': 'Some English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    },
    {
        'County': 'Some Countys',
        'English_Name': 'Some Englishs Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    }
], 'basic')]

fixture_geocode_colision_match = [
    {
        'cdist': 0,
        'distance': 0,
        'edist': 0,
        'equals': True,
        'exact': True,
        'fullitem': {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOME COUNTY',
        'item_english_name': 'SOME ENGLISH NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'
    }
]

fixture_comparer_colision_aproximate = [([
    {
        'County': 'Somei County',
        'English_Name': 'Some English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    },
    {
        'County': 'Some Countys',
        'English_Name': 'Some Englishs Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    }
], 'basic')]

fixture_geocode_colision_aproximate = [
    {
        'cdist': 1,
        'distance': 1,
        'edist': 0,
        'equals': True,
        'exact': False,
        'fullitem': {
            'County': 'Somei County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOMEI COUNTY',
        'item_english_name': 'SOME ENGLISH NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'},
    {
        'cdist': 1,
        'distance': 2,
        'edist': 1,
        'equals': True,
        'exact': False,
        'fullitem': {
            'County': 'Some Countys',
            'English_Name': 'Some Englishs Name',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOME COUNTYS',
        'item_english_name': 'SOME ENGLISHS NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'
    }
]


fixture_comparer_fullcolision_match = [([
    {
        'County': 'Some County',
        'English_Name': 'Some English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    },
    {
        'County': 'Some County',
        'English_Name': 'Some English Name',
        'ITM_E': 679583,
        'ITM_N': 670627
    }
], 'basic')]

fixture_geocode_fullcolision_match = [
    {
        'cdist': 0,
        'distance': 0,
        'edist': 0,
        'equals': True,
        'exact': True,
        'fullitem': {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOME COUNTY',
        'item_english_name': 'SOME ENGLISH NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'},
    {
        'cdist': 0,
        'distance': 0,
        'edist': 0,
        'equals': True,
        'exact': True,
        'fullitem': {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'SOME COUNTY',
        'item_english_name': 'SOME ENGLISH NAME',
        'level': 'basic',
        'query_county': 'SOME COUNTY',
        'query_english_name': 'SOME ENGLISH NAME'
    }
]

fixture_comparer_county = [
    ([
        {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627
        },
        {
            'County': 'Some County',
            'English_Name': 'Some English Name',
            'ITM_E': 679583,
            'ITM_N': 670627
        }
    ], 'basic'),
    ([
        {
            'County': 'A County',
            'English_Name': 'A County',
            'ITM_E': 679583,
            'ITM_N': 670627
        },
        {
            'County': 'Another County',
            'English_Name': 'Another County',
            'ITM_E': 679583,
            'ITM_N': 670627
        }
    ], 'county')
]

fixture_geocode_county = [
    {
        'cdist': 0,
        'distance': 0,
        'edist': 0,
        'equals': True,
        'exact': True,
        'fullitem': {
            'County': 'A County',
            'English_Name': 'A County',
            'ITM_E': 679583,
            'ITM_N': 670627},
        'geo': (52.78079326249755, -6.820351975635851),
        'item_county': 'A COUNTY',
        'item_english_name': 'A COUNTY',
        'level': 'county',
        'query_county': 'A COUNTY',
        'query_english_name': 'A COUNTY'}]
