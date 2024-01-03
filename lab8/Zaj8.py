from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt

im = Image.open("obraz.jpg")
im_cpy = im.copy()

# Zadanie 1


def filtruj(obraz, kernel, scale):
    obraz1 = obraz.copy()
    kopia1 = obraz.load()
    kopia2 = obraz1.load()
    w, h = obraz.size
    d = int(len(kernel)/2)
    # temp = [0,0,0]
    for i in range(d, w-d):
        for j in range(d, h - d):
            temp = [0, 0, 0]
            for x in range(-d, d + 1):
                for y in range(-d, d + 1):
                    pix = kopia1[i+x, j+y]
                    temp[0] += pix[0] * kernel[x + d][y + d]
                    temp[1] += pix[1] * kernel[x + d][y + d]
                    temp[2] += pix[2] * kernel[x + d][y + d]
            if scale != 0:
                temp[0] = temp[0] / scale
                temp[1] = temp[1] / scale
                temp[2] = temp[2] / scale
            kopia2[i, j] = (int(temp[0]), int(temp[1]), int(temp[2]))
    return obraz1


# Zadanie 2
# a

blur1 = im_cpy.filter(ImageFilter.BLUR)

# b

parametry = ImageFilter.BLUR.filterargs
print(parametry)

kernel2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

im_cpy2 = im.copy()

blur2 = filtruj(im_cpy2, kernel2, 16)

# c

blur_diff = ImageChops.difference(blur1, blur2)

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(im)
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(blur1)
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(blur2)
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(blur_diff)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')

# Zadanie 3

im_cpy3 = im.copy()
im_l = im_cpy3.convert('L')

# a

im_cpy4 = im_l.copy()
emboss1 = im_cpy4.filter(ImageFilter.EMBOSS)

# b

parametry2 = ImageFilter.EMBOSS.filterargs
print(parametry2)

SOBEL1 = ((3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
SOBEL2 = ((3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))

ImageFilter.EMBOSS.filterargs = SOBEL1

im_cpy5 = im_l.copy()
im_SOBEL1 = im_cpy5.filter(ImageFilter.EMBOSS)

ImageFilter.EMBOSS.filterargs = SOBEL2

im_cpy6 = im_l.copy()
im_SOBEL2 = im_cpy6.filter(ImageFilter.EMBOSS)

# c

plt.figure(figsize=(32, 16))
plt.subplot(1, 4, 1)
plt.imshow(im_l, 'gray')
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(emboss1, 'gray')
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(im_SOBEL1, 'gray')
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(im_SOBEL2, 'gray')
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

# Zadanie 4

# DETAIL
# EDGE_ENHANCE_MORE
# SHARPEN
# SMOOTH_MORE

im_cpy7 = im.copy()
im_cpy8 = im.copy()
im_cpy9 = im.copy()
im_cpy10 = im.copy()

im_detail = im_cpy7.filter(ImageFilter.DETAIL)
im_detail_diff = ImageChops.difference(im, im_detail)

im_edge = im_cpy8.filter(ImageFilter.EDGE_ENHANCE_MORE)
im_edge_diff = ImageChops.difference(im, im_edge)

im_sharpen = im_cpy9.filter(ImageFilter.SHARPEN)
im_sharpen_diff = ImageChops.difference(im, im_sharpen)

im_smooth = im_cpy10.filter(ImageFilter.SMOOTH_MORE)
im_smooth_diff = ImageChops.difference(im, im_smooth)

plt.figure(figsize=(16, 16))
plt.subplot(4, 2, 1)
plt.imshow(im_detail)
plt.title("DETAIL")
plt.axis('off')
plt.subplot(4, 2, 2)
plt.imshow(im_detail_diff)
plt.axis('off')
plt.subplot(4, 2, 3)
plt.title("EDGE_ENHANCE_MORE")
plt.imshow(im_edge)
plt.axis('off')
plt.subplot(4, 2, 4)
plt.imshow(im_edge_diff)
plt.axis('off')
plt.subplot(4, 2, 5)
plt.title("SHARPEN")
plt.imshow(im_sharpen)
plt.axis('off')
plt.subplot(4, 2, 6)
plt.imshow(im_sharpen_diff)
plt.axis('off')
plt.subplot(4, 2, 7)
plt.title("SMOOTH_MORE")
plt.imshow(im_smooth)
plt.axis('off')
plt.subplot(4, 2, 8)
plt.imshow(im_smooth_diff)
plt.axis('off')
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig3.png')

# Zadanie 5

# 11.BoxBlur

# PIL.ImageFilter.BoxBlur() Blurs the image by setting each pixel to the average value of the pixels in a square box
# extending radius pixels in each direction.
# Supports float radius of arbitrary size.
# Uses an optimized implementation which runs in linear time relative to the size of the image for any radius value.

# do funkcji przekazujemy moc blura (szerokość jądra)

im_cpy11 = im.copy()
im_boxblur = im_cpy11.filter(ImageFilter.BoxBlur(8))
im_boxblur_diff = ImageChops.difference(im, im_boxblur)

# 12.GaussianBlur

# do funkcji przekazujemy moc blura (szerokość jądra) w formie "radius = 5"

im_cpy12 = im.copy()
im_gausblur = im_cpy12.filter(ImageFilter.GaussianBlur(radius = 5))
im_gausblur_diff = ImageChops.difference(im, im_gausblur)

# 13.UnsharpMask

# Syntax: PIl.ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)
# Parameters:
# radius: Blur Radius
# percent: Unsharp strength, in percent
# threshold: Threshold controls the minimum brightness change that will be sharpened

im_cpy13 = im.copy()
im_unsharp = im_cpy13.filter(ImageFilter.UnsharpMask(radius = 4, percent = 500, threshold = 8))
im_unsharp_diff = ImageChops.difference(im, im_unsharp)

# 14.Kernel

# The current version only supports 3×3 and 5×5 integer and floating point kernels.

# Syntax: PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0)
# Parameters:
# size – Kernel size, given as (width, height). In the current version, this must be (3, 3) or (5, 5).
# kernel – A sequence containing kernel weights.
# scale – Scale factor. If given, the result for each pixel is divided by this value. the default is the sum of
# the kernel weights.
# offset – Offset. If given, this value is added to the result, after it has been divided by the scale factor.

im_cpy14 = im.copy()
im_kernel = im_cpy14.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 11, -2, -2, -2, -2), 1, 0))
im_kernel_diff = ImageChops.difference(im, im_kernel)

