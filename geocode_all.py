import sys
sys.path.append("./src")

from collections import Counter
from pygeoirish import geocode

result_stats = []


def process(line):
    line = line.strip()
    if line:
        return line, *geocode(line)
    return "", "", ""


with open('addresses_for_task.csv') as file:
    for line, base, result in map(process, file.readlines()):
        if not line:
            continue
        result_stats += [len(result)]
        print('%s | %s | %s | %s' % (line, len(result), base, result))


print(Counter(result_stats))
