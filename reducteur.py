# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott


##################################################
# Import de librairies personnelles              #
##################################################

from fonctions import *
from collections import Counter


##################################################
# Definition de fonctions                        #
##################################################


# crawURL
# Entree : 
# Sorti : 
def searchMostCommons(  ):
    """
    A partir de quelques pages wikipedia, etablit la liste des mots les plus utilises
    """
    urls = [ "https://fr.wikipedia.org/wiki/Histoire_de_France" ,
            "https://fr.wikipedia.org/wiki/Histoire_des_mathématiques" ,
            "https://fr.wikipedia.org/wiki/Histoire_du_vol_spatial" ,
            "https://fr.wikipedia.org/wiki/Linux",
            "https://fr.wikipedia.org/wiki/Python_(langage)" ]

    mots = Counter()
    for url in urls:      
        try:
            mots.update( motsFromURL ( url ))
        except:
            pass
    return mots