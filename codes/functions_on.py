""" Functions for to the starting of Dofus """

import pyautogui as pg
import numpy as np
import PIL

def agrandir () :
    """ Take a reference photo of the enlarge square"""
    pg.sleep(2)
    photo = pg.screenshot(region=(1475,220,20,20))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/agrandir.jpg")
    return 0

def reconnaissance_agrandir () :
    """ Return True if the enlarge square is visible"""
    photo = pg.screenshot(region=(1475,220,20,20))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/agrandir.jpg")
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

def jouer () :
    """ Takes a reference photo of the play button """
    pg.sleep(2)
    photo = pg.screenshot(region=(1290,430,160,60))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/jouer.jpg")
    return 0

def reconnaissance_jouer () :
    """ Return True if the play button is visible"""
    photo = pg.screenshot(region=(1290,430,160,60))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/jouer.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 20000 :
        return False
    else :
        return True

def serveur () :
    """ Takes a reference photo of the select button """
    pg.sleep(2)
    photo = pg.screenshot(region=(860,760,160,30))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/serveur.jpg")
    return 0

def reconnaissance_serveur () :
    """ Return True if the select button is visible"""
    photo = pg.screenshot(region=(860,760,160,30))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/serveur.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 20000 :
        return False
    else :
        return True

def jouer2 () :
    """ Take a reference photo of the 2nd play button """
    pg.sleep(2)
    photo = pg.screenshot(region=(1140,860,90,40))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/jouer2.jpg")
    return 0

def reconnaissance_jouer2 () :
    """ Return True if the 2nd play button is visible"""
    photo = pg.screenshot(region=(1140,860,90,40))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/jouer2.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 10000 :
        return False
    else :
        return True

def hdv () :
    """ Takes a reference photo of the sales hotel """
    pg.sleep(2)
    photo = pg.screenshot(region=(1550,690,50,50))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/hdv.jpg")
    return 0

def reconnaissance_hdv () :
    """Return True if the sales hotel is visible"""
    photo = pg.screenshot(region=(1550,690,50,50))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/hdv.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 20000 :
        return False
    else :
        return True

def attention () :
    """ Take a reference photo of the warning pop-up """
    pg.sleep(2)
    photo = pg.screenshot(region=(910,630,60,40))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/attention.jpg")
    return 0

def reconnaissance_attention () :
    """ Return True if the warning pop-up is visible"""
    photo = pg.screenshot(region=(910,630,60,40))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/attention.jpg")
    a_ref = np.array(a)
    k = 0
    for i in range (len(tab)) :
        for j in range (len(tab[0])) :
            if tab[i][j] > a_ref[i][j] :
                k += tab[i][j] - a_ref[i][j]
            else :
                k += a_ref[i][j] - tab[i][j]
    if k > 8000 :
        return False
    else :
        return True

def offrande () :
    """ Take a reference photo of the offering pop-up """
    pg.sleep(2)
    photo = pg.screenshot(region=(580,510,40,30))
    photo = photo.convert("L")
    photo.show()
    photo.save("../assets/ref/offrande.jpg")
    return 0

def reconnaissance_offrande () :
    """ Return True if the offering pop-up is visible"""
    photo = pg.screenshot(region=(580,510,40,30))
    photo = photo.convert("L")
    tab = np.array(photo)
    a = PIL.Image.open("../assets/ref/offrande.jpg")
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

def banque () :
    """ Recover all the money from the bank """
    pg.click(960,550,duration=1)   # Banker
    pg.click(600,900,duration=2)   # Bank
    pg.click(320,940,duration=1)   # Withdrawal
    pg.click(750,960,duration=1)   # All
    pg.click(1020,960,duration=1)  # Validate
    pg.click(550,100,duration=1)   # Quit
    return 0

def allumage (auto_enlarge = 0) :
    """ Launch Dofus """
    pg.click(1918,1078)         # Go to the desktop
    pg.doubleClick(1250, 400)   # Allumer BlueStacks
    if (auto_enlarge) : # If the game is not automatically in full screen
        while not reconnaissance_agrandir() :
            pg.sleep(1)
        pg.click(1480,230)         # Enlarge the window
    while not reconnaissance_jouer() :
        pg.sleep(1)
    pg.click(1400,450)         # Click on play
    while not reconnaissance_serveur() :
        pg.sleep(1)
    pg.click(950,780)          # Choice of server
    while not reconnaissance_jouer2() :
        pg.sleep(1)
    pg.click(1200,880)         # Character selection
    while not reconnaissance_hdv() :
        pg.sleep(1)
    if reconnaissance_attention() :
        pg.click(920,640)
    if reconnaissance_offrande() :
        pg.click(600,520)
    banque()
    return 1
