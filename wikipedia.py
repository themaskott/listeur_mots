# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott



##################################################
# Import de librairies python                    #
##################################################

from urllib import request, parse
import certifi, json



##################################################
# Definition de fonctions                        #
##################################################

# requestWikiApi
# effectue une requete sur l API de wikipedia
# le retour peut etre utilise au format JSON
# necessite de recuperer le pageID pour acceder au champ du contenu
# Entree : mot clef titre de la page wikipedia
# Sortie : le contenu de la page correspondante

def requestWikiApi( motClef ):
    """
    Interaction avec l API de wikipedia
    """
    # Nettoayge du mot clef / ex: Commissariat_à_l'énergie_atomique_et_aux_énergies_alternatives --> Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives
    motClef = parse.quote( motClef )

    # recuperation du 'pageId' de wikipedia
    req = request.Request( "https://fr.wikipedia.org/w/api.php?action=query&prop=iwlinks&utf8&iwprefix=en&format=json&indexpageids&titles=" + motClef )
    resp = request.urlopen( req, cafile=certifi.where() )
    respData = json.loads( resp.read().decode("utf-8") )
    resp.close()

    pageId = respData["query"]["pageids"][0]

    # requete sur le contenu de la page

    req = request.Request( "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles=" + motClef )
    resp = request.urlopen( req, cafile=certifi.where() )
    respData = json.loads( resp.read().decode("utf-8") )
    resp.close()
    return respData["query"]["pages"][pageId]["extract"]
    
