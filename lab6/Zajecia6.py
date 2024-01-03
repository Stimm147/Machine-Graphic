from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1

obraz = Image.open('obraz.jpg')
obraz_cpy = obraz.copy()
inicjaly = Image.open("inicjaly.bmp")
czarno_bialy = Image.open("ramka5.bmp")

# Zadanie 2
# a


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):

    obraz_cpy = obraz.copy()
    inicjaly_tab = np.asarray(inicjaly)
    w_z, h_z = inicjaly.size

    for i in range(h_z):
        for j in range(w_z):
            if inicjaly_tab[i, j] == 0:
                obraz_cpy.putpixel((j + m, i + n), kolor)
    return obraz_cpy


wstawione_inicjaly = wstaw_inicjaly(obraz_cpy, inicjaly, -100, -50, (255, 0, 0))
wstawione_inicjaly.save("obraz1.png")

# b


def wstaw_inicjaly_maska(obraz, inicjaly, m, n, a, b, c):

    obraz_cpy = obraz.copy()
    inicjaly_tab = np.asarray(inicjaly)
    w_z, h_z = inicjaly.size

    for i in range(h_z):
        for j in range(w_z):
            p = obraz.getpixel((j+m, i+n))
            if inicjaly_tab[i, j] == 0:
                obraz_cpy.putpixel((j + m, i + n), (p[0]+a, p[1]+b, p[2]+c))
    return obraz_cpy


obraz_z_maska = wstaw_inicjaly_maska(obraz_cpy, inicjaly, 250, 200, -50, 100, 80)
obraz_z_maska.save("obraz2.png")

# Zadanie 3


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):

    obraz_cpy = obraz.copy()

    inicjaly_tab = inicjaly.load()
    obraz_cpy_tab = obraz_cpy.load()

    w, h = obraz.size
    w_z, h_z = inicjaly.size

    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            if inicjaly_tab[i, j] == 0:
                obraz_cpy_tab[i + m, j + n] = kolor
    return obraz_cpy


nienie = wstaw_inicjaly_load(obraz_cpy, inicjaly, -100, -50, (255, 0, 0))
# nienie.show()


def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, a, b, c):

    obraz_cpy = obraz.copy()

    inicjaly_tab = inicjaly.load()
    obraz_cpy_tab = obraz_cpy.load()

    w, h = obraz.size
    w_z, h_z = inicjaly.size

    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            if inicjaly_tab[i, j] == 0:
                obraz_cpy_tab[i + m, j + n] = (obraz_cpy_tab[i + m,j + n][0] + a, obraz_cpy_tab[i + m,j + n][1] + b, obraz_cpy_tab[i + m, j + n][2] + c)
    return obraz_cpy


eoeo = wstaw_inicjaly_maska_load(obraz_cpy, inicjaly, 250, 200, -50, 100, 80)
# eoeo.show()


# Zadanie 4
# a


def kontrast(obraz, wsp_kontrastu):
    if 0 <= wsp_kontrastu <= 100:
        mn = ((255 + wsp_kontrastu) / 255) ** 2
    if 0 > wsp_kontrastu:
        mn = ((255 + 0) / 255) ** 2
    if 100 < wsp_kontrastu:
        mn = ((255 + 100) / 255) ** 2
    return obraz.point(lambda i: 128 + (i -128) * mn)


kontrast1 = kontrast(obraz,33)
kontrast2 = kontrast(obraz,66)
kontrast3 = kontrast(obraz,99)

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(kontrast1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(kontrast2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(kontrast3)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')

# b


def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: 255 * np.log(1 + i / 255))


def filtr_liniowy(image, a, b):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0] * a + b, pixele[i, j][1] * a + b, pixele[i, j][2] * a + b)


filtr = obraz.copy()
filtr_liniowy(filtr, 2, 100)

t_l = transformacja_logarytmiczna(obraz)


plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(filtr)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(t_l)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

# c


def transformacja_gamma(obraz, gamma):
    if 0 > gamma:
        gamma = 0
    if 100 < gamma:
        gamma = 100
    return obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)


gamma1 = transformacja_gamma(obraz_cpy, 3.14)
gamma2 = transformacja_gamma(obraz_cpy, 20)
gamma3 = transformacja_gamma(obraz_cpy, 89)

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(obraz)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(gamma1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(gamma2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(gamma3)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')

# Zadanie 5


T = np.array(obraz, dtype='uint8')
print(T[16,55])
T += 100
obraz_wynik = Image.fromarray(T, "RGB")

obraz_wynik2 = obraz_cpy.point(lambda i: i + 100)

Y = np.array(obraz_wynik2, dtype="uint8")
H = np.array(obraz_wynik, dtype="uint8")

print(Y[16,55])
print(H[16,55])

roznica = ImageChops.difference(obraz_wynik, obraz_wynik2)

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(obraz_wynik)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(obraz_wynik2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(roznica)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig_4.png')

# Zadanie 6


def zmien_jasnosc(obraz, wartosc):
    w, h = obraz.size
    pixele = obraz.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0] + wartosc, pixele[i, j][1] + wartosc, pixele[i, j][2] + wartosc)


kopia = obraz.copy()
zmien_jasnosc(kopia, 100)

