from itertools import combinations

def solve(n, k):
    text = str(n)
    # comme text est un itérable on peut lui appliquer
    # directement combinations (pas besoin de faire une liste)
    # et on peut comparer directement les tuples produits par combinations
    # il ne reste plus qu'à refaire une chaine à partir du tuple qui gagne
    return "".join(min(combinations(text, len(text)-k)))

