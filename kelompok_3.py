# -*- coding: utf-8 -*-
"""Kelompok 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QuQeacjwMWIbxCJp98lEf6OzGHXYtj0Y

# **Judul: Implementasi Image Processing Menggunakan 7 Langkah Pemrosesan Gambar**

### **KELOMPOK 3:**
1.   EKA SETYA NINGSING - 221011400399
2.   KEZIA PATRICIA ZEFANYA - 221011402076
3.   MOCHAMMAD IQBAL SUYUDI W. - 221011400378
4.   MU'AMMAR KURNIAWAN - 221011400390
5.   MUHAMMAD MICKO BIAGI - 221011400396

# **Tujuan Proyek**

### **Proyek ini bertujuan untuk:**

*   Menerapkan 7 teknik dasar image processing pada satu gambar.
*   Memberikan pemahaman komprehensif tentang manipulasi gambar, termasuk kecerahan, konversi skala abu-abu, blurring, dan zoom.
*   Menghasilkan solusi interaktif yang ramah pengguna, seperti slider untuk kecerahan dan zoom.
"""

from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Membuka gambar kelompok3.png
img = cv2.imread('kelompok3.png')

# Menampilkan gambar asli
print("Gambar Asli:")
cv2_imshow(img)

"""## **Open Image**

Membuka gambar contoh "kelompok3.png" menggunakan OpenCV sebagai input utama.
"""

# Konversi gambar ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menampilkan gambar grayscale
print("Gambar Grayscale:")
cv2_imshow(gray)

# Menyimpan hasil grayscale
cv2.imwrite('kelompok3_grayscale.png', gray)

"""## **Grayscale (Konversi Skala Abu-abu)**

Gambar dikonversi ke skala abu-abu untuk menghilangkan informasi warna, yang memudahkan analisis struktur gambar.
"""

# Menerapkan Gaussian Blur
blur = cv2.GaussianBlur(img, (15, 15), 0)

# Menampilkan gambar hasil blur
print("Gambar Blurring:")
cv2_imshow(blur)

# Menyimpan hasil blur
cv2.imwrite('kelompok3_blur.png', blur)

"""## **Blurring (Pengaburan)**

Gambar diberi efek blur menggunakan filter Gaussian untuk mengurangi noise dan detail yang berlebihan.
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Membaca gambar input
img = cv2.imread('kelompok3.png')

# Menentukan koordinat area blur secara lebih presisi
x1, y1 = 1430, 100  # Kiri atas (x1, y1)
x2, y2 = 2000, 1200  # Kanan bawah (x2, y2)

# Membuat salinan gambar
img_blur = img.copy()

# Mengambil area wajah (ROI - Region of Interest)
roi = img_blur[y1:y2, x1:x2]

# Menerapkan Gaussian Blur hanya pada area wajah
roi_blur = cv2.GaussianBlur(roi, (55, 55), 0)

# Mengembalikan area blur ke gambar asli
img_blur[y1:y2, x1:x2] = roi_blur

# Menampilkan hasil blur fokus
print("Gambar dengan area blur pada wajah M. Micko Biagi:")
cv2_imshow(img_blur)

# Menyimpan hasil gambar
cv2.imwrite('kelompok3_blur_micko_fix.png', img_blur)
print("Hasil blur disimpan sebagai 'kelompok3_blur_micko_fix.png'")

"""## **Blurring Focus (Fokus Pengaburan)**

Gambar diberi efek blur menggunakan filter Gaussian untuk mengurangi noise dan detail yang berlebihan pada sisi tertentu.
"""

# Menentukan faktor zoom out (contoh: 0.5x pengecilan)
zoom_out_scale = 0.2

# Menghitung dimensi baru
new_width = int(width * zoom_out_scale)
new_height = int(height * zoom_out_scale)

# Resize gambar untuk Zoom Out
zoom_out = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Menampilkan hasil Zoom Out
print("Gambar Zoom Out (0.5x):")
cv2_imshow(zoom_out)

# Menyimpan hasil gambar Zoom Out
cv2.imwrite('kelompok3_zoom_out.png', zoom_out)
print("Hasil Zoom Out disimpan sebagai 'kelompok3_zoom_out.png'")

"""## **Zoom Out**

Zoom Out: Mengecilkan gambar untuk melihat keseluruhan struktur dalam satu tampilan.
"""

import cv2
from google.colab.patches import cv2_imshow

# Membaca gambar
img = cv2.imread('kelompok3.png')

# Menentukan koordinat area fokus (contoh wajah tengah, Mu'ammar K.)
# Koordinat kiri atas (x1, y1) dan kanan bawah (x2, y2) - Sesuaikan dengan gambar
x1, y1 = 730, 350  # Kiri atas
x2, y2 = 1170, 1100  # Kanan bawah

# Crop area fokus (wajah)
cropped = img[y1:y2, x1:x2]

# Memperbesar hasil crop dengan faktor 2x
zoom_in = cv2.resize(cropped, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

# Menampilkan hasil Zoom In
print("Gambar Zoom In Fokus (Crop dan Perbesar):")
cv2_imshow(zoom_in)

# Menyimpan hasil Zoom In
cv2.imwrite('kelompok3_zoom_in_focus.png', zoom_in)
print("Hasil Zoom In disimpan sebagai 'kelompok3_zoom_in_focus.png'")

"""## **Zoom In**

