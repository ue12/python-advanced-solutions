
##################################################
# compare_all
##################################################
def compare_all(fun1, fun2, entrees):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si fun1(entree) == fun2(entree)
    """
    # on vérifie pour chaque entrée si f et g retournent
    # des résultats égaux avec ==
    # et on assemble le tout avec une comprehension de liste
    return [fun1(entree) == fun2(entree) for entree in entrees]

