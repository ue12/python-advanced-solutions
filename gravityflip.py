def flip(d, a):
    # parentheses not required, but clearer
    reverse = (d == 'L')
    return sorted(a, reverse=reverse)
