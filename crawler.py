# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott


##################################################
# Import de librairies python                    #
##################################################



##################################################
# Import de librairies personnelles              #
##################################################

from fonctions import *



##################################################
# Definition de fonctions                        #
##################################################


# crawURL
# Entree : mot clef en lien avec la cible
# Sorti : dictionnaire des mots trouves
def crawlURL( motClef ):
    """
    Ouvre le fichier saveURL.txt contenant les urls precedement recuperees
    Parse ces urls pour mettre a jour le dictionnaire de mots
    Pour limiter le nombre d url parsees il ne parcourt que celles contenant un mot clef
    """
    with open("saveURL.txt", "r") as fin:
        mots = set()
        for url in fin:        
            if motClef.lower() in url.lower():
                # utilisation du try pour passer les url inactives ou bad requests
                try:
                    mots.update( motsFromURL ( url ))
                except:
                    pass
        return mots