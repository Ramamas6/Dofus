""" Some various functions """

from matplotlib import pyplot as pp
from functions_on import *

def entier (k) :
    """ Convert a char k in an integer (with the possibility of an empty k) """
    if k == '' :
        return 0
    else :
        return int(k)

def attribution_num (k) :
    """ Assigns an integer k to an object """
    if k == 0 :
        return "eau"
    if k == 1 :
        return "ble"
    if k == 2 :
        return "avoine"
    if k == 3 :
        return "orge"
    if k == 4 :
        return "seigle"
    if k == 5 :
        return "lin"
    if k == 6 :
        return "chanvre"
    if k == 7 :
        return "riz"
    if k == 8 :
        return "houblon"
    if k == 9 :
        return "frostiz"
    if k == 10 :
        return "malt"
    if k == 11 :
        return "citron"
    if k == 12 :
        return "mesure de sel"

def gooo (objet) :
    """ Go click on an object """
    while not reconnaissance_hdv() :
        pg.sleep(1)
    pg.click(1570, 710,duration=1)     # Click on the sales hotel
    pg.click(230, 250,duration=0.5)    # Click on the search bar
    pg.write(objet)
    pg.press("enter")
    if objet == "eau" :
        # Scrolls
        pg.moveTo(230, 800)
        pg.mouseDown()
        pg.moveTo(230, 100)
        pg.mouseUp()
        # Click on the water
        pg.click(230,500)
        pg.click(230,700,duration=1)
    elif objet == "ble" :
        # Scrolls
        pg.moveTo(230, 800)
        pg.mouseDown()
        pg.moveTo(230, 100)
        pg.mouseUp()
        # Click on the wheat
        pg.click(230, 390)
        pg.click(230, 440,duration=1)
    elif objet == "orge" :
        pg.click(230, 780,duration=0.5)
        pg.click(230, 700,duration=1)
    elif objet == "avoine" :
        pg.click(230, 470,duration=0.5)
        pg.click(230, 530,duration=1)
    elif objet == "riz" :
        pg.click(230, 780,duration=0.5)
        pg.click(230, 700,duration=1)
    elif objet == "houblon" :
        pg.click(230, 400,duration=0.5)
    elif objet == "lin" :
        # Scrolls
        pg.moveTo(230, 800)
        pg.mouseDown()
        pg.moveTo(230, 100)
        pg.mouseUp()
        # Click on the linen
        pg.click(230, 580)
        pg.click(230, 640,duration=1)
    elif objet == "seigle" :
        pg.click(230, 400,duration=0.5)
        pg.click(230, 460,duration=1)
    elif objet == "malt" :
        pg.sleep(0.5)
        pg.click(230, 400)
    elif objet == "chanvre" :
        pg.click(230, 350,duration=0.5)
        pg.click(230, 400,duration=1)
    elif objet == "frostiz" :
        pg.click(230, 480,duration=0.5)
        pg.click(230, 520,duration=1)
    elif objet == "citron" :
        pg.click(230, 540,duration=0.5)
        pg.click(230, 600,duration=1)
    elif objet == "mesure de sel" :
        pg.sleep(0.1)
    # Click on the object
    pg.click(230,450,duration=1)
    pg.click(650,410,duration=1)
    return 1

def conversion_entier (texte) :
    """ Convert a text to an integer, omitting letters and special characters """
    if type(texte) != str :
        return 0
    i = 0
    nbr = ""
    for k in range(len(texte)) :
        if (texte[k] == '0') or (texte[k] == '1') or (texte[k] == '2') or (texte[k] == '3') or (texte[k] == '4') or (texte[k] == '5') or (texte[k] == '6') or (texte[k] == '7') or (texte[k] == '8') or (texte[k] == '9') :
            nbr = nbr+texte[k]
    for k in range (len(nbr)) :
        i += int(nbr[k]) * (10**(len(nbr)-k-1))
    return i

