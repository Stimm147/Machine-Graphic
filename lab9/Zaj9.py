from PIL import Image, ImageOps, ImageChops
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageStat as stat

# Zadanie 1

im = Image.open("zeby.png")
# im.show()

print(im.mode)

szary = im.convert('L')


# szary.show()

# Zadanie 2

# 2.1


def histogram_norm(obraz):
    s = stat.Stat(im)
    hist = obraz.histogram()
    for x in range(len(hist)):
        hist[x] = hist[x] / s.count[0]
    fig = plt.figure()
    plt.title("histogram ")
    plt.bar(range(256), hist[:], color='b', alpha=0.8)
    return fig, hist


# 2.2


def histogram_cumul(obraz):
    hist_cumul = []
    s = stat.Stat(im)
    hist_norm = obraz.histogram()
    for x in range(len(hist_norm)):
        hist_norm[x] = hist_norm[x] / s.count[0]
    for x in range(len(hist_norm)):
        temp = 0
        for y in range(x):
            temp = temp + hist_norm[y]
        hist_cumul.append(temp)
    fig = plt.figure()
    plt.title("histogram ")
    plt.bar(range(256), hist_cumul[:], color='b', alpha=0.8)
    return hist_cumul, fig


# 2.3


def histogram_equalization(obraz):
    hist_cumul, fig = histogram_cumul(obraz)
    obraz1 = obraz.point(lambda i: int(255 * hist_cumul[i]))
    return obraz1


normal = histogram_equalization(szary)
normal.save('equalized.png')

diff = ImageChops.difference(szary, normal)
# diff.show()


def make_histogram(obraz):
    hist = obraz.histogram()
    fig = plt.figure()
    plt.title("histogram ")
    plt.bar(range(256), hist[:], color='b', alpha=0.8)
    return fig


histogram_base = make_histogram(szary)
histogram_base.savefig('histogram_base.png')
a = Image.open('histogram_base.png')

histogram_base, nienie = histogram_norm(szary)
histogram_base.savefig('histogram_norm.png')
b = Image.open('histogram_norm.png')

aha, histogram_base = histogram_cumul(szary)
histogram_base.savefig('histogram_cumul.png')
c = Image.open('histogram_cumul.png')

histogram_eq = make_histogram(normal)
histogram_eq.savefig('histogram_eq.png')
d = Image.open('histogram_eq.png')

plt.figure(figsize=(30, 8))
plt.subplot(1, 4, 1)
plt.imshow(a, 'gray')
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(b, 'gray')
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(c, 'gray')
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(d, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig1.png')

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


statystyki(szary)
print('\n')
statystyki(normal)

# Zadanie 3

widok_equalized = ImageOps.equalize(im, mask=None)
widok_equalized.save('equalized1.png')

normal = histogram_equalization(szary)

plt.figure(figsize=(30, 8))
plt.subplot(1, 3, 1)
plt.imshow(szary, 'gray')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(normal, 'gray')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(widok_equalized, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig2.png')


def konwertuj1(obraz, w_r, w_g, w_b):
    obraz_cpy = obraz.copy()
    obraz_load = obraz_cpy.load()
    w, h = obraz.size
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            tab[y, x] = round(obraz_load[x, y][0] * w_r + obraz_load[x, y][1] * w_g + obraz_load[x, y][2] * w_b)
    return Image.fromarray(tab)


mgla = Image.open('mgla.jpg')
uuh = konwertuj1(mgla, 299/1000,  587/1000, 114/1000)
uuh.save('mgla_L1.png')

mgla2 = mgla.convert('L')
mgla2.save('mgla_L.png')

print('\n')
statystyki(uuh)
print('\n')
statystyki(mgla2)


def konwertuj1(obraz, w_r, w_g, w_b):
    obraz_cpy = obraz.copy()
    obraz_load = obraz_cpy.load()
    w, h = obraz.size
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            tab[y, x] = int(obraz_load[x, y][0] * w_r + obraz_load[x, y][1] * w_g + obraz_load[x, y][2] * w_b)
    return Image.fromarray(tab)


uuh2 = konwertuj1(mgla, 299/1000,  587/1000, 114/1000)
uuh2.save('mgla_L2.png')

mgla3 = mgla.convert('L')
mgla3.save('mgla_LL.png')

print('\n')
statystyki(uuh2)
print('\n')
statystyki(mgla3)