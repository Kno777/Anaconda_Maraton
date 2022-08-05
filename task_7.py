"""
Գրել ծրագիր, որը կհաշվի տրված զանգվածի արժեքների քառակուսիները և 
կպահի դրանք նոր զանգվածում՝ սորտավորված ձևով։
"""

def square(lst:list):
    sq = [x ** 2 for x in lst]
    sort_list = sorted(sq)
    return sort_list

print(square([12,33,4,55,6,7]))