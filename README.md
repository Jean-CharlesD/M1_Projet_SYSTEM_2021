# Projet_SYSTEM_2021

#* Version : 0.0.1

#* Auteurs : MESTIRI Yosra, DELMAS Jean-Charles, RAVAOZAFINDRASOA Ravo

#* Contact :

        - yosra.mestiri@etu.umontpellier.fr
        - delmas.jeancharles@etu.umontpellier.fr
        - ravo.ravaozafindrasoa@etu.umontpellier.fr
                 
#* Description :
        
        Ce programme permet, à partir d'un dossier contenant des fichiers de Mapping SAM, d'obtenir des résumés (sous forme de fichiers .txt) 
        des informations des alignements de lectures.
        
        Le programme est fonctionnel, mais des améliorations sont encore possibles.
        
        Le programme est en python3, pour l'utiliser il faut récupérer le script nommé "systeme05MainMapping".
        Les modules os, pysam, shutil sont nécessaires pour faire fonctionner le programme.
        Le script s'exécute dans le dossier contenant les fichiers à traiter, il s'exécute dans un terminal de commande.
        Une fois le script exécuté, aucune autre action n'est requise de la part de l'utilisateur.
        
#* Programme systeme05MainMapping :

        #- fonction : traite des fichiers SAM dans un dossier, et en donne des résumés statistiques sous forme de fichiers .txt

        #- paramètres : AUCUN
        
        #- modules nécessaires : os ; pysam ; shutil

#* Exécution du script : 

        #- récupérer le script du programme, ensuite le placer à l'intérieur du dossier contenant les fichiers à traiter
     
        #- ouvrir un terminal de commandes, puis se placer dans le dossier à traiter, via la commande : cd <chemin du dossier>
        
        #- octroier le droit d'exécution au script, à l'aide de la commande : chmod +x systeme05MainMapping
        
        #- exécuter le script, en entrant la commande : python3 systeme05MainMapping

#* Notes : 

        #- Vérifier que les fichiers à traiter possèdent l'extension .sam (en minuscule)
        
        #- Pour installer le module pysam, taper dans le terminal de commande : pip install pysam
