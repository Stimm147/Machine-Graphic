from PIL import Image
import math
import numpy as np

im = Image.open("obraz.jpg")


def rysuj_kwadrat_max(obraz, m, n, k): # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp_r = []
    temp_g = []
    temp_b = []
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp_r.append(pixel[0])
            temp_g.append(pixel[1])
            temp_b.append(pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (max(temp_r), max(temp_g), max(temp_b))
    return obraz1


obraz1 = rysuj_kwadrat_max(im, 300, 150, 50)
obraz2 = rysuj_kwadrat_max(obraz1, 50, 100, 50)
obraz3 = rysuj_kwadrat_max(obraz2, 250, 300, 50)
obraz3.save("obraz1.png")


def rysuj_kwadrat_min(obraz, m, n, k): # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp_r = []
    temp_g = []
    temp_b = []
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp_r.append(pixel[0])
            temp_g.append(pixel[1])
            temp_b.append(pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (min(temp_r), min(temp_g), min(temp_b))
    return obraz1


obraz1 = rysuj_kwadrat_min(im, 310, 130, 20)
obraz2 = rysuj_kwadrat_min(obraz1, 460, 10, 20)
obraz3 = rysuj_kwadrat_min(obraz2, 420, 350, 20)
obraz3.save("obraz2.png")


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def kopiuj_kolo(obraz, m_s, n_s, m_d, n_d, r):
    obraz1 = obraz.copy()
    obraz_cpy = obraz1.load()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2:
            obraz1.putpixel((i, j), (obraz_cpy[i + m_d - m_s, j + n_d - n_s][0], obraz_cpy[i + m_d - m_s, j + n_d - n_s][1], obraz_cpy[i + m_d - m_s, j + n_d - n_s][2]))
    return obraz1


nie = kopiuj_kolo(im, 60, 60, 330, 120, 60)
nie2 = kopiuj_kolo(nie, 555, 60, 330, 120, 60)
nie3 = kopiuj_kolo(nie2, 60, 350, 330, 120, 60)
nie4 = kopiuj_kolo(nie3, 555, 350, 330, 120, 60)
nie.save("obraz3.png")
nie4.save("obraz4.png")


def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img


def odbij_w_pionie2(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1 - i, j]
    return img


