#!/usr/bin/env python3

# ESIEA MS-SIS
# PROJET python - listeurDeMots
# 29/10/2021
# @Maskott


##################################################
# Import de librairies python                    #
##################################################

import argparse
from collections import Counter


##################################################
# Import de librairies personnelles              #
##################################################

from fonctions import *
from crawler import *
from parseur import *
from wikipedia import *
from reducteur import *


##################################################
# Fonctions                                      #
##################################################

# getArgPArseur
# utilisation de argparse pour recupere les arguments au lancement du programme
def getArgParseur( ):
	"""
	Gestion des arguments passes en ligne de commande
	"""
	argparseur = argparse.ArgumentParser( add_help=True )
	argparseur.add_argument( "-p", "--page", help="Page a chercher dans Wikipedia" )
	argparseur.add_argument( "-u", "--url", help="URL specifique a parser" )
	argparseur.add_argument( "-f", "--file", help="Fichier html specifique a parser" )
	argparseur.add_argument( "-t", "--textFile", help="Fichier texte a parser" )
	argparseur.add_argument( "-e", "--extractURL", help="Extrait les URL des contenus cibles et parse celles contenant un mot-clef" )
	argparseur.add_argument( "-r", "--reduce", help="Retire les mots les plus communs du resultat", action="store_true" )
	argparseur.add_argument( "-v", "--verbose", help="Mode verbose", action="store_true" )


	return argparseur


##################################################
# Fonction principale                            #
##################################################

def main( args ):
	"""
	listeurDeMots recupere des mots d interets depuis plusieurs sources (wikipedia, site internet, fichiers)
	et en affiche la liste afin de preparer un dictionnaire de mots de passe
	"""

	# set des mots qui seront retenus
	setMots = set()
	motsCommuns = Counter()


	# recherche sur wikipedia
	if ( args.page ):
		if ( args.verbose ): 
			print("[+] Recherche de '{0}' dans Wikipedia".format( args.page ) )
		setMots.update(	motsFromWiki( args.page ) )

	# traite une url specifique
	if ( args.url ):
		if ( args.verbose ): 
			print("[+] Recherche de '{0}' ".format( args.url ) )
		setMots.update( motsFromURL( args.url ) )

	# extrait les mots d un fichier au format HTML
	if ( args.file ):
		if ( args.verbose ): 
			print("[+] Ouverture de '{0}' ", args.file )
		setMots.update( motsFromHTMLFile( args.file ))

	# extrait les mots d un fichier texte simple
	if ( args.textFile ):
		if ( args.verbose ): 
			print("[+] Ouverture de '{0}' ", args.textFile )
		with open( args.textFile ) as f:
			setMots.update( afficheMots( genereMots( f )))

	# recherche des urls
	if ( args.extractURL ):
		with open("saveURL.txt", "w") as fout:
			if ( args.page ):
				fout.write( extractDatasFromFile( requestWikiApi( args.page ), "url"))
			if ( args.url ):
				fout.write( extractDatasFromHTML( requestURL( args.url ), "url") )
			if ( args.file ):
				with open( args.file ) as fin:
					fout.write( extractDatasFromFile ( fin.read(), "url" ))
		# parse les urls precedement extraites et met a jour le dictionnaire de mots
		setMots.update( crawlURL( args.extractURL ) )


	# prepare un dictionnaire (Counter) de mots communs
	if ( args.reduce ):
		if ( args.verbose ): 
			print("[+] Constitution du dictionnaire des mots courants")
		motsCommuns = searchMostCommons()


	# affichage sous forme de dictionnaire
	if ( args.verbose ):
		 print(setMots)
	else :
	# affichage des mots
		for mot in setMots:
			# n affiche pas les mots presents plus de 3 fois dans motsCommuns
			# si l option n a pas ete demandee, motsCommuns est vide, motsCommun[mot] == 0, tous les mots sont affiches
			if motsCommuns[mot] > 3:
				pass
			else:
				print(mot)


if __name__ == "__main__":
	args = getArgParseur().parse_args()
	main( args )