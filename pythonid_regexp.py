
##################################################
# pythonid_regexp
##################################################
# un identificateur commence par une lettre ou un underscore
# et peut être suivi par n'importe quel nombre de
# lettre, chiffre ou underscore, ce qui se trouve être \w
# si on ne se met pas en mode unicode
pythonid = r"[a-zA-Z_]\w*"


##################################################
# pythonid_bis
##################################################
# on peut aussi bien sûr l'écrire en clair
pythonid_bis = r"[a-zA-Z_][a-zA-Z0-9_]*"

