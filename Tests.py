from itertools import groupby

def remove_consecutive_duplicates(s):
    return print(' '.join(k for k,_ in groupby(s.split())))


def uni_total(string):
    return sum(map(ord, string))

print(uni_total('adsaasd'))
remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')