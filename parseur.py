# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott




##################################################
# Import de librairies python                    #
##################################################

from urllib import request, parse
from html.parser import HTMLParser
import certifi


##################################################
# Definition de classes                          #
##################################################

class Crawler( HTMLParser ):

    def __init__(self):
        super(Crawler, self).__init__()
        self.reset()
        self.contenu = ""
        self.urllinks = ""

    # recupere les liens contenus dans la page
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, link in attrs:
                if name == "href" and link.startswith("http"):
                    self.urllinks += link + "\n"
  
    # recupere le contenu des champs de la page
    def handle_data(self, contenu):
        self.contenu += contenu


##################################################
# Definition de fonctions                        #
##################################################

def requestURL( url ):
    """
    Effectue une requete simple sur une URL et renvoie le contenu de la page
    """
    # prepare l url en encodant les caractere non ascii de l uri
    methode = url.split("//")[0]
    uri = url.split("//")[1]
    urlPropre = methode + "//" + parse.quote( uri )
    req = request.Request( urlPropre )
    resp = request.urlopen( req, cafile=certifi.where() )     
    respData = resp.read()
    resp.close()
    return respData 


def extractDatasFromHTML( pageHTML, datas ):
    """
    Utilise une classe HTMLPaser pour extraire soit le contenu de la page soit les liens HTML de la page
    """
    parseur = Crawler()
    parseur.feed( pageHTML.decode("utf-8", "ignore") )
    if datas == "url":
        return parseur.urllinks
    if datas == "content":
        return parseur.contenu

def extractDatasFromFile( pageHTML, datas ):
    """
    Utilise une classe HTMLPaser pour extraire soit le contenu de la page soit les liens HTML de la page
    Recoit en entree un fichier dont le contenu est au format HTML
    """
    parseur = Crawler()
    parseur.feed( pageHTML )
    if datas == "url":
        return parseur.urllinks
    if datas == "content":
        return parseur.contenu