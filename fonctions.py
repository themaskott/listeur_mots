# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott


##################################################
# Import de librairies python                    #
##################################################

from urllib import parse
import os

##################################################
# Import de librairies personnelles              #
##################################################

from wikipedia import *
from parseur import *


##################################################
# Definition de constantes                       #
##################################################

# taille minimale des mots retenus
MIN_SIZE = 4

# taille maximale des mots retenus
MAX_SIZE = 30

# caracteres a retirer au debut et fin des mots
UNUSEDCHAR = " \"\'%&#{}()[]-|1234567890.,!§:/;?+*<>=@’\n\t\r"


##################################################
# Definition de fonctions                        #
##################################################

# genereMots
# generateur des mots contenus dans un fichier
# Entree : un descripteur de fichier ouvert en lecture
# Sortie : un iterrable
def genereMots( fichier ):
	"""
	Genere les mots contenus dans un fichier texte
	"""
	for line in fichier:
		for mot in line.split():
			if len(mot) < MAX_SIZE:
				yield mot

# sanitizeMots
# Recoit les mots d un generateur et les affiche apres nettoyage
# Entree : un iterrable de chaines de caracteres
# Sortie : un dictionnaire contenant les mots ( utilisation de set pour eliminer les doublons )
def sanitizeMots( generateur ):
	"""
	Parcours un generateur de mots et affiche ces derniers apres leur nettoyage
	"""
	mots = set()
	for mot in generateur:
		mot = mot.strip(UNUSEDCHAR).lower()
		mot = mot.replace("d’", "").replace("l’", "").replace("s’", "")
		mot = mot.replace("d'", "").replace("l'", "").replace("s'", "")
		mor = mot.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
		mot = mot.strip(UNUSEDCHAR)

		if mot.isalnum() and len( mot ) > MIN_SIZE :
			mots.add(mot)
	return mots


# motsFromWiki
# Entree : le titre d une page wikipedia a consulter (ex : 'Thales')
# Sortie : dictionnaire des mots contenus dans cette page
def motsFromWiki( WikiPage ):
	"""
	Interroge l API wikipedia pour recuperer le contenu d une page specifique
	Extrait le contenu de cette page pour en generer les mots
	"""
	mots = set()
	# ecrit dans un fichier tmp le retour du contenu de l API wikipedia au format HTML
	with open("tmp.txt", "w") as tmpFile:
		tmpFile.write( requestWikiApi( WikiPage ))

	# parse le HTML du retour precedent pour recuperer le contenu des champs
	with open("tmp.txt","r") as tmpFile:
		with open("tmp2.txt", "w") as tmpFile2:
			tmpFile2.write( extractDatasFromFile( tmpFile.read() , "content" ))
	
	# extrait les mots de ces contenus
	with open("tmp2.txt", "r") as tmpFile2:
		mots = sanitizeMots( genereMots( tmpFile2 ))

	os.remove("tmp.txt")
	os.remove("tmp2.txt")
	return mots


# motsFromURL
# Entree : l url du site cible
# Sortie : dictionnaire des des mots contenus dans cette page
def motsFromURL( url ):
	"""
	Interroge une page web quelconque pour en recuperer le contenu
	Genere les mots de ce contenu
	"""
	mots = set()
	
	with open("tmp.txt", "w") as tmpFile:
		tmpFile.write( extractDatasFromHTML( requestURL( url ), "content"))

	with open("tmp.txt","r") as tmpFile:
		mots = sanitizeMots(genereMots(tmpFile))

	os.remove("tmp.txt")
	return mots


# motsFromHTMLFile
# Entree : un nom de fichier contenant de l HTML
# Sortie : dictionnaire des mots contenus
def motsFromHTMLFile( fichier ):
	"""
	Parse un fichier HTML pour en extraire le contenu
	"""
	mots = set()
	# parse le HTML du fichier pour recuperer le contenu des champs
	with open( fichier, "r") as fileHTML:
		with open("tmp.txt", "w") as tmpFile:
			tmpFile.write( extractDatasFromFile( fileHTML.read() , "content" ))
	
	# extrait les mots de ces contenus
	with open("tmp.txt", "r") as tmpFile:
		mots = sanitizeMots( genereMots( tmpFile ))

	os.remove("tmp.txt")
	return mots