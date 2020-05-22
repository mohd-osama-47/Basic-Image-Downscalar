import imutils
import cv2
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import Tk

#the root object
root = Tk()
root.title("Down Scaler")
root.geometry('325x120')
root.iconbitmap('images\\icon.ico')

def button_fun1():
    global img_folder_path
    img_folder_path = askdirectory(title='Chose the desired directory')
    label1 = tk.Label(root, text = img_folder_path, fg='blue').grid(row=1, column=0)

def button_fun2():
    global output_folder
    output_folder = askdirectory(title='Chose the desired directory')
    label2 = tk.Label(root, text = output_folder, fg='blue').grid(row=2, column=0)

def scaller():
    for img_number in range(len(os.listdir(img_folder_path))):
        image = cv2.imread(f"{img_folder_path}\\{img_number}.jpg")
        image = imutils.resize(image, width=70)
        cv2.imwrite(f"{output_folder}\\{img_number}.jpg",image)

    messagebox.showinfo("Done!","The process of downscalling has been completed!")


l = tk.Label(root, text="Supply the origin and the destination files\n and the process of down scalling will occur.")
l.grid(row=0)


b1 = tk.Button(root, text="Images file", command=button_fun1)
b1.grid(row=1, column=1)

b2 = tk.Button(root, text="Results file", command=button_fun2)
b2.grid(row=2, column=1)

b3 = tk.Button(root, text="Start?", command=scaller)
b3.grid(row=3, columnspan = 2)


root.mainloop()