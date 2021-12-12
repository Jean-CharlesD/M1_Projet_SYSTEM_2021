#!/usr/bin/python3
#-*- coding : utf-8 -*-

"""
#* Algorithme extractionUnmapped():
    - fonction : Donne un fichierTCEU à partir d'un fichierTC
    - paramètres : Nécessite un fichierTC

#* Algorithme deplacementResultatTCEU():
    - fonction : Déplace un fichierTCEU vers le répertoire ResultatTCEU/
    - paramètres : Nécessite un fichierTCEU

#* Algorithme extractionUnmappedDossier():
    - fonction : Pour tout fichierTC d'un dossier,donne un fichierTCEU puis le déplace vers le répertoire ResultatTCEU/
    - paramètres : AUCUN

#* Le programme s'éxecute dans un terminal, et le fichier du programme doit être dans le dossier contenant les fichiers
"""

import os, shutil, pysam

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

extractionUnmappedDossier()