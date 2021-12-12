#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
#* Algorithme verificationFichier():
    - fonction : Vérifie si un fichierRegulier est un fichier SAM
    - paramètres : Nécessite un fichierRegulier

#* Algorithme deplacementFichierValide():
    - fonction : Déplace un fichierRegulier vers le répertoire fichierValide/
    - paramètres : Nécessite un fichierRegulier

#* Algorithme verificationDossier():
    - fonction : Pour tout fichierRegulier SAM d'un dossier le déplace vers le répertoire fichierValide/
    - paramètres : AUCUN

#* Le programme s'éxecute dans un terminal, et le fichier du programme doit être dans le dossier contenant les fichiers
"""

import os, shutil

def verificationFichier(fichierRegulier): #! on vérifie si le fichier est un fichier SAM

    cheminCourrant = os.getcwd()
    cheminFichierRegulier = cheminCourrant+"/"+fichierRegulier

    if cheminFichierRegulier.endswith(".sam") and os.path.isfile(cheminFichierRegulier):
        deplacementFichierValide(fichierRegulier)
        print("Le fichier {} est déplacé dans le dossier fichiersValides, le format est valide. Il sera utilisé pour la suite.".format(fichierRegulier))

def deplacementFichierValide(fichierRegulier):
        
    cheminCourrant = os.getcwd()
    cheminFichiersRegulier = cheminCourrant+"/"+fichierRegulier
    cheminDossierFichiersValides = cheminCourrant+"/"+"fichiersValides/"
    
    source = cheminFichiersRegulier
    destination = cheminDossierFichiersValides

    shutil.move(source,destination)


def verificationDossier():

    if not os.path.isdir("fichiersValides"):
        os.makedirs("fichiersValides")         
        print("Dossier fichierValides non-existant, le dossier a donc été crée.")

    print("\nLe vérification des fichiers s'effectue, patientez...\n")

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierRegulier in dossier:
        verificationFichier(fichierRegulier)
    
    print("\nLa vérification est terminée.\n")

    os.chdir(cheminCourrant+"/"+"fichiersValides/")
    print("Changement de dossier, on est dans le dossier : {}\n".format(os.getcwd()))

verificationDossier()