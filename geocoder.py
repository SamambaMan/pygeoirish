import sys
import argparse
sys.path.append("./src")

from collections import Counter
from pygeoirish import geocode, serve


def exploratory():
    result_stats = []
    with open('addresses_for_task.csv') as file:
        for line in file.readlines():
            line = line.strip()
            if not line:
                continue
            result = geocode(line)
            result_stats += [len(result)]
            print('%s | %s | %s' % (line, len(result), result))

    print(Counter(result_stats))


F_MAP = {
    'serve': serve,
    'geocode': geocode
}


parser = argparse.ArgumentParser(
    description='Irish Geocoder',
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument(
    '--serve',
    action='store_true',
    default=False,
    help="HTTP server for geocoding"
)
parser.add_argument(
    '--geocodeall',
    action='store_true',
    default=False,
    help="geocode an entire address file to the standard output"
)
parser.add_argument(
    '--geocode',
    action='store',
    type=str,
    nargs='+',
    help="Commando line geocoder"
)

args = parser.parse_args()

if args.geocode:
    print(geocode(' '.join(args.geocode)))
if args.serve:
    serve()
if args.geocodeall:
    exploratory()
