import numpy as np
from PIL import Image

# Zadanie 2

obrazek = Image.open("inicjaly.bmp")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# Zadanie 3

obrazek = Image.open("inicjaly.bmp")
dane_obrazka = np.asarray(obrazek)
dane_obrazka = dane_obrazka * 1

t1_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')

t1_text.close()

# Zadanie 4

#a

t1 = np.loadtxt("inicjaly.txt")

print("\ntyp danych tablicy:", t1.dtype)
print("rozmiar tablicy:", t1.shape)
print("liczba elementow:", t1.size)
print("wymiar tablicy:", t1.ndim)
print("rozmiar wyrazu tablicy:", t1.itemsize)

#b

print("\npierwszy wyraz:", dane_obrazka[30][50])
print("drugi wyraz:", dane_obrazka[40][90])
print("drugi wyraz:", dane_obrazka[0][99])

# Zadanie 5

t2 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
print("\ntyp danych tablicy:", t2.dtype)
print("rozmiar tablicy:", t2.shape)
print("liczba elementow:", t2.size)
print("wymiar tablicy:", t2.ndim)
print("rozmiar wyrazu tablicy:", t2.itemsize)
print(t2[30][50])
print(t2[40][90])

# Zadanie 6

t3 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("\ntyp danych tablicy:", t3.dtype)
print("rozmiar tablicy:", t3.shape)
print("liczba elementow:", t3.size)
print("wymiar tablicy:", t3.ndim)
print("rozmiar wyrazu tablicy:", t3.itemsize)
print(t3[30][50])
print(t3[40][90])

ob_d = Image.fromarray(t3)

ob_d.show()