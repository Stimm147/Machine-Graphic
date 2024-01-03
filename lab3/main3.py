from PIL import Image
import numpy as np


def dwa_prostokaty(width, height, m, n):
    t = (height, width)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = 100
    for i in range(n):
        for j in range(m):
            tab[i][j] = 200
    for i in range(n, height):
        for j in range(m, width):
            tab[i][j] = 200

    tab1 = tab.astype(np.uint8)
    return Image.fromarray(tab1)


obraz1_1 = dwa_prostokaty(480, 320, 100, 50)
obraz1_1.save("obraz1_1.jpg")
obraz1_1.save("obraz1_1.png")


def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg


tab_neg = negatyw_szare(obraz1_1)
obraz1_1N = Image.fromarray(tab_neg)
obraz1_1N.save("obraz1_1N.jpg")
obraz1_1N.save("obraz1_1N.png")


def rysuj_ramke_szare(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = 100
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = (k+50) % 256
    tab1 = tab.astype(np.uint8)
    return Image.fromarray(tab1)


obraz1_2 = rysuj_ramke_szare(480, 320, 20)
obraz1_2.save("obraz1_2.jpg")
obraz1_2.save("obraz1_2.png")

tab_neg1 = negatyw_szare(obraz1_2)
obraz1_2N = Image.fromarray(tab_neg1)
obraz1_2N.save("obraz1_2N.jpg")
obraz1_2N.save("obraz1_2N.png")


def dwa_prostokaty_kolor(width, height, m, n):
    t = (height, width, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [25,170,200]
    for i in range(n):
        for j in range(m):
            tab[i][j] = [100,50,200]
    for i in range(n, height):
        for j in range(m, width):
            tab[i][j] = [100,50,200]

    tab1 = tab.astype(np.uint8)
    return Image.fromarray(tab1)


obraz2_1 = dwa_prostokaty_kolor(480, 320, 100, 80)
obraz2_1.save("obraz2_1.jpg")
obraz2_1.save("obraz2_1.png")


def rysuj_ramke_kolor(w, h, grub):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [25, 170, 200]
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = [(k+90) % 256,(k+50) % 256,(k+10) % 256]
    tab1 = tab.astype(np.uint8)
    return Image.fromarray(tab1)


obraz2_2 = rysuj_ramke_kolor(480, 320, 15)
obraz2_2.save("obraz2_2.jpg")
obraz2_2.save("obraz2_2.png")


def negatyw_kolor(obraz):
    tab = np.asarray(obraz)
    h, w, u = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            for u in range(3):
                tab_neg[i, j, u] = 255 - tab[i, j, u]
    return Image.fromarray(tab_neg)


obraz2_1N = negatyw_kolor(obraz2_1)
obraz2_1N.save("obraz2_1N.jpg")
obraz2_1N.save("obraz2_1N.png")

obraz2_2N = negatyw_kolor(obraz2_2)
obraz2_2N.save("obraz2_2N.jpg")
obraz2_2N.save("obraz2_2N.png")


def rysuj_pasy_poziome_kolor(obraz, grub):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    for u in range(h):
        for r in range(w):
            if t_obraz[u, r] == 1:
                tab[u, r] = [255, 255, 255]
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if (t_obraz[i, j] != 1) & (k % 2 == 0):
                    tab[i, j] = [10, 100, 150]
                if (t_obraz[i, j] != 1) & (k % 2 == 1):
                    tab[i, j] = [100, 100, 50]
    return Image.fromarray(tab)


inicjaly = Image.open("inicjaly.bmp")
obraz3 = rysuj_pasy_poziome_kolor(inicjaly, 10)
obraz3.save("obraz3.jpg")
obraz3.save("obraz3.png")

