# importerer os, som bruges til at se om den fysiske sti eksisterer
import os
# importerer shutil, som bruges til at kopiere mapper og filer, hvis destinationsmappen ikke eksisterer
import shutil
# importerer date, som bruges til timestamp i logs
from datetime import datetime
# importerer isfile, bruges til at se om sti fører til en file
from genericpath import isfile


# vi laver en metode, som tager imod parametrene source og destination (bruger input)
def copyFunction(source, destination):
    # vi bruger en try/except til logning
    try:
        # vi ser om source-stien eksisterer
        if os.path.exists(source):
            # vi ser om destination-stien
            if os.path.exists(destination):
                # looper alle filer og mapper igennem og sletter dem
                for path in os.scandir(destination):
                    # ser om det er en fil og sletter den
                    if isfile(path):
                        os.remove(path)
                    # ser om det er en sti og sletter den
                    elif os.path.exists(path):
                        os.rmdir(path)
                # hvis stien eksisterer, giver vi copytree en ekstra parameter, som siger at den gerne må eksistere
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                # hvis stien ikke eksisterer, så opretter vi den og lægger filerne ind
                shutil.copytree(source, destination)
            logFunction('copy backup', 'true')
        else:
            # hvis sourceFolder ikke eksisterer, fortæller vi brugeren og laver en log-fil
            print("Source folder does not exist")
            logFunction('copy backup', 'false')
    except:
        # hvis det fejler, skriver vi det i logfilen
        logFunction('copy backup', 'false')


# vi laver en lognings metode
def logFunction(function, success):

    # vi definerer sti for log-fil
    logPath = "/Users/moa/Documents/logs/Copy logs.csv"
    # vi definerer tid for kald
    today = datetime.now()

    if os.path.exists(logPath):
        # hvis log-fil allerede eksisterer, så skriver vi i den (a = appending)
        with open(logPath, 'a') as file:
            file.write(function + ',' + success + ',' + str(today) + '\n')
    else:
        # hvis log-fil ikke eksisterer, så opretter vi den før vi skriver i den (x = create)
        with open(logPath, 'x') as file:
            file.write('function,success,date\n')
            file.write(function + ',' + success + ',' + str(today) + '\n')


# variable, som bruges til at definere stierne
sourceFolder = "/Users/moa/Documents/backup1"
destinationFolder = "/Users/moa/Documents/backup2"

# vi kalder metoden med forskellige sources og destinations
copyFunction(sourceFolder, destinationFolder)
# copyFunction(/Users/moa/Documents/backup1, /Users/moa/Documents/backup2)