def below_zero(ops: list[int]) -> bool:
    balance = 0
    for op in ops:
        balance += op
        if balance < 0:
            return True
    return False