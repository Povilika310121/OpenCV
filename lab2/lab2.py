import numpy
import cv2


def get_img():
    img = cv2.imread(r'2.jpg', flags=cv2.IMREAD_GRAYSCALE)
    h = int(img.shape[0])
    w = int(img.shape[1])
    return img, w, h


def show_img(img, img2):
    cv2.imshow('Display blur', img)
    cv2.imshow('Display origin', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


frame, width, heigth = get_img()

copyFrame = get_img()[0]
n = 5
gauss_matr = [[0] * n for i in range(n)]
a = n // 2
b = a
sigma = 0.001
sum = 0
# матрица свёртки
for i in range(0, n):
    for j in range(0, n):
        gauss_matr[i][j] = (1 / (2 * numpy.pi * (sigma ** 2))) * numpy.exp(
            -((i - a) ** 2 + (j - b) ** 2) / 2 * sigma ** 2)
        sum += gauss_matr[i][j]

# Нормируем матрицу
for i in range(n):
    for j in range(n):
        gauss_matr[i][j] /= sum
# грницы обхода
h_start = a
w_start = a
h_finish = heigth - a
w_finish = width - a

# Операция свертки
for i in range(h_start, h_finish):
    for j in range(w_start, w_finish):
        newVal = 0
        for k in range(n):
            for l in range(n):
                newVal = newVal + gauss_matr[k][l] * copyFrame[i - a + k][j - a + l]
        copyFrame[i][j] = newVal

show_img(copyFrame, frame)
