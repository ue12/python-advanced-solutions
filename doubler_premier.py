
##################################################
# doubler_premier
##################################################
def doubler_premier(func, first, *args):
    """
    renvoie le résultat de la fonction f appliquée sur
    func(2 * first, *args)
    """
    # une fois qu'on a écrit la signature on a presque fini le travail
    # en effet on a isolé la fonction, son premier argument, et le reste
    # des arguments
    # il ne reste qu'à appeler func, en doublant first
    return func(2*first, *args)


##################################################
# doubler_premier_bis
##################################################
def doubler_premier_bis(func, *args):
    """
    marche aussi mais moins élégant
    """
    first, *remains = args
    return func(2*first, *remains)


##################################################
# doubler_premier_ter
##################################################
def doubler_premier_ter(func, *args):
    """
    ou encore comme ça, mais
    c'est carrément moche
    """
    first = args[0]
    remains = args[1:]
    return func(2*first, *remains)