Zoom In: Memperbesar gambar hingga beberapa kali lipat untuk menampilkan detail gambar dengan interpolasi berkualitas tinggi.
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from ipywidgets import interact, FloatSlider

# Membaca gambar
img = cv2.imread('kelompok3.png')

# Fungsi untuk Zoom In dan Zoom Out
def zoom(scale):
    # Menghitung dimensi baru berdasarkan skala
    height, width = img.shape[:2]
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize gambar dengan skala
    zoomed_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC)

    # Jika Zoom In (lebih besar), crop bagian tengah agar pas layar
    if scale > 1:
        center_x, center_y = new_width // 2, new_height // 2
        crop_size_x, crop_size_y = width, height
        zoomed_img = zoomed_img[center_y - crop_size_y // 2:center_y + crop_size_y // 2,
                                center_x - crop_size_x // 2:center_x + crop_size_x // 2]

    # Menampilkan gambar hasil zoom
    print(f"Faktor Zoom: {scale}x")
    cv2_imshow(zoomed_img)

# Slider interaktif untuk Zoom In (1x - 5x) dan Zoom Out (0.1x - 1x)
print("Geser slider ke kanan untuk Zoom In (memperbesar), ke kiri untuk Zoom Out (mengecilkan):")
interact(zoom, scale=FloatSlider(min=0.1, max=5, step=0.1, value=1))

"""## **Interaktif Zoom In/Out dengan Slider**

- Fitur interaktif memungkinkan pengguna memperbesar dan memperkecil gambar menggunakan slider di Google Colab.
- Slider dapat mengatur skala antara 0.1x (Zoom Out) hingga 5x (Zoom In).
"""

# Flip Horizontal
flip_horizontal = cv2.flip(img, 1)

# Menampilkan hasil flip
print("Gambar Flip Horizontal:")
cv2_imshow(flip_horizontal)

# Menyimpan hasil flip
cv2.imwrite('kelompok3_flip_horizontal.png', flip_horizontal)

"""## **Flip Horizontal**

Melakukan pembalikan gambar secara horizontal untuk memberikan perspektif yang berbeda pada gambar.
"""

# Flip Vertikal
flip_vertical = cv2.flip(img, 0)

print("Gambar Flip Vertikal:")
cv2_imshow(flip_vertical)

# Menyimpan hasil flip
cv2.imwrite('kelompok3_flip_vertical.png', flip_vertical)

"""## **Flip Vertikal**

Melakukan pembalikan gambar secara vertikal untuk memberikan perspektif yang berbeda pada gambar.
"""

# Menambah kecerahan
bright_add = cv2.add(img, np.ones(img.shape, dtype="uint8") * 50)

# Mengurangi kecerahan
bright_subtract = cv2.subtract(img, np.ones(img.shape, dtype="uint8") * 50)

# Membagi kecerahan
bright_divide = cv2.divide(img, 2)

# Mengalikan kecerahan
bright_multiply = cv2.multiply(img, 1.5)

# Menampilkan hasil
print("Tambah Kecerahan:")
cv2_imshow(bright_add)

print("Kurangi Kecerahan:")
cv2_imshow(bright_subtract)

print("Bagi Kecerahan:")
cv2_imshow(bright_divide)

print("Kali Kecerahan:")
cv2_imshow(bright_multiply)

# Menyimpan hasil
cv2.imwrite('kelompok3_brightness_add.png', bright_add)
cv2.imwrite('kelompok3_brightness_subtract.png', bright_subtract)
cv2.imwrite('kelompok3_brightness_divide.png', bright_divide)
cv2.imwrite('kelompok3_brightness_multiply.png', bright_multiply)

"""## **Brightness Otomatis (Manual Arithmetic Operation)**
Pengaturan kecerahan dilakukan secara otomatis dengan menambahkan, mengurangi, membagi, dan mengalikan nilai piksel gambar menggunakan operasi aritmatika.
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from ipywidgets import interact, IntSlider

# Membaca gambar
img = cv2.imread('kelompok3.png')

# Fungsi untuk menyesuaikan kecerahan
def adjust_brightness(brightness):
    # Konversi gambar ke float32 untuk menghindari overflow
    bright_img = img.astype(np.float32)

    # Tambahkan nilai brightness
    bright_img = bright_img + brightness

    # Batasi nilai piksel antara 0 - 255
    bright_img = np.clip(bright_img, 0, 255).astype(np.uint8)

    # Menampilkan gambar hasil
    print(f"Kecerahan: {brightness}")
    cv2_imshow(bright_img)

# Menampilkan slider interaktif
print("Geser slider ke kiri untuk mengurangi kecerahan, ke kanan untuk menambah kecerahan:")
interact(adjust_brightness, brightness=IntSlider(min=-100, max=100, step=1, value=0))

"""## **Brightness Adjustment (Pengaturan Kecerahan)**

- Slider interaktif digunakan untuk meningkatkan atau menurunkan kecerahan gambar.
- Geser ke kiri untuk menggelapkan gambar dan ke kanan untuk mencerahkan gambar.

# **Kesimpulan**
Proyek ini memberikan wawasan mendalam tentang manipulasi gambar digital dan menunjukkan bagaimana 7 langkah pemrosesan gambar dapat diimplementasikan dengan baik dalam satu rangkaian kerja. Dengan fitur interaktif seperti slider untuk kecerahan dan zoom, proyek ini diharapkan dapat menjadi dasar untuk aplikasi image processing yang lebih kompleks di masa depan.
"""