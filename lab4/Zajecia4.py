from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# Zadanie 1

im1 = Image.open('obraz.jpg')

# Zadanie 2

# a

T = np.array(im1)
tab_r = T[:, :, 0]
im_r = Image.fromarray(tab_r)
tab_g = T[:, :, 1]
im_g = Image.fromarray(tab_g)
tab_b = T[:, :, 2]
im_b = Image.fromarray(tab_b)

# b

im2 = Image.merge('RGB', (im_r, im_g, im_b))

porownanie = ImageChops.difference(im1, im2)

# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(im2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(porownanie)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')

# Zadanie 3

r, g, b = im1.split()
im3 = Image.merge('RGB', (r, b, g))

# a

im3.save("im3.jpg")
im3.save("im3.png")

# b

im3_1 = Image.open('im3.jpg')
im3_2 = Image.open('im3.png')
im3_diff = ImageChops.difference(im3_1, im3_2)

# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im3_1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(im3_2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(im3_diff)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

# Zadanie 4

obraz1_1jpg = Image.open('obraz1_1.jpg')
obraz1_1png = Image.open('obraz1_1.png')
obraz1_1diff = ImageChops.difference(obraz1_1jpg, obraz1_1png)
obraz1_1Njpg = Image.open('obraz1_1.jpg')
obraz1_1Npng = Image.open('obraz1_1.png')
obraz1_1Ndiff = ImageChops.difference(obraz1_1Njpg, obraz1_1Npng)
obraz1_2jpg = Image.open('obraz1_2.jpg')
obraz1_2png = Image.open('obraz1_2.png')
obraz1_2diff = ImageChops.difference(obraz1_2jpg, obraz1_2png)
obraz1_2Njpg = Image.open('obraz1_2N.jpg')
obraz1_2Npng = Image.open('obraz1_2N.png')
obraz1_2Ndiff = ImageChops.difference(obraz1_2Njpg, obraz1_2Npng)

plt.figure(figsize=(32, 16))
plt.subplot(4, 3, 1)
plt.imshow(obraz1_1jpg, "gray")
plt.axis('off')
plt.subplot(4, 3, 2)
plt.imshow(obraz1_1png, "gray")
plt.axis('off')
plt.subplot(4, 3, 3)
plt.imshow(obraz1_1diff, "gray")
plt.axis('off')
plt.subplot(4, 3, 4)
plt.imshow(obraz1_1Njpg, "gray")
plt.axis('off')
plt.subplot(4, 3, 5)
plt.imshow(obraz1_1Npng, "gray")
plt.axis('off')
plt.subplot(4, 3, 6)
plt.imshow(obraz1_1Ndiff, "gray")
plt.axis('off')
plt.subplot(4, 3, 7)
plt.imshow(obraz1_2jpg, "gray")
plt.axis('off')
plt.subplot(4, 3, 8)
plt.imshow(obraz1_2png, "gray")
plt.axis('off')
plt.subplot(4, 3, 9)
plt.imshow(obraz1_2diff, "gray")
plt.axis('off')
plt.subplot(4, 3, 10)
plt.imshow(obraz1_2Njpg, "gray")
plt.axis('off')
plt.subplot(4, 3, 11)
plt.imshow(obraz1_2Npng, "gray")
plt.axis('off')
plt.subplot(4, 3, 12)
plt.imshow(obraz1_2Ndiff, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')

# Zadanie 5

tab1 = np.array(obraz1_1png)
im4 = Image.fromarray(tab1)

# a

im4_1 = Image.merge('RGB', (r, g, im4))

im4_2 = Image.merge('RGB', (r, im4, b))

im4_3 = Image.merge('RGB', (im4, g, b))

# b

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im4_1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(im4_2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(im4_3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig4.png')

# Zadanie 6

# a

kanal1 = Image.open('kanal1.png')
T = np.array(kanal1)
tab_5_1 = T[:, :, 0]
im5_1 = Image.fromarray(tab_5_1)
kanal2 = Image.open('kanal2.png')
T = np.array(kanal2)
tab_5_2 = T[:, :, 0]
im5_2 = Image.fromarray(tab_5_2)
kanal3 = Image.open('kanal3.png')
T = np.array(kanal3)
tab_5_3 = T[:, :, 0]
im5_3 = Image.fromarray(tab_5_3)

# b

im5__1 = Image.merge('RGB', (im5_1, im5_2, im5_3))
im5__2 = Image.merge('RGB', (im5_1, im5_3, im5_2))
im5__3 = Image.merge('RGB', (im5_2, im5_1, im5_3))
im5__4 = Image.merge('RGB', (im5_2, im5_3, im5_1))
im5__5 = Image.merge('RGB', (im5_3, im5_1, im5_2))
im5__6 = Image.merge('RGB', (im5_3, im5_2, im5_1))

plt.figure(figsize=(32, 16))
plt.subplot(3, 2, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im5__1)
plt.axis('off')
plt.subplot(3, 2, 2)
plt.imshow(im5__2)
plt.axis('off')
plt.subplot(3, 2, 3)
plt.imshow(im5__3)
plt.axis('off')
plt.subplot(3, 2, 4)
plt.imshow(im5__4)
plt.axis('off')
plt.subplot(3, 2, 5)
plt.imshow(im5__5)
plt.axis('off')
plt.subplot(3, 2, 6)
plt.imshow(im5__6)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig5.png')

test_caly_czarny = ImageChops.difference(im1, im2)
test_nie_do_konca_czarny = ImageChops.difference(im3_1, im3_2)

# Zadanie 7

def czy_czarny_jest_czarny_kolor(obraz):
    tab = np.asarray(obraz)
    h, w, u = tab.shape
    for i in range(h):
        for j in range(w):
            for u in range(u):
                if tab[i, j, u] != 0:
                    return False
    return True

def czy_czarny_jest_czarny_szary(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    for i in range(h):
        for j in range(w):
            if tab[i, j] != 0:
                return False
    return True


print(czy_czarny_jest_czarny_kolor(test_caly_czarny))
print(czy_czarny_jest_czarny_kolor(test_nie_do_konca_czarny))
print(czy_czarny_jest_czarny_szary(obraz1_1diff))
print(czy_czarny_jest_czarny_kolor(im3_diff))

print(czy_czarny_jest_czarny_szary(obraz1_1diff))
print(czy_czarny_jest_czarny_szary(obraz1_1Ndiff))
print(czy_czarny_jest_czarny_szary(obraz1_2diff))
print(czy_czarny_jest_czarny_szary(obraz1_2Ndiff))