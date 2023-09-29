import time
import random
import string
import timeit


def random_string(l):
    return ["".join(random.choices(string.digits, k=8)) for _ in range(l)]


def random_tuple(l):
    return [
        (random.uniform(0.0, 999999.9), "".join(random.choices(string.digits, k=8)))
        for _ in range(l)
    ]


ALL = 10_000

eligible_zones = random_string(ALL)
neighbors_ids = random_string(ALL)


def la():
    return list(filter(lambda x: x in neighbors_ids, eligible_zones))


def fo():
    return [x for x in neighbors_ids if x in eligible_zones]


print(f"--- {timeit.timeit(la, number=100)} ---")
print(f"--- {timeit.timeit(fo, number=100)} ---")
