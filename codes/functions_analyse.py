""" Price analysis functions """

from functions_reading import *

def analyse (objet) :
    """ Calculates and saves the different statistics of the prices of the object """
    # Get the prices
    texte = "../assets/Objets/" + objet + "/prix.txt"
    fichier = open(texte,"r")
    a = fichier.read()
    fichier.close()
    prix = a.split("\n")
    del prix[0]
    if len(prix) == 0:
        return 0
    # Entry of the different prices
    PrixGen = []
    PrixPart = [[],[],[]]
    for i in range (len(prix)) :
        prix[i] = prix[i].split("\t")
        for k in range(3) :
            if (int(prix[i][k])) > 0 :
                PrixPart[2-k].append(int(prix[i][k]))
                PrixGen.append(int(prix[i][k]))
    # Drawing of general curves
    for k in range (3) :
        pp.plot(PrixPart[k])
    pp.legend(['1', '10', '100'])
    pp.ylabel("Prix (pour 100)")
    pp.title("Evolution des prix de " + objet)
    pp.savefig("../assets/Objets/"+ objet +"/figure_générale.jpg")
    pp.close()
    # General Price Statistics
    PrixGen = tri_tab(PrixGen)
    for k in range(3) :
        PrixPart[k] = tri_tab(PrixPart[k])
    m = PrixGen[0]
    M = PrixGen[len(PrixGen)-1]
    moyenne = int(somme(PrixGen)/len(PrixGen))
    moy_etendue = int((M + m)/2)
    min_standard = mini_pourcent(PrixGen,90)
    min_fort = mini_pourcent(PrixGen,95)
    fichier = open("../assets/Objets/"+objet+"/limites.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    fichier = open("../assets/Objets/"+objet+"/limites.txt","w")
    fichier.write(a[0]+"\n")
    fichier.write(str(m)+"\n")
    fichier.write(str(M)+"\n")
    fichier.write(str(moyenne)+"\n")
    fichier.write(str(moy_etendue)+"\n")
    fichier.write(str(min_standard)+"\n")
    fichier.write(str(min_fort)+"\n")
    for k in range(7,len(a)) :
        fichier.write(a[k]+"\n")
    fichier.close()
    # Specific price statistics
    for k in range(3) :
        m = PrixPart[k][0]
        M = PrixPart[k][len(PrixPart[k])-1]
        moyenne = int(somme(PrixPart[k])/len(PrixPart[k]))
        moy_etendue = int((M + m)/2)
        min_standard = mini_pourcent(PrixPart[k],90)
        min_fort = mini_pourcent(PrixPart[k],95)
        max_standard = maxi_pourcent(PrixPart[k],90)
        max_fort = maxi_pourcent(PrixPart[k],95)
        fichier = open("../assets/Objets/"+objet+"/limites"+str(10**k)+".txt","r")
        a = fichier.read()
        fichier.close()
        a = a.split("\n")
        fichier = open("../assets/Objets/"+objet+"/limites"+str(10**k)+".txt","w")
        fichier.write(str(m)+"\n")
        fichier.write(str(M)+"\n")
        fichier.write(str(moyenne)+"\n")
        fichier.write(str(moy_etendue)+"\n")
        fichier.write(str(min_standard)+"\n")
        fichier.write(str(min_fort)+"\n")
        fichier.write(str(max_standard)+"\n")
        fichier.write(str(max_fort)+"\n")
        for k in range(9,len(a)) :
            fichier.write(a[k]+"\n")
        fichier.close()
    return (1)

def evolution (attente_seconde) :
    """ Retrieves prices items (in loop) """
    nbr = 12
    L = [[[],[],[]] for i in range(nbr)]
    attente = 1000*attente_seconde
    k = 0
    c = ""
    while (c != "OK") :
        for i in range(nbr) :
            a = prix(attribution_num(i))
            if a != (0,0,0) :
                L[i][0].append(a[2])
                L[i][1].append(a[0]*100)
                L[i][2].append(a[1]*10)
        k += 1
        if k == 15 : # Re-demare dofus (in case of bug)
            k = 0
            pg.click(1850,10)  # Click on the cross
            pg.click(1100,550) # Validate
            pg.sleep(1)
            allumage()
        c = pg.confirm("Arrêter ?", timeout = attente)
    for i in range(nbr) :
        pp.plot(L[i][0])
        pp.plot(L[i][1])
        pp.plot(L[i][2])
        pp.legend(['100', '1', '10'])
        pp.ylabel("Prix (pour 100)")
        pp.title("Evolution des prix de " + attribution_num(i))
        pp.savefig("../assets/Objets/"+attribution_num(i)+"/figure.jpg")
        pp.show()
    return 1