def mini (mat) :
    """ Returns the minimum of a matrix and its row """
    k = min(mat[0])
    j = (0)
    for i in range (1, len(mat)):
        if min(mat[i]) < k :
            k = min(mat[i])
            j = i
    return (k,j)

def maxi (mat) :
    """ Returns the maximum of a matrix and its row """
    k = max(mat[0])
    j = 0
    for i in range (1, len(mat)):
        if max(mat[i]) > k :
            k = max(mat[i])
            j = i
    return (k,j)

def tri_mat (mat) :
    """ Sorting a matrix """
    for i in range (len(mat)) :
        min = mat[i]
        imin = i
        for j in range (i,len(mat)) :
            if mat[j][1] < min[1] :
                min = mat[j]
                imin = j
        mat[imin] = mat[i]
        mat[i] = min
    return mat

def tri_tab (tab) :
    """ Sort a table """
    for i in range (len(tab)) :
        min = tab[i]
        imin = i
        for j in range (i,len(tab)) :
            if tab[j] < min :
                min = tab[j]
                imin = j
        tab[imin] = tab[i]
        tab[i] = min
    return tab

def moy_tab (tab) :
    """ Return the average value (neither the min nor the max) of an array with 3 values """
    M = max(tab)
    m = min(tab)
    if (tab[0] != M and tab[0] != m) :
        return tab[0]
    elif (tab[1] != M and tab[1] != m) :
        return tab[1]
    else :
        return tab[2]

def mini_pourcent (L, k) :
    """ Returns the minimum to k% of a sorted list """
    k = 100-k
    n = int(k*len(L)/100)
    if L == [] or k > 100 or k < 0 :
        return 99999
    elif n < len(L) :
        return L[n]
    else :
        return L[n-1]

def maxi_pourcent (L, k) :
    """ Returns the maximum to k% of a sorted list """
    n = int(k*len(L)/100)+1
    if L == [] or k > 100 or k < 0 :
        return 0
    elif n < len(L) :
        return L[n]
    else :
        return L[n-1]

def somme (tab) :
    """ Calculate the sum of the values of an array """
    s = 0
    for k in range (len(tab)) :
        s += tab[k]
    return s

def coloree (img,l1,l2) :
    """ Return True if ? """
    tab = np.array(img)
    mi = mini(tab[l1])
    Ma = maxi(tab[l1])
    for k in range(l1,l2) :
        m = mini(tab[k])
        M = maxi(tab[k])
        if m < mi :
            mi = m
        if M > Ma :
            Ma = M
    if (mi[0] < 15) or (Ma[0] < 240) :
        return True
    else :
        return False

def noir_blanc (photo) :
    """ Transforms an image into black and white """
    img = photo.convert("L")
    tab = np.array(img)
    """ Line 1 """
    if coloree(photo,0,54) :
        for i in range(54):
            for j in range(len(tab[0])):
                if tab[i][j] > 60 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    else :
        for i in range(54):
            for j in range(len(tab[0])):
                if tab[i][j] > 100 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    """ Line 2 """
    if coloree(photo,54,135) :
        for i in range(54,135):
            for j in range(len(tab[0])):
                if tab[i][j] > 60 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    else :
        for i in range(54,135):
            for j in range(len(tab[0])):
                if tab[i][j] > 100 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    """ Line 3 """
    if coloree(photo,135,len(tab)) :
        for i in range(135,len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j] > 60 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    else :
        for i in range(135,len(tab)):
            for j in range(len(tab[0])):
                if tab[i][j] > 100 :
                    tab[i][j] = 255
                else :
                    tab[i][j] = 0
    img = PIL.Image.fromarray(tab)
    return img

def noir_blanc_mat (tab) :
    """ Transforms a matrix into black and white """
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] > 100 :
                tab[i][j] = 255
            else :
                tab[i][j] = 0
    return tab

def references_num ():
    """ Take a picture a reference number """
    pg.sleep(1)
    photo = pg.screenshot(region=(1043,468,12,17))
    photo = noir_blanc(photo)
    photo.save("ref.jpg")
    photo.show()
    return 0