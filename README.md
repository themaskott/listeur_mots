## listeurDeMots

Compulse différentes sources afin de proposer une liste de mots qui puisse servir à un générateur de mots de passe.

## Utilisation

```
usage: listeurDeMots.py [-h] [-p PAGE] [-u URL] [-f FILE] [-t TEXTFILE] [-e EXTRACTURL] [-r] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  Page a chercher dans Wikipedia
  -u URL, --url URL     URL specifique a parser
  -f FILE, --file FILE  Fichier html specifique a parser
  -t TEXTFILE, --textFile TEXTFILE  Fichier texte a parser
  -e EXTRACTURL, --extractURL EXTRACTURL  Extrait les URL des contenus cibles et parse celles contenant un mot-clef
  -r, --reduce          Retire les mots les plus communs du resultat
  -v, --verbose         Mode verbose
```

-p :    recherche directement sur la page wikipedia de titre 'PAGE'
        utilise l'API de wikipedia

-u :    recherche sur une URL spécifiée

-f :    recherche les mots dans un fichier html

-t :    recherche les mots dans un fichier texte

-e :    extrait les urls présentes dans le site ciblé, et les parcours afin d'enrichir le resultat ( /!\ augemente le temps de traitement)
        ne retient que les urls contenant le mot clef spécifié en option (pour limiter le nombre de rebonds)

-r :    constitue une liste de mots courants pour les retirer du resultat et afiner sa pertinence


## Fichiers


| Nom | But |
|-----|-----|
| listeurDeMots.py | fichier principal, gestion des options et lancement des recherches spécifiées |
| fonctions.py | fonctions utilisées par le reste du programme |
| parseur.py | parse de l'HTML, en extrait le contenu ou les URL présentes |
| crawler.py | parcourt un ensemble d'URL |
| wikipedia.py | interaction avec l'API de wikipedia |
| reducteur.py | constitue une liste de mots courants pour les retirer du resultat final |



## Exemples d'utilisation

```
python3 listeurDeMots.py -p Thales
```
--> Requête simple sur l'API wikipedia

```
python3 listeurDeMots.py -p Commissariat_à_l\'énergie_atomique_et_aux_énergies_alternatives -r
```
--> Requête simple sur l'API wikipedia avec réduction des résultats

```
python3 listeurDeMots.py -u  https://fr.wikipedia.org/wiki/Thales -e Thales -r
```
--> Pourcours la page wikipedia de Thales, puis les urls présentes dans celle ci et contenant le mot clef 'Thales', et réduit le nombre de mots.

## Remaque

Les pages wikipedia contiennent souvent les liens vers ces mêmes pages dans d'autres langues.
Dans l'exemple ci-dessus, cela permet de récupérer des mots de langues étrangères.
