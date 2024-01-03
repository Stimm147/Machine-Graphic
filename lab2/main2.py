from PIL import Image
import numpy as np


# Zadanie 1


def rysuj_ramke_w_obrazie(obraz, grub):
    obraz_wstawiany = np.asarray(obraz) * 1
    h, w = obraz_wstawiany.shape
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j] = 0
        for j in range(w - grub, w):
            obraz_wstawiany[i][j] = 0
    for i in range(w):
        for j in range(grub):
            obraz_wstawiany[j][i] = 0
        for j in range(h - grub, h):
            obraz_wstawiany[j][i] = 0
    tab = obraz_wstawiany.astype(bool)
    return Image.fromarray(tab)


# Zadanie 2

inicjaly = Image.open("inicjaly.bmp")

inicjaly_paski1 = rysuj_ramke_w_obrazie(inicjaly, 10)

inicjaly_paski1.save("ramka10.bmp")

inicjaly_paski2 = rysuj_ramke_w_obrazie(inicjaly, 5)

inicjaly_paski2.save("ramka5.bmp")


# Zadanie 3.1


def rysuj_ramke(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(min(w, h) / (grub * 2))
    for k in range(ile):
        tab[grub * k:h - grub * k, grub * k:w - grub * k] = k % 2
    tab1 = tab.astype(np.bool_)

    return Image.fromarray(tab1)


# tab = rysuj_ramke(120, 60, 3)
# im_ramka = Image.fromarray(tab)
# im_ramka.show()
# im_ramka.save("uuh.bmp")

# Zadanie 3.2

def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)


# obraz = rysuj_pasy_pionowe(180, 100, 15)
# im_ramka2 = Image.fromarray(obraz)
# im_ramka2.show()

# Zadanie 3.3

def dwa_prostokaty(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(n):
        for j in range(m):
            tab[i][j] = 0
    for i in range(n, h):
        for j in range(m, w):
            tab[i][j] = 0
    tab1 = tab.astype(np.bool_)

    return Image.fromarray(tab1)


# uuh = dwa_prostokaty(180, 100, 70, 110)
# im_ramka3 = Image.fromarray(uuh)
# im_ramka3.show()

# Zadanie 4


zad31 = rysuj_ramke(480, 320, 10)
# zad31.show()
zad31.save("zad31.bmp")

zad32 = rysuj_pasy_pionowe(480, 320, 10)
# zad32.show()
zad32.save("zad32.bmp")

zad33 = dwa_prostokaty(480, 320, 100, 50)
# zad33.show()
zad33.save("zad33.bmp")

# Zadanie 5


def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz = np.asarray(obraz_bazowy) * 1
    h1, w1 = tab_obraz.shape
    tab_obraz2 = np.asarray(obraz_wstawiany) * 1
    h2, w2 = tab_obraz2.shape

    if (w2 + m > w1) & (h2 + n <= h1):
        for i in range(h2):
            for j in range(w1 - m):
                tab_obraz[i + n][j + m] = tab_obraz2[i][j]
    elif (w2 + m <= w1) & (h2 + n > h1):
        for i in range(h1 - n):
            for j in range(w2):
                tab_obraz[i + n][j + m] = tab_obraz2[i][j]
    elif (w2 + m > w1) & (h2 + n > h1):
        for i in range(h1 - n):
            for j in range(w1 - m):
                tab_obraz[i + n][j + m] = tab_obraz2[i][j]
    elif (w2 + m <= w1) & (h2 + n <= h1):
        for i in range(h2):
            for j in range(w2):
                tab_obraz[i + n][j + m] = tab_obraz2[i][j]

    tab = tab_obraz.astype(bool)

    return Image.fromarray(tab)


obrazek1 = Image.open("zad32.bmp")
zad_51 = wstaw_obraz_w_obraz(obrazek1, inicjaly, 300, 90)
zad_52 = wstaw_obraz_w_obraz(obrazek1, inicjaly, 10, 290)
zad_51.save("wstaw1.bmp")
zad_52.save("wstaw2.bmp")
