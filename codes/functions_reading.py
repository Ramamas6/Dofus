""" Screen reading and analysis functions """

from functions_usefull import *

def ecriture_fichier (nom,L) :
    """ Write the price in the price file """
    titre = "../assets/Objets/" + nom + "/prix.txt"
    fichier = open(titre,"a")
    fichier.write("\n"+str(L[2])+"\t"+str(L[1]*10)+"\t"+str(L[0]*100))
    fichier.close()
    return 1

def ecriture_fichier_liste (nom,L) :
    """ Write the prices (of a list) in the price file """
    titre = "../assets/Objets/" + nom + "/prix.txt"
    fichier = open(titre,"a")
    for k in range (len(L[0])) :
        fichier.write("\n"+str(L[0][k])+"\t"+str(L[2][k])+"\t"+str(L[1][k]))
    fichier.close()
    return 1

def arrondi_ligne (i) :
    """ Round off the lines """
    if i < 10 :     # L1 : between 1 and 3
        return 1
    elif i < 110 :  # L2 : between 82 and 86
        return 2
    else :          # L3 : between 166 and 168
        return 3

def max_diff_num (x) :
    """ Returns the maximum difference value of one numeral "x" """
    fichier = open("../assets/ref/max_diff.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    return int(a[x])

def reperer_num (img,x) :
    """ Locate all the numeral "x" in the picture """
    tab = np.array(img)
    nom_image = "../assets/ref/" + str(x) + ".jpg"
    ref = PIL.Image.open(nom_image)
    ref = np.array(ref)
    L = []
    k = 0
    # Calculation of the differences between the "x" and each subarray of the image
    for it in range (len(tab)):
        for jt in range (len(tab[0])):
            if (it < 5) or (it > 80 and it < 88) or (it > 164 and it < 170) :
                if (it < len(tab) - len(ref)) and (jt < len(tab[0]) - len(ref[0])) :
                    k = 0
                    for i in range (it,it+len(ref)) :
                        for j in range (jt,jt+len(ref[0])) :
                            if tab[i][j] > ref[i-it][j-jt] :
                                k += tab[i][j] - ref[i-it][j-jt]
                            else :
                                k += ref[i-it][j-jt] - tab[i][j]
                    # If the difference is smaller than max_diff (modifiable): an "x" is marked
                    if k < max_diff_num(x) :
                        v = True
                        # Verification that it is not an already spotted "x"
                        for k in range (len(L)) :
                            m = abs(it - L[k][1]) + abs(jt - L[k][2])
                            if m < 10 :
                                v = False
                        if v == True:
                            L.append((k,it,jt))
    for i in range (len(L)) :
        L[i] = (L[i][0],arrondi_ligne(L[i][1]),L[i][2])
    return L

def suppr_nbr (tab) :
    """ Removes numbers that appear in excess """
    # Delete the 1's that appear in excess
    i = 0
    while (i < len(tab)) :
        if (tab[i][0]) == 1 :
            v = False
            if (i > 1 and abs(tab[i-1][1] - tab[i][1]) < 7) or (i < len(tab)-1 and abs(tab[i+1][1] - tab[i][1]) < 7) :
                del tab[i]
        i += 1
    # Removes the k > 1 that appear in excess
    i = 0
    while (i < len(tab)-1) :
        if abs(tab[i+1][1] - tab[i][1]) < 5 :
            if tab[i+1][2] < tab[i][2] :
                del tab[i]
            else :
                del tab[i+1]
        else :
            i += 1
    return tab

def prix_fini (tab) :
    """ Returns the price of an array (eg : [1, 2, 3] -> 123)"""
    x = 0
    for k in range (len(tab)) :
        x += tab[len(tab) - k - 1][0] * (10**k)
    return x

def reperer_prix(img) :
    """ Returns the prices of an image """
    L = []
    for k in range (10) :
        L.append(reperer_num(img,k))
    # Separation of the lines
    L1 = []
    L2 = []
    L3 = []
    for i in range (len(L)) :
        for j in range (len(L[i])) :
            if L[i][j][1] == 1 :
                L1.append((i,L[i][j][2],L[i][j][0]))
            if L[i][j][1] == 2 :
                L2.append((i,L[i][j][2],L[i][j][0]))
            if L[i][j][1] == 3 :
                L3.append((i,L[i][j][2],L[i][j][0]))
    a1 = prix_fini(suppr_nbr(tri_mat(L1)))
    a2 = prix_fini(suppr_nbr(tri_mat(L2)))
    a3 = prix_fini(suppr_nbr(tri_mat(L3)))
    return (a1,a2,a3)

def prix (objet) :
    """ Returns the current price of an object and writes it to the price file """
    gooo(objet)
    # Take the picture
    pg.sleep(1)
    photo = pg.screenshot(region=(1035,465,80,190))
    pg.click(520, 180)
    # Find the number of the photo
    fichier = open("../assets/Objets/"+objet+"/limites.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    n = a[0]
    # Saving the photo
    photo = noir_blanc(photo)
    texte = "../assets/Objets/" + objet + "/images/" + n + ".jpg"
    photo.save(texte)
    # Refreshes the limit file
    fichier = open("../assets/Objets/"+objet+"/limites.txt","w")
    fichier.write(str(int(n)+1))
    for k in range(1,len(a)) :
        fichier.write("\n"+a[k])
    fichier.close()
    # Get the prices of the photo and enter them in the price file
    p = reperer_prix(photo)
    if p != (0,0,0) :
        ecriture_fichier(objet,p)
    return p