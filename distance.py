
##################################################
# distance
##################################################
import math

def distance(*args):
    """
    La racine de la somme des carrés des arguments
    """
    # avec une compréhension on calcule
    # la liste des carrés des arguments
    # on applique ensuite sum pour en faire la somme
    # vous pourrez d'ailleurs vérifier que sum ([]) = 0
    # enfin on extrait la racine avec math.sqrt
    return math.sqrt(sum([x**2 for x in args]))


##################################################
# distance_bis
##################################################
def distance_bis(*args):
    """
    Idem mais avec une expression génératrice
    """
    # on n'a pas encore vu cette forme - cf Semaine 5
    # mais pour vous donner un avant-goût d'une expression
    # génératrice:
    # on peut faire aussi comme ceci
    # observez l'absence de crochets []
    # la différence c'est juste qu'on ne
    # construit pas la liste des carrés,
    # car on n'en a pas besoin
    # et donc un itérateur nous suffit
    return math.sqrt(sum(x**2 for x in args))

