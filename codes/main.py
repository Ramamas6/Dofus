""" A trading bot for Dofus """

from functions_buying import *

def general () :
    txt = pg.confirm("Menu principal",buttons=('Quitter','Allumer','Analyses prix','Achats'))
    while (txt != 'Quitter') :
        if txt == "Analyses prix" :
            n = pg.prompt(text='Saisir le temps d attente (défaut : 30 secondes ; minimum : 5 secondes)')
            n = conversion_entier(n)
            if n > 4 :
                evolution(n)
        elif txt == "Achats" :
            n = pg.prompt(text='Saisir le temps d attente (défaut : 30 secondes ; minimum : 5 secondes)')
            n = conversion_entier(n)
            banque()
            achat(n)
        elif txt == "Allumer" :
            allumage()
        txt = pg.confirm("Menu principal",buttons=('Quitter','Allumer','Analyses prix','Achats'))
    return 0

def test_photo (objet,k) :
    img = PIL.Image.open("../assets/Objets/"+objet+"/images/"+str(k)+".jpg")
    return reperer_prix(img)

#general()