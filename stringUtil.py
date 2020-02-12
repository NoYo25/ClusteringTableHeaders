# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:17:07 2019

@author: Nora
"""
import inflection
import re
from difflib import SequenceMatcher


#TODO: get ride of this it is a bugy one instead use the inflection library, inflection library is used in semantic feature extractor
def to_snake_case(word):
    word = word.replace("_", "")
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def find_longest_substring(string1, string2):
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))
    return string1[match.a: match.a + match.size].replace('_', '')

def getWords(word):
    w = unifyWord(word)
    w = w.replace('_', ' ')
    return w.title()

def unifyWord(word):
        new_word = word.replace(" ", "_").replace(".", "_")
        new_word = inflection.underscore(new_word)
        return new_word

if __name__ == '__main__':
    w = "HelloWorld"
    print(to_snake_case(w))

    str1 = "Surname"
    str2 = "Author_Surname"
    print(find_longest_substring(str1, str2))

    x = getWords("firstAuthor_Name")
    print(x)