# 15.RankFilter

# Syntax: PIL.ImageFilter.RankFilter(size, rank)
#
# Parameters:
# size: The kernel size, in pixels.
# rank: What pixel value to pick. Use 0 for a min filter, size * size / 2 for a median filter, size * size – 1
# for a max filter, etc.

im_cpy15 = im.copy()
im_rank = im_cpy15.filter(ImageFilter.RankFilter(size = 3, rank = (3 * 3)//2))
im_rank_diff = ImageChops.difference(im, im_rank)

# 16.MedianFilter

# method creates a median filter. Picks the median pixel value in a window with the given size.
#
# Syntax: PIL.ImageFilter.MedianFilter(size=3)
#
# Parameters:
# size: The kernel size, in pixels.

im_cpy16 = im.copy()
im_median = im_cpy16.filter(ImageFilter.MedianFilter(size = 3))
im_median_diff = ImageChops.difference(im, im_median)

# 17.MinFilter

# Syntax: PIL.ImageFilter.MinFilter(size=3)
#
# Parameters:
# size: The kernel size, in pixels.

im_cpy17 = im.copy()
im_min = im_cpy17.filter(ImageFilter.MinFilter(size = 3))
im_min_diff = ImageChops.difference(im, im_min)

# 18.MaxFilter

# Syntax: PIL.ImageFilter.MaxFilter(size=3)
#
# Parameters:
# size: The kernel size, in pixels.

im_cpy18 = im.copy()
im_max = im_cpy18.filter(ImageFilter.MaxFilter(size = 3))
im_max_diff = ImageChops.difference(im, im_max)

plt.figure(figsize=(16, 32))
plt.subplot(8, 2, 1)
plt.imshow(im_boxblur)
plt.title("BoxBlur - ImageFilter.BoxBlur(8)")
plt.axis('off')
plt.subplot(8, 2, 2)
plt.imshow(im_boxblur_diff)
plt.axis('off')
plt.subplot(8, 2, 3)
plt.imshow(im_gausblur)
plt.title("GaussianBlur - ImageFilter.GaussianBlur(radius = 5)")
plt.axis('off')
plt.subplot(8, 2, 4)
plt.imshow(im_gausblur_diff)
plt.axis('off')
plt.subplot(8, 2, 5)
plt.imshow(im_unsharp)
plt.title("UnsharpMask - ImageFilter.UnsharpMask(radius = 4, percent = 500, threshold = 8)")
plt.axis('off')
plt.subplot(8, 2, 6)
plt.imshow(im_unsharp_diff)
plt.axis('off')
plt.subplot(8, 2, 7)
plt.imshow(im_kernel)
plt.title("Kernel - ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 11, -2, -2, -2, -2), 1, 0)")
plt.axis('off')
plt.subplot(8, 2, 8)
plt.imshow(im_kernel_diff)
plt.axis('off')
plt.subplot(8, 2, 9)
plt.imshow(im_rank)
plt.title("RankFilter - ImageFilter.RankFilter(size = 3, rank = (3 * 3)//2)")
plt.axis('off')
plt.subplot(8, 2, 10)
plt.imshow(im_rank_diff)
plt.axis('off')
plt.subplot(8, 2, 11)
plt.imshow(im_median)
plt.title("MedianFilter - ImageFilter.MedianFilter(size = 3)")
plt.axis('off')
plt.subplot(8, 2, 12)
plt.imshow(im_median_diff)
plt.axis('off')
plt.subplot(8, 2, 13)
plt.imshow(im_min)
plt.title("MinFilter - ImageFilter.MinFilter(size = 3)")
plt.axis('off')
plt.subplot(8, 2, 14)
plt.imshow(im_min_diff)
plt.axis('off')
plt.subplot(8, 2, 15)
plt.imshow(im_max)
plt.title("MaxFilter - ImageFilter.MaxFilter(size = 3)")
plt.axis('off')
plt.subplot(8, 2, 16)
plt.imshow(im_max_diff)
plt.axis('off')
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig4.png')
