from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

# Zadanie 1

im = Image.open('diff.png')

# a


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # wyświetla max i min wartość pikseli
    print("count ", s.count)  # zlicza sumę wysokości i szerokości obrazka
    print("mean ", s.mean)  # srednia wartość pikseli
    print("median ", s.median)  # mediana wartości pikseli
    print("stddev ", s.stddev)  # odchylenie standardowe wartości pikseli


statystyki(im)

# b

hist = im.histogram()
p = 0
print(hist[p])
print(hist[256 + p])
print(hist[2*256 + p])


def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")


rysuj_histogram_RGB(im)


# c


def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent


zlicz, procent = zlicz_roznice_srednia_RGB(im, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz)
print('procent niepasujących pikseli = ' , procent)
zlicz1, procent1 = zlicz_roznice_srednia_RGB(im, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz1)
print('procent niepasujących pikseli = ' , procent1)
zlicz2, procent2 = zlicz_roznice_srednia_RGB(im, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz2)
print('procent niepasujących pikseli = ' , procent2)


def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

zlicz3, procent3 = zlicz_roznice_suma_RGB(im, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz3)
print('procent niepasujących pikseli = ' , procent3)
zlicz4, procent4 = zlicz_roznice_suma_RGB(im, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz4)
print('procent niepasujących pikseli = ' , procent4)
zlicz5, procent5 = zlicz_roznice_suma_RGB(im, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz5)
print('procent niepasujących pikseli = ' , procent5)

# Zadanie 2

# a

im1 = Image.open('obraz.jpg')
im1.save("obraz1.jpg")

# b

im2 = Image.open('obraz1.jpg')
im2.save("obraz2.jpg")
im3 = Image.open('obraz2.jpg')
im3.save("obraz3.jpg")
im4 = Image.open('obraz3.jpg')
im4.save("obraz4.jpg")
im5 = Image.open('obraz4.jpg')
im5.save("obraz5.jpg")

# c

roznice1 = ImageChops.difference(im1, im5)
statystyki(roznice1)
zlicz6, procent6 = zlicz_roznice_srednia_RGB(roznice1, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz6)
print('procent niepasujących pikseli = ' , procent6)
zlicz7, procent7 = zlicz_roznice_srednia_RGB(roznice1, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz7)
print('procent niepasujących pikseli = ' , procent7)
zlicz8, procent8 = zlicz_roznice_srednia_RGB(roznice1, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz8)
print('procent niepasujących pikseli = ' , procent8)

zlicz9, procent9 = zlicz_roznice_suma_RGB(roznice1, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz9)
print('procent niepasujących pikseli = ' , procent9)
zlicz10, procent10 = zlicz_roznice_suma_RGB(roznice1, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz10)
print('procent niepasujących pikseli = ' , procent10)
zlicz11, procent11 = zlicz_roznice_suma_RGB(roznice1, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz11)
print('procent niepasujących pikseli = ' , procent11)

# d

roznice2 = ImageChops.difference(im4, im5)
statystyki(roznice2)
zlicz12, procent12 = zlicz_roznice_srednia_RGB(roznice2, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz12)
print('procent niepasujących pikseli = ' , procent12)
zlicz13, procent13 = zlicz_roznice_srednia_RGB(roznice2, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz13)
print('procent niepasujących pikseli = ' , procent13)
zlicz14, procent14 = zlicz_roznice_srednia_RGB(roznice2, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz14)
print('procent niepasujących pikseli = ' , procent14)

zlicz15, procent15 = zlicz_roznice_suma_RGB(roznice2, 0)
print("odczyt dla współczynnika 0:")
print('liczba niepasujących pikseli = ' , zlicz15)
print('procent niepasujących pikseli = ' , procent15)
zlicz16, procent16 = zlicz_roznice_suma_RGB(roznice2, 10)
print("odczyt dla współczynnika 10:")
print('liczba niepasujących pikseli = ' , zlicz16)
print('procent niepasujących pikseli = ' , procent16)
zlicz17, procent17 = zlicz_roznice_suma_RGB(roznice2, 20)
print("odczyt dla współczynnika 20:")
print('liczba niepasujących pikseli = ' , zlicz17)
print('procent niepasujących pikseli = ' , procent17)

# Zadanie 3


def ukryj_kod(obraz, im_kod):
    t_obraz = np.asarray(obraz)
    t_kodowany = t_obraz.copy()
    h, w, d = t_obraz.shape
    t_kod = np.asarray(im_kod)
    for i in range(h):
        for j in range(w):
            if t_kod[i, j] > 0:
                k = randint(0,2)
                t_kodowany[i, j, k] = t_obraz[i, j, k] + 1
    return Image.fromarray(t_kodowany)


# a


def odkoduj(obraz1,obraz2):

    tab = np.asarray(obraz1)
    h, w, u = tab.shape
    tab2 = np.asarray(obraz2)
    t = (h, w, u)
    tab3 = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if tab[i, j, 0] != tab2[i, j, 0]:
                tab3[i, j, 0] = 255

            if tab[i, j, 1] != tab2[i, j, 1]:
                tab3[i, j, 0] = 255

            if tab[i, j, 2] != tab2[i, j, 2]:
                tab3[i, j, 0] = 255

    tab4 = tab3[:, :, 0]
    return Image.fromarray(tab4)

# b


im_kodowany = Image.open('jesien.jpg')
im_zakodowany2 = Image.open('zakodowany2.bmp')

rezultat = odkoduj(im_kodowany,im_zakodowany2)
# print("tryb:", rezultat.mode)
rezultat.save("kod2.bmp")