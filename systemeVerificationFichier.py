#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""

?[Vérification fichiers]

* Algorithme verificationFichier($fichierRégulier):
    - SI: le $fichierRégulier est un SAM, alors
            - deplacementFichierRégulierValide($fichierRégulier)
            - Afficher("$fichierRégulier déplacé dans $fichiersValides, le format de $fichierRégulier est valide. Il sera utilisé pour la suite.")
    - SINON: 
            - ne rien faire

* Algorithme deplacementFichierrValide($fichierRégulier):
    - SI: le dossier $fichiersValides n'existe pas, alors
        - Créer un dossier $fichiersValides
        - Afficher ("Dossier $fichierValides non-existant, le dossier a donc été crée.)
    - SINON: 
        - Ne rien faire

    - Déplacer $fichierRégulier dans le dossier $fichiersValides

* Algorithme verificationDossier($dossier):
    - BOUCLE: Pour tout $fichierRégulier du $dossier, faire
        - verificationFichier($fichierRégulier)

"""

import os, shutil

def verificationFichier(fichierRegulier): 

    cheminCourrant = os.getcwd()
    cheminFichierRegulier = cheminCourrant+"/"+fichierRegulier

    if cheminFichierRegulier.endswith(".SAM") and os.path.isfile(cheminFichierRegulier):
        deplacementFichierValide(fichierRegulier)
        print("Le fichier {} est déplacé dans le dossier fichiersValides, le format est valide. Il sera utilisé pour la suite.".format(fichierRegulier))
    else:
        print("")

def deplacementFichierValide(fichierRegulier):
    
    if not os.path.isdir("fichiersValides"):
        os.makedirs("fichiersValides")         
        print("Dossier fichierValides non-existant, le dossier a donc été crée.")
    else: 
        print("")
        
    cheminCourrant = os.getcwd()
    cheminFichiersRegulier = cheminCourrant+"/"+fichierRegulier
    cheminDossierFichiersValides = cheminCourrant+"/"+"fichiersValides/"
    
    source = cheminFichiersRegulier
    destination = cheminDossierFichiersValides

    shutil.move(source,destination)


def verificationDossier():

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierRegulier in dossier:
        verificationFichier(fichierRegulier)

    os.chdir(cheminCourrant+"/"+"fichiersValides/")
    print(os.getcwd())