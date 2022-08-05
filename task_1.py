"""
Տրված ֆայլում պարունակվում են թվեր։ 
Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը։
"""

def file_numbers_sum(file):
    file_open = open(file, 'r')
    summer = 0
    for val in file_open.readlines():
        summer += int(val)
    file_open.close()
    return f"Numbers sum = {summer}"


print(file_numbers_sum('task_1.txt'))