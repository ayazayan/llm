from typing import List


def below_zero(transactions: List[int]) -> bool:
    balance = 0
    for amount in transactions:
        balance += amount
        if balance < 0:
            return True
    return False