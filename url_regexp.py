
##################################################
# url_regexp
##################################################
# en ignorant la casse on pourra ne mentionner les noms de protocoles
# qu'en minuscules
i_flag = "(?i)"

# pour élaborer la chaine (proto1|proto2|...)
protos_list = ['http', 'https', 'ftp', 'ssh', ]
protos      = "(?P<proto>" + "|".join(protos_list) + ")"

# à l'intérieur de la zone 'user/password', la partie
# password est optionnelle - mais on ne veut pas le ':' dans
# le groupe 'password' - il nous faut deux groupes
password    = r"(:(?P<password>[^:]+))?"

# la partie user-password elle-même est optionnelle
# on utilise ici un raw f-string avec le préfixe rf
# pour insérer la regexp <password> dans la regexp <user>
user        = rf"((?P<user>\w+){password}@)?"

# pour le hostname on accepte des lettres, chiffres, underscore et '.'
# attention à backslaher . car sinon ceci va matcher tout y compris /
hostname    = r"(?P<hostname>[\w\.]+)"

# le port est optionnel
port        = r"(:(?P<port>\d+))?"

# après le premier slash
path        = r"(?P<path>.*)"

# on assemble le tout
url = i_flag + protos + "://" + user + hostname + port + '/' + path


##################################################
# url_bis
##################################################
# merci à sizeof qui a pointé l'utilisation de re.X
# https://docs.python.org/fr/3/library/re.html#re.X
# ce qui donne une présentation beaucoup plus compacte

protos_list = ['http', 'https', 'ftp', 'ssh', ]

url_bis = rf"""(?x)                    # verbose mode
    (?i)                               # ignore case
    (?P<proto>{"|".join(protos_list)}) # http|https|...
    ://                                # separator
    ((?P<user>\w+){password}@)?        # optional user/password
    (?P<hostname>[\w\.]+)              # mandatory hostname
    (:(?P<port>\d+))?                  # optional port
    /(?P<path>.*)                      # mandatory path
"""

