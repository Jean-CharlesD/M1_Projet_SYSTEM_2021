#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""

?[Extraction des mauvais reads]

* Algorithme purificationFichier($fichierParsé): $fichierPurifié
    - BOUCLE: Pour chaque $read du $fichierParsé, faire
        - SI: le $read est non-mappés, alors
            - Extraire le $read
        - SINON SI: le $read est partiellement mappés, alors
            - Extraire le $read
        - SINON SI: le $read est en paire ET l'un des $read de la paire est non-mappés, alors
            - Extraire le $read
        - SINON SI: le $read est en paire ET l'un des $read de la paire est partiellement mappés, alors
            - Extraire le $read
        - SINON: ne rien faire

    - Résultat: $fichierPurifié

    - RETOURNER $fichierPurifié

* Algorithme deplacementRésultatPurification($fichierPurifié):
    - SI: le dossier $RésultatPurification n'existe pas, alors
        - Créer un dossier $RésultatPurification
        - Afficher ("Dossier $RésultatPurification non-existant, le dossier a donc été crée.)
    - SINON: 
        - Ne rien faire

    - Déplacer $fichierPurifié dans le dossier $RésultatPurification

* Algorithme purificationDossier($résultatParsing):
    - BOUCLE: pour chaque $fichierParsé du dossier $résultatParsing, faire 
        - deplacementRésultatPurification(purificationFichier($fichierParsé): $fichierPurifié):

"""
import os, shutil

def purificationFichier(fichierParse):#! on obtient fichierPurifie


def deplacementResultatPurification(fichierPurifie):

    if not os.path.isdir("ResultatPurification"):
        os.makedirs("ResultatPurification")         
        print("Dossier ResultatPurification non-existant, le dossier a donc été crée.")
    else: 
        print("")

    cheminCourrant = os.getcwd()
    cheminfichierPurifie = cheminCourrant+"/"+fichierPurifie
    cheminDossierResultatPurification = cheminCourrant+"/"+"ResultatPurification/"
    
    source = cheminfichierPurifie
    destination = cheminDossierResultatPurification

    shutil.move(source,destination)

def purificationDossier():

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierParse in dossier:
        deplacementResultatPurification(purificationFichier(fichierParse))

    os.chdir(cheminCourrant+"/"+"RésultatPurification/")
    print(os.getcwd())