#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
#* Version : 0.0.1

#* Auteurs : MESTIRI Yosra, DELMAS Jean-Charles, RAVAOZAFINDRASOA Ravo

#* Contact :

        - yosra.mestiri@etu.umontpellier.fr
        - delmas.jeancharles@etu.umontpellier.fr
        - ravo.ravaozafindrasoa@etu.umontpellier.fr

#* Github  du projet : https://github.com/Jean-CharlesD/Projet_SYSTEM_2021

#* Algorithme mainMapping() :
    - fonction : traite les fichiers SAM et en donne un résumé statistique
    - paramètre : AUCUN

#* Le programme s'éxecute dans un terminal, et le fichier du programme doit être dans le dossier contenant les fichiers
"""

import os, shutil, pysam, re

#? [Vérification de fichiers]

def testLigne(fichierRegulier): #! regarde le header pour déterminer si le fichier est un SAM

    test = 0

    with open (fichierRegulier, "r") as fr:

        b = fr.readlines()[0]

        if re.match(r'@[A-Z][A-Z]', b):
            test = 1

    return test

def verificationFichier(fichierRegulier): #! on vérifie si le fichier est un fichier SAM

    cheminCourrant = os.getcwd()
    cheminFichierRegulier = cheminCourrant+"/"+fichierRegulier

    if os.path.isfile(cheminFichierRegulier) and os.path.getsize(cheminFichierRegulier) > 0 and testLigne(cheminFichierRegulier) == 1 :
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

#? [Trie et compression de fichiers]

def trieCompression(fichierRegulier): #! on obtient un fichierTC
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

#? [Extraction des reads  non-mappés]

def extractionUnmapped(fichierTC): #! on obtient un fichierTCEU
                                   #! samtools view <fichier d'entrée> -f 0X2 -bo <fichier de sortie>
    a = "{}.bam".format(fichierTC)
    b = "{}".format(fichierTC)
    c = "-f"
    d = "0X2"
    e = "-bo"
    with open ("{}[mapped].bam".format(fichierTC), "wb") as fichierTCEU:
        fichierTCEU.write(pysam.view(b, c, d, e, a))

def deplacementResultatTCEU(fichierTCEU):

    cheminCourrant = os.getcwd()
    cheminfichierTCEU = cheminCourrant+"/"+fichierTCEU
    cheminDossierResultatTCEU = cheminCourrant+"/"+"ResultatTCEU/"
    
    source = cheminfichierTCEU
    destination = cheminDossierResultatTCEU

    shutil.move(source,destination)

def extractionUnmappedDossier():

    if not os.path.isdir("ResultatTCEU"):
        os.makedirs("ResultatTCEU")         
        print("Dossier ResultatTCEU non-existant, le dossier a donc été crée.")

    print("\nL'extraction des reads non-mappés s'effectue, patientez...")

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierTC in dossier:
        if fichierTC.endswith(".bam") and os.path.isfile(fichierTC):
            extractionUnmapped(fichierTC)
    
    dossierReload01 = os.listdir(cheminCourrant)
    
    for fichierTCEU in dossierReload01:
        if fichierTCEU.endswith("[mapped].bam") and os.path.isfile(fichierTCEU):
            deplacementResultatTCEU(fichierTCEU)

    for fichierTC in dossier:
       if fichierTC.endswith(".bam") and os.path.isfile(fichierTC):
            os.remove(fichierTC)

    print("\nL'extraction est terminée.\n")

    os.chdir(cheminCourrant+"/"+"ResultatTCEU/")
    print("Changement de dossier, on est dans le dossier : {}\n".format(os.getcwd()))

#? [Statistiques de fichiers]

def stats(fichierTCEU): #! on obtient un fichierStats 
                        #! samtools stats <fichier> | grep ^SN

    a = "{}".format(fichierTCEU)

    with open ("{}[stats01].txt".format(fichierTCEU), "w") as fichierStats01:
        b = str(pysam.stats(a))
        fichierStats01.write(b)
    
    with open ("{}[FinalStats].txt".format(fichierTCEU), "w") as fichierFinalStats: 
        with open("{}[stats01].txt".format(fichierTCEU), "r") as c:
            d = c.readlines()
            for lignes in d:
                if lignes.startswith("SN"):
                    fichierFinalStats.write(lignes)

def deplacementResultatStats(fichierStats):

    cheminCourrant = os.getcwd()
    cheminfichierStats = cheminCourrant+"/"+fichierStats
    cheminDossierResultatStats = cheminCourrant+"/"+"ResultatStats/"
    
    source = cheminfichierStats
    destination = cheminDossierResultatStats

    shutil.move(source,destination)

def statsDossier():

    if not os.path.isdir("ResultatStats"):
        os.makedirs("ResultatStats")         
        print("Dossier ResultatStats non-existant, le dossier a donc été crée.")
    
    print("\nLa récolte de statistiques s'effectue, patientez...")

    cheminCourrant = os.getcwd()
    dossier = os.listdir(cheminCourrant)

    for fichierTCEU in dossier:
        if fichierTCEU.endswith(".bam") and os.path.isfile(fichierTCEU):
            stats(fichierTCEU)

    dossierReload01 = os.listdir(cheminCourrant)

    for fichierFinalStats in dossierReload01:
        if fichierFinalStats.endswith("[FinalStats].txt") and os.path.isfile(fichierFinalStats):
            deplacementResultatStats(fichierFinalStats)
    
    for fichierTCEU in dossierReload01:
        if (fichierTCEU.endswith(".bam") and os.path.isfile(fichierTCEU)) or (fichierTCEU.endswith("[stats01].txt") and os.path.isfile(fichierTCEU)):
            os.remove(fichierTCEU)
    
    print("\nLa récolte est terminée.")

#? [mainMapping]

def mainMapping():

    verificationDossier()
    trieCompressionDossier()
    extractionUnmappedDossier()
    statsDossier()

mainMapping()