"""
Տեքստային ֆայլի համար իրականացնել ծրագիր, 
որը կհաշվի ֆայլում հանդիպող սիմվոլների քանակը
"""

from collections import Counter

def file_symbol_count(file_name):
    f = open(file_name, 'r')
    text = open(file_name)
    count_smb = Counter(f.read())
    f.close()
    return f"This is my text \n{text.read()} \tand count smybol \n{count_smb}"
        
print(file_symbol_count('task_4.txt'))