# solution 1
def dig_pow(n, p):
    total = 0
    for power, digit in enumerate(str(n), p):
        total += int(digit)**power
    if total % n == 0:
        return total // n
    return -1


# solution 2
# exactement la même idée
# mais dans un Python un peu plus savant / pédant
def dig_pow(n, p):
    # une expression génératrice
    total = sum(int(digit)**power
                for power, digit in enumerate(str(n), p))
    # une expression conditionnelle
    return total //n if total % n == 0 else -1
