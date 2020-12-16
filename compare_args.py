
##################################################
# compare_args
##################################################
def compare_args(fun1, fun2, arg_tuples):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si fun1(*tuple) == fun2(*tuple)
    """
    # c'est presque exactement comme compare_all, sauf qu'on s'attend
    # à recevoir une liste de tuples d'arguments, qu'on applique
    # aux deux fonctions avec la forme * au lieu de les passer directement
    return [fun1(*arg) == fun2(*arg) for arg in arg_tuples]

