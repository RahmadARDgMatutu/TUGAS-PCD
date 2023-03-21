import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# fungsi untuk membuka file citra
def open_image():
    global img_tk, img_cv, img_gray, img_gaussian, img_canny
    # membuka dialog untuk memilih file citra
    file_path = filedialog.askopenfilename()
    if file_path:
        # membaca citra menggunakan OpenCV
        img_cv = cv2.imread(file_path)
        # mengubah citra menjadi grayscale
        img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        # mengaplikasikan filter Gaussian
        img_gaussian = cv2.GaussianBlur(img_gray, (5,5), 0)
        # mengaplikasikan Canny edge detection
        img_canny = cv2.Canny(img_gaussian, 100, 200)
        # mengubah citra menjadi format yang dapat ditampilkan pada Tkinter
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img_tk = ImageTk.PhotoImage(Image.fromarray(img_cv))
        # menampilkan citra pada label di GUI
        label.config(image=img_tk)
        label.image = img_tk

# fungsi untuk mengaplikasikan filter Gaussian pada citra
def apply_gaussian():
    global img_tk
    img_gaussian = cv2.GaussianBlur(img_gray, (5,5), 0)
    img_canny = cv2.Canny(img_gaussian, 100, 200)
    img_gaussian = cv2.cvtColor(img_gaussian, cv2.COLOR_GRAY2RGB)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img_gaussian))
    label.config(image=img_tk)
    label.image = img_tk

# fungsi untuk mengaplikasikan Canny edge detection pada citra
def apply_canny():
    global img_tk
    img_canny = cv2.Canny(img_gaussian, 100, 200)
    img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2RGB)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img_canny))
    label.config(image=img_tk)
    label.image = img_tk

# membuat GUI menggunakan Tkinter
root = tk.Tk()

# menambahkan label untuk menampilkan citra
label = tk.Label(root)
label.pack()

# menambahkan tombol untuk membuka citra
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# menambahkan tombol untuk mengaplikasikan filter Gaussian
gaussian_button = tk.Button(root, text="Gaussian Filter", command=apply_gaussian)
gaussian_button.pack()

# menambahkan tombol untuk mengaplikasikan Canny edge detection
canny_button = tk.Button(root, text="Canny Edge Detection", command=apply_canny)
canny_button.pack()

# menjalankan GUI
root.mainloop()