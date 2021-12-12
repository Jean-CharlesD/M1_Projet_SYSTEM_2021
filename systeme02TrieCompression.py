#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
#* Algorithme trieCompression():
    - fonction : Donne un fichierTC à partir d'un fichierRegulier
    - paramètres : Nécessite un fichierRegulier

#* Algorithme deplacementResultatTC():
    - fonction : Déplace un fichierTC vers le répertoire resultatTC/
    - paramètres : Nécessite un fichierTC

#* Algorithme trieCompressionDossier():
    - fonction : Pour tout fichierRegulier d'un dossier,donne un fichierTC puis le déplace vers le répertoire resultatTC/
    - paramètres : AUCUN

#* Le programme s'éxecute dans un terminal, et le fichier du programme doit être dans le dossier contenant les fichiers
"""

import os, shutil, pysam

def trieCompression(fichierRegulier): #! on un obtient fichierTC
                                      #! samtools sort -o <fichier de sortie> <fichier d'entrée>

    a = "{}[sorted].bam".format(fichierRegulier)
    b = "{}".format(fichierRegulier)
    c = "-o"
    pysam.sort(c, a, b) 

def deplacementResultatTC(fichierTC):
    
    cheminCourrant = os.getcwd()
    cheminfichierTC = cheminCourrant+"/"+fichierTC
    cheminDossierResultatTC = cheminCourrant+"/"+"resultatTC/"
    
    source = cheminfichierTC
    destination = cheminDossierResultatTC

    shutil.move(source,destination)

def trieCompressionDossier():

    if not os.path.isdir("resultatTC"):
        os.makedirs("resultatTC")         
        print("Dossier resultatTC non-existant, le dossier a donc été crée.")

    print("\nLe trie + la compression s'effectuent, patientez...")

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierRegulier in dossier:
        if fichierRegulier.endswith(".sam") and os.path.isfile(fichierRegulier):
            trieCompression(fichierRegulier)
    
    dossierReload01 = os.listdir(cheminCourrant)

    for fichierTC in dossierReload01:
        if fichierTC.endswith("[sorted].bam") and os.path.isfile(fichierTC):
            deplacementResultatTC(fichierTC)

    print("\nLe trie + la compression sont terminés.\n")

    os.chdir(cheminCourrant+"/"+"resultatTC/")
    print("Changement de dossier, on est dans le dossier : {}\n".format(os.getcwd()))

trieCompressionDossier()