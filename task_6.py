"""
Իրականացնել ծրագիր, որը կհաշվի թե յուրաքանչյուր 
բառ քանի անգամ է հանդիպում տեքստային ֆայլում։
"""
from collections import Counter

def word_count_in_file(file_name):
    f = open(file_name, 'r')
    word = f.read()
    word = word.replace('\n', '')
    word = word.split(' ')
    count_word = Counter(word)
    return count_word
    
print(word_count_in_file('task_6.txt'))