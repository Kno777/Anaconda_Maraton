"""
Իրականացնել strmove() ֆունկցիան, որը տրված տողը ցիկլիկ տեղաշարժում է դեպի աջ տրված քանակով։ 
Օրինակ, strmove(“hello”, 2); կտեղաշարժի “hello”-ն 2 դիրքով դեպի աջ և կստանա “lohel”:
"""

def leftmove(line, key):
    return line[key : ] + line[0 : key]

def rightmove(line, key):
    return leftmove(line, len(line) - key)

print(rightmove("hello", 2))
print(leftmove("hello", 4))