#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
#* Algorithme stats():
    - fonction : Donne un fichierStats à partir d'un fichierTCEU
    - paramètres : Nécessite un fichierTCEU

#* Algorithme deplacementResultatStats():
    - fonction : Déplace un fichierStats vers le répertoire ResultatStats/
    - paramètres : Nécessite un fichierStats

#* Algorithme StatsDossier():
    - fonction : Pour tout fichierTCEU d'un dossier,donne un fichierStats puis le déplace vers le répertoire ResultatStats/
    - paramètres : AUCUN

#* Le programme s'éxecute dans un terminal, et le fichier du programme doit être dans le dossier contenant les fichiers
"""

import os, shutil, pysam

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

statsDossier()