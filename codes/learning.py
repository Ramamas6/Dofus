""" Allows you to set max_diff_num (already set) """

from functions_reading import *

def test ():
    """ Useless : takes a photo """
    pg.sleep(1)
    photo = pg.screenshot(region=(1035,465,80,190))
    return photo

def take_photo ():
    """ Takes a picture, saves it and adds its number to the database """
    # Determine the number of the photo
    fichier = open("../assets/learning/photos.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    a = a[len(a)-1]
    a = a.split("\t")
    a = int(a[0]) + 1
    a = str(a)
    # Take and save the picture
    pg.sleep(1)
    photo = pg.screenshot(region=(1035,465,80,190))
    photo = noir_blanc(photo)
    texte = "../assets/learning/" + a + ".jpg"
    photo.save(texte)
    # Writes the number of the photo in the file
    fichier = open("../assets/learning/photos.txt","a")
    fichier.write("\n")
    fichier.write(a)
    fichier.write("\t0\t0\t0")
    fichier.close()
    photo.show()
    return 0

def copie_max_diff(k) :
    """ Make a backup (copy) of the file """
    fichier = open("../assets/ref/max_diff.txt","r")
    a = fichier.read()
    fichier.close()
    texte = "../assets/learning/max_diff" + str(k) + ".txt"
    fichier = open(texte,"w")
    fichier.write(a)
    fichier.close()
    return 0

def verifier_learning () :
    """ Displays the photos for which the price is not good """
    fichier = open("../assets/learning/photos.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    a = a[len(a)-1]
    a = a.split("\t")
    a = int(a[0])
    j = 0
    for i in range (1,a+1) :
        fichier = open("../assets/learning/photos.txt","r")
        a = fichier.read()
        fichier.close()
        a = a.split("\n")
        a = a[i]
        a = a.split("\t")
        prix_reels = [int(a[1]),int(a[2]),int(a[3])]
        texte = "../assets/learning/" + str(i) + ".jpg"
        img = PIL.Image.open(texte)
        prix = reperer_prix(img)
        if (prix[0] != prix_reels[0] or prix[1] != prix_reels[1] or prix[2] != prix_reels[2]) :
            print(str(i)+" : PB")
            j += 1
    return j

def modifier_max_diff(prix,prix_reel) :
    """" Counting of the number of occurrences of each item in the two prizes """
    P = [0 for i in range(10)]
    PR = [0 for i in range(10)]
    P0 = [0 for i in range(10)]
    PR0 = [0 for i in range(10)]
    P1 = [0 for i in range(10)]
    PR1 = [0 for i in range(10)]
    P2 = [0 for i in range(10)]
    PR2 = [0 for i in range(10)]
    for i in range (len(prix)):
        a = str(prix[i])
        for j in range (len(a)):
            P[int(a[j])] += 1
    for i in range (len(prix_reel)):
        a = str(prix_reel[i])
        for j in range (len(a)):
            PR[int(a[j])] += 1
    a = str(prix[0])
    for j in range (len(a)):
        P0[int(a[j])] += 1
    a = str(prix[1])
    for j in range (len(a)):
        P1[int(a[j])] += 1
    a = str(prix[2])
    for j in range (len(a)):
        P2[int(a[j])] += 1
    a = str(prix_reel[0])
    for j in range (len(a)):
        PR0[int(a[j])] += 1
    a = str(prix_reel[1])
    for j in range (len(a)):
        PR1[int(a[j])] += 1
    a = str(prix_reel[2])
    for j in range (len(a)):
        PR2[int(a[j])] += 1
    # Increases of max_diff
    fichier = open("../assets/ref/max_diff.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    verif = False
    for k in range (10) :
        if (P0[k] < PR0[k]) or (P1[k] < PR1[k]) or (P2[k] < PR2[k]):
            a[k] = str(10+int(a[k]))
            verif = True
    fichier = open("../assets/ref/max_diff.txt","w")
    for k in range (10) :
        fichier.write(a[k])
        fichier.write("\n")
    fichier.close()
    # Returns the differences of the number of occurrences
    for k in range (10) :
        PR[k] = PR[k] - P[k]
    return verif

def traitement (k):
    """ Processes the image of number k """
    # Get the real prices of the image
    fichier = open("../assets/learning/photos.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    a = a[k]
    a = a.split("\t")
    prix_reels = [int(a[1]),int(a[2]),int(a[3])]
    if prix_reels == [0,0,0] :
        return 0
    texte = "../assets/learning/" + str(k) + ".jpg"
    img = PIL.Image.open(texte)
    prix = reperer_prix(img)
    j = 1
    while modifier_max_diff(prix,prix_reels) :
        print(j)
        j += 1
        prix = reperer_prix(img)
    copie_max_diff(k)
    return "i"

