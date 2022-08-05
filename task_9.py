"""
Հաշվել տրված թվի թվանշանների արտադրյալի և գումարի տարբերությունը։
Օրինակ, տրված է 4637, վերադարձնել (4*6*3*7) - (4+6+3+7):
"""

def sum_and_mul_avg(num):
    summer = 0
    muller = 1
    while num != 0:
        tmp = num
        summer += num % 10
        muller *= tmp % 10
        num //= 10
    return f'{summer} - {muller} = {muller - summer}'

print(sum_and_mul_avg(1234))