""" Buying and selling functions (incorrect functioning) """

from functions_analyse import *

def ref_achetable () :
    """ Takes a reference photo of the buy button """
    pg.sleep(2)
    photo = pg.screenshot(region=(910,930,70,50))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/achetable.jpg")
    return 0

def achetable () :
    """ Return True if the buy button is green """
    photo = pg.screenshot(region=(910,930,70,50))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/achetable.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 5000 :
        return False
    else :
        return True

def ecriture_achat (objet,nbr,cout) :
    """ Write the information (number of purchases and cost) in the files """
    # Write in the object file
    fichier = open("../assets/Objets/"+objet+"/limites.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    fichier = open("../assets/Objets/"+objet+"/limites.txt","w")
    for k in range(7) :
        fichier.write(a[k]+"\n")
    fichier.write(str(nbr+entier(a[7]))+"\n")
    fichier.write(str(cout+entier(a[8]))+"\n")
    fichier.close()
    # Write in the general file
    fichier = open("../assets/ref/perso.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    fichier = open("../assets/ref/perso.txt","w")
    argt = int(a[0]) - cout
    stock = int(a[1]) - nbr
    fichier.write(str(argt)+"\n")
    fichier.write(str(stock)+"\n")
    fichier.write(a[2]+"\n")
    fichier.write(a[3]+"\n")
    fichier.close()
    if argt < 0 or stock < 0 :
        return 0
    else :
        return 1

def achat_objet_continu(objet,num) :
    """ Buy the item as long as possible and send back the number of times it could """
    gooo(objet)
    pg.sleep(1)
    pg.click(1070,(480+75*num))
    # Save the photo
    fichier = open("../assets/ref/perso.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    n = a[3]
    fichier = open("../assets/ref/perso.txt","w")
    fichier.write(a[0]+"\n")
    fichier.write(a[1]+"\n")
    fichier.write(a[2]+"\n")
    fichier.write(str(int(n)+1)+"\n")
    fichier.close()
    photo = pg.screenshot(region=(1035,465,80,190))
    texte = "../assets/achats/" + objet + n + ".jpg"
    photo.save(texte)
    # Buy in a loop
    k = 0
    while achetable() :
        pg.click(1000,950)
        pg.click(1070,610)
        k += 1
        pg.sleep(0.5)
    pg.click(520, 180)
    return k

def achat_fort (objet,min_fort) :
    """" Buys objects with a price lower than "min_fort" and returns the number of objects bought and the total price """
    nbr_obj = 0
    prix_total = 0
    v = True
    while v : # As long as there has been at least 1 purchase
        v = False
        a = prix(objet) # Update prices
        for k in range (3) :
            n = 10**k
            p = a[k]*(10**(2-k))
            if p < min_fort[0] and p < min_fort[1] and p > 0 : # Detects if a price is lower than min_fort
                nbr_achat = achat_objet_continu(objet,k)
                nbr_obj += (n * nbr_achat)
                prix_total += (a[k] * nbr_achat)
                if nbr_achat > 0 : # If he was able to buy at least 1 item: the loop starts again
                    v = True
    return (nbr_obj, prix_total)

def achat (attente_seconde) :
    """ Allows you to automatically buy cheap items """
    nbr_items = [0,1,2,3,4,5,6,7,8,9,10]
    objets_analyse = [11]
    L = [[[],[],[]] for i in range(len(objets_analyse))]
    attente = 1000*attente_seconde
    c = ""
    for i in range(len(nbr_items)) :
        analyse(attribution_num(nbr_items[i]))
    # Get the min_standard and min_fort
    min_standard = []
    min_fort = []
    for i in range(len(nbr_items)) :
        fichier = open("../assets/Objets/"+attribution_num(nbr_items[i])+"/limites.txt","r")
        a = fichier.read()
        fichier.close()
        a = a.split("\n")
        fichier = open("../assets/Objets/"+attribution_num(nbr_items[i])+"/limites100.txt","r")
        b = fichier.read()
        fichier.close()
        b = b.split("\n")
        min_standard.append([int(a[5]),int(b[4])])
        min_fort.append([int(a[6]),int(b[5])])
    # Buy
    while (c != "OK") :
        k = 0
        v = 0
        # Buy objects with a price lower than min_fort
        for i in range(len(nbr_items)) :
            (nbr,cout) = achat_fort(attribution_num(nbr_items[i]),min_fort[i])
            v = v + ecriture_achat(attribution_num(nbr_items[i]),nbr,cout)
        # Analysis of other objects
        for i in range (len(objets_analyse)) :
            a = prix(attribution_num(objets_analyse[i]))
            if a != (0,0,0) :
                L[i][0].append(a[2])
                L[i][1].append(a[0]*100)
                L[i][2].append(a[1]*10)
        # Wait
        k += 1
        if k == 10 :
            return 0
        if k == 15 :
            k = 0
            pg.click(1850,10)  # Click on the cross
            pg.click(1100,550) # Validate
            pg.sleep(1)
            allumage()
            for i in range(len(nbr_items)) :
                analyse(attribution_num(nbr_items[i]))
        if v < len(nbr_items) :
            print("Probleme dans les prix / dans le stockage")
            c = "OK"
        else :
            c = pg.confirm("Arrêter ?", timeout = attente)
    for i in range(len(L)) :
        pp.plot(L[i][0])
        pp.plot(L[i][1])
        pp.plot(L[i][2])
        pp.legend(['100', '1', '10'])
        pp.ylabel("Prix (pour 100)")
        pp.title("Evolution des prix de " + attribution_num(objets_analyse[i]))
        pp.savefig("../assets/Objets/"+attribution_num(objets_analyse[i])+"/figure.jpg")
        pp.show()
    return 1


