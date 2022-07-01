import math
import urllib
from urllib.parse import urlparse


def netloc_parse(netloc: str) -> str:
    if netloc.split('.')[0] == 'www':
        return str(netloc.split('.')[1])
    return str(netloc.split('.')[0])


# TODO:
# https://colab.research.google.com/drive/
# https://university.ylab.site/python/lecture-1-hw/
def domain_name(url: str) -> str:
    if url != '':
        netloc = urllib.parse.urlsplit(url).netloc
        if netloc == '':
            netloc = urllib.parse.urlsplit('//' + url).netloc  # Add prefix
        return netloc_parse(netloc)


def int32_to_ip(ipnum: int) -> str:
    """Based on https://stackoverflow.com/questions/5619685/conversion-from-ip-string-to-integer-and-backward-in-python"""
    o1 = int(ipnum / 16777216) % 256
    o2 = int(ipnum / 65536) % 256
    o3 = int(ipnum / 256) % 256
    o4 = int(ipnum) % 256
    return f'{o1}.{o2}.{o3}.{o4}'


def zeros(n: int) -> int:
    if 0 == n:
        return 0
    k_max = math.log(n, 5)
    z = [int(n/5**k) for k in range(1, int(k_max)+1)]
    return sum(z)


def bananas(s: str, word: str = 'banana') -> set:
    pos_word = []
    word_count = 0
    for cnt, i in enumerate(s):
        if i == word[word_count]:
            pos_word.append([cnt])
    while True:
        word_count += 1
        if word_count == len(word):
            break
        new_pos_word = []
        for el in pos_word:
            for cnt, i in enumerate(s[el[-1]:]):
                if i == word[word_count]:
                    new_pos_word.append(el + [el[-1] + cnt])
        pos_word = new_pos_word
    result = []
    for pos in pos_word:
        string = ''
        for cnt, i in enumerate(s):
            if cnt in pos:
                string += i
            else:
                string += '-'
        result.append(string)
    return set(result)


def count_find_num(primesL: list, limit: int) -> list:
    product = math.prod(primesL)
    if limit < product:
        return []
    elif limit / product < 2:
        return [1, product]
    else:
        result = [product]
        index_start = 0
        quit_while = 1
        while quit_while:
            add_result = []
            quit_while = 0
            for prod in result[index_start:]:
                for i in primesL:
                    if prod * i <= limit:
                        add_result.append(prod * i)
                        quit_while += 1
            index_start = len(result)
            result += add_result
    return [len(set(result)), max(result)]


# Task 1
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"

# Task 2
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

# Task 3
assert zeros(0) == 0
assert zeros(1) == 0
assert zeros(6) == 1
assert zeros(10) == 2
assert zeros(16) == 3
assert zeros(30) == 7

# Task 4
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

# Task 5
primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 480
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []

primesL = [2, 3, 5]
limit = 30
assert count_find_num(primesL, limit) == [1, 30]

primesL = [2, 3, 5]
limit = 59
assert count_find_num(primesL, limit) == [1, 30]

primesL = [2, 3, 5]
limit = 60
assert count_find_num(primesL, limit) == [2, 60]
