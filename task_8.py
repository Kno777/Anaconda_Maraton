"""
Հաշվել տրված թվի թվանշանների գումարը։ Օրինակ, տրված է 4637, վերադարձնել 4+6+3+7:
"""

def number_sum(value):
    summer = 0
    while value != 0:
        summer += value % 10
        value //= 10
    return summer

print(number_sum(123))