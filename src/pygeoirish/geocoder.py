import csv
import re
from Levenshtein import distance
from .itm2utm import itm2geo
from operator import eq


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


def lcomp(word, another_word):
    return distance(word, another_word) < L_FACTOR


ds_centres = read_centres()
ds_townlands = read_townlands()
comparers = [
    {'ds': ds_centres, 'comp': eq},
    {'ds': ds_townlands, 'comp': eq},
    {'ds': ds_centres, 'comp': lcomp},
    {'ds': ds_townlands, 'comp': lcomp},
]


def cleanup(term):
    term = term.upper()
    term = term.strip()
    terms = r"[^a-zA-Z0-9,]|^CO "
    term = re.sub(terms, ' ', term, flags=re.I)
    return term.strip()


def base_filter(english_name, county, dataset, comp=eq):
    return list(
        filter(
            lambda item:
            comp(
                county,
                item['County'].upper()
            ) and comp(english_name, item['English_Name'].upper()),
            dataset)
    )


def geocode(query):
    query = query.split(',')
    query = [cleanup(item) for item in query]

    for i in reversed(range(len(query) - 1)):
        for comparer in comparers:
            dataset = comparer['ds']
            comp = comparer['comp']

            filtereds = base_filter(query[i], query[-1], dataset, comp)

            if filtereds:
                return (query[i], query[-1]), [
                    {
                        'C': item['County'],
                        'E': item['English_Name'],
                        'ITM_E':item['ITM_E'],
                        'ITM_N':item['ITM_N'],
                        'GEO': itm2geo(
                            float(item['ITM_E']),
                            float(item['ITM_N'])
                        )
                    } for item in filtereds]

    return "", ""
