"""
Իրականացնել ֆունկցիա, որը կհեռացնի ստացված տողի (string) ամեն երրորդ սիմվոլը։
"""

def remove_smybol(line:str):
    new_str = ""
    for char in range(1, len(line), 2):
        new_str += line[char]
    return f"This is my new test '{new_str}' and this old text '{line}'"

print(remove_smybol("armenia"))