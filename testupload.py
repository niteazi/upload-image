import tkinter as tk
from tkinter import *
import customtkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random  # to create noise



# Create a Tkinter window
my_w = customtkinter.CTk()
my_w.title('Image Processing')
my_font1 = ('arial', 20, 'bold')
my_font2 = ('arial', 15)
my_w.geometry("300x300")


l1 = customtkinter.CTkLabel(master=my_w, text='Upload your Yuji', width=30, font=my_font1)
l1.place(relx=0.5, rely=0.3, anchor=CENTER)

width = 300  # Width
height = 300  # Height

screen_width = my_w.winfo_screenwidth()  # Width of the screen
screen_height = my_w.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

my_w.geometry('%dx%d+%d+%d' % (width, width, x, y))
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
# Function to upload and process an image
def upload_and_process():
    f_types = [('Jpg Files', '*.jpg')]
    file_path = filedialog.askopenfilename(filetypes=f_types)

    if file_path:
        # Process the uploaded image
        im = cv2.imread(file_path)
        image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        image_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.blur(image, (50, 50))
        image_gaussianblur = cv2.GaussianBlur(image, (15, 15), 500)
        image_noise = sp_noise(image, 0.1)
        image_blurednoise = cv2.blur(image_noise, (15, 15))

        plt.figure(figsize=(12, 6))
        plt.subplot(231), plt.imshow(image), plt.title('Original Yuji')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(232), plt.imshow(image_gray, cmap='gray'), plt.title('Yuji in Gray')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(233), plt.imshow(image_blur), plt.title('Yuji with Blur')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(234), plt.imshow(image_gaussianblur), plt.title('Yuji with Gaussian Blur')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(235), plt.imshow(image_noise), plt.title('Yuji with Noise')
        plt.xticks([])
        plt.yticks([])
        plt.subplot(236), plt.imshow(image_blurednoise), plt.title('Yuji with Noise and then Blur')
        plt.xticks([])
        plt.yticks([])

        plt.tight_layout()
        plt.show()


# Upload File button
b1 = customtkinter.CTkButton(master=my_w, text='Select Yuji', width=35,corner_radius=15,font=my_font2, command=upload_and_process)
b1.place(relx=0.5, rely=0.43, anchor=CENTER)


def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output



my_w.mainloop()
