"""
Տրված ֆայլում պարունակվում է տեքստ։ 
Իրականացնել ծրագիր, որը ֆայլի մեջ պարունակվող տեքստի բոլոր բառերի առաջին 
տառերը դարձնում է մեծատառ և ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։
"""

def file_capitalize(file_name):
    f = open(file_name, 'r')
    other_file = open('task_2_new.txt', 'w')
    for char in f.readlines():
        char = char.replace('\n', ' ')
        other_file.write(char.capitalize())
    f.close()
    
file_capitalize('task_2.txt')
