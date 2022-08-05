"""
Օգտագործելով աղյուսակ (dictionary) 
հաշվել զանգվածում բոլոր թվերի կրկնությունների քանակը
"""
from collections import Counter

def number_count(lst:list):
    count_number = Counter(lst)
    return f"This is my list {lst} and count elem {count_number}"

print(number_count([1,2,1,4,5,2,5,6]))
    