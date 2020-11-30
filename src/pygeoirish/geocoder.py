import csv
import re
from Levenshtein import distance
from .itm2utm import itm2geo


L_FACTOR = 3
F_CENTRES = ('datasets/Centres_of_Population_-_OSi_'
             'National_Placenames_Gazetteer.csv')
F_TOWNLANDS = ('datasets/Townlands_-_OSi_'
               'National_Placenames_Gazetteer.csv')


def read_centres():
    with open(F_CENTRES) as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_townlands():
    with open(F_TOWNLANDS) as file:
        reader = csv.DictReader(file)
        return list(reader)


def cleanup(term):
    term = term.upper()
    term = term.strip()
    terms = r"[^a-zA-Z0-9,]|^CO "
    term = re.sub(terms, ' ', term, flags=re.I)
    return term.strip()


ds_centres = read_centres()
ds_townlands = read_townlands()
comparers = [
    ds_centres,
    ds_townlands
]


def assemble_comparison(english_name, county, item):
    compare_result = {
        'query_english_name': english_name,
        'query_county': county,
        'item_english_name': item['English_Name'].upper(),
        'item_county': item['County'].upper(),
        'fullitem': item
    }
    compare_result['cdist'] = distance(
        compare_result['item_county'], compare_result['query_county']
    )
    compare_result['edist'] = distance(
        compare_result['item_english_name'],
        compare_result['query_english_name']
    )
    compare_result['equals'] = \
        compare_result['cdist'] < L_FACTOR and \
        compare_result['edist'] < L_FACTOR
    compare_result['exact'] = \
        not compare_result['cdist'] and not compare_result['edist']
    compare_result['distance'] = \
        compare_result['cdist'] + compare_result['edist']

    return compare_result


def base_filter(english_name, county, dataset):
    compare_result = map(
        lambda item: assemble_comparison(
            english_name,
            county,
            item
        ),
        dataset
    )
    filter_result = filter(
        lambda item: item['equals'],
        compare_result
    )
    sorted_result = sorted(
        filter_result,
        key=lambda item: item['distance']
    )
    return list(sorted_result)


def extract_prefered_addresses(filtereds):
    exact = list(
        filter(
            lambda item: item['exact'],
            filtereds
        )
    )
    if exact:
        return exact

    return filtereds


def geocode(query):
    query = query.split(',')
    query = [cleanup(item) for item in query]

    for i in reversed(range(len(query) - 1)):
        for dataset in comparers:

            base_filtereds = base_filter(query[i], query[-1], dataset)

            filtereds = extract_prefered_addresses(base_filtereds)

            if filtereds:

                return (query[i], query[-1]), [
                    {
                        'C': item['fullitem']['County'],
                        'E': item['fullitem']['English_Name'],
                        'ITM_E':item['fullitem']['ITM_E'],
                        'ITM_N':item['fullitem']['ITM_N'],
                        'GEO': itm2geo(
                            float(item['fullitem']['ITM_E']),
                            float(item['fullitem']['ITM_N'])
                        )
                    } for item in filtereds]

    return "", ""
