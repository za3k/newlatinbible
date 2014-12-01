#!/bin/python3
import sys,re

def piglatin_lowercase_word(word, cons=re.compile('''(?P<first>[bcdfghjklmnpqrstvwxz]+)(?P<rest>.+)'''), vowel=re.compile('''[aeiouy].*''')):
    m = cons.match(word)
    if m:
       return m.group('rest') + m.group('first') + 'ay'
    m = vowel.match(word)
    if m:
       return word + 'way'
    return word

def piglatin_word(word):
    c = get_capitalization(word)
    w = piglatin_lowercase_word(word.lower())
    return c(w)

def piglatin_token(token):
    word = extract_word(token)
    if word:
        return token.replace(word, piglatin_word(word))
    else:
        return token

def get_capitalization(token):
    types = [
        lambda w: w.title(),
        lambda w: w.upper(),
        lambda w: w.lower()
    ]
    default_capitalization = lambda w: w
    for t in types:
        if (t(token) == token):
            return t
    return default_capitalization

def extract_word(token, largest_word=re.compile('''[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+''')):
    m = largest_word.match(token)
    if m:
        return m.group(0)

def piglatin_line(line):
    return " ".join(map(piglatin_token, line.rstrip('\n').split()))

for line in sys.stdin:
    print(piglatin_line(line))
