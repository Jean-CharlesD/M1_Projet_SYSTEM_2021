#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
?[Parsing de fichiers]

* Algorithme parsingFichier($fichierRégulier): $fichierParsé
    - Parsing $fichierRégulier

    - Résultat = $fichierParsé

    - RETOURNER $fichierParsé

* Algorithme deplacementRésultatParsing($fichierParsé):
    - SI: le dossier $résultatParsing n'existe pas, alors
        - Créer un dossier $résultatParsing
        - Afficher ("Dossier $résultatParsing non-existant, le dossier a donc été crée.)
    - SINON: 
        - Ne rien faire

    - Déplacer $fichierParsé dans le dossier $résultatParsing

* Algorithme parsingDossier($fichierRégulier):
    - BOUCLE: Pour chaque $fichierRégulier du dossier $fichierValide, faire
        - deplacementRésultatParsing($parsingFichier($fichierRégulier): $fichierParsé)

"""
import os, shutil

def parsingFichier(fichierRegulier): #! on obtient fichierParse


def deplacementResultatParsing(fichierParse):

    if not os.path.isdir("resultatParsing"):
        os.makedirs("resultatParsing")         
        print("Dossier resultatParsing non-existant, le dossier a donc été crée.")
    else: 
        print("")

    cheminCourrant = os.getcwd()
    cheminfichierParse = cheminCourrant+"/"+fichierParse
    cheminDossierResultatParsing = cheminCourrant+"/"+"resultatParsing/"
    
    source = cheminfichierParse
    destination = cheminDossierResultatParsing

    shutil.move(source,destination)

def parsingDossier():

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierRegulier in dossier:
        deplacementResultatParsing(parsingFichier(fichierRegulier))

    os.chdir(cheminCourrant+"/"+"résultatParsing/")
    print(os.getcwd())