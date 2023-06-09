from tkinter import *
from PIL import Image
from tkinter import messagebox
from fr import bigFunction2
from ar import bigFunction

fenetre_P = Tk()
fenetre_P.geometry("950x630")
fenetre_P.title("Sélection de la langue")
fenetre_P.configure(bg="#f0f0f0")

title_frame = Frame(fenetre_P, bg="#f0f0f0")
title_frame.pack(pady=50)

par = Label(title_frame, text="Choisir votre langue", font=("Arial", 28, "bold"), bg="#f0f0f0", fg="#365972")
par.pack()

btn_frame = Frame(fenetre_P, bg="#f0f0f0")
btn_frame.pack(pady=50)

btn_style = {"font": ("Arial", 20, "bold"), "bg": "#fdcd56", "fg": "white", "width": 10, "height": 2, "bd": 0, "activebackground": "#f9b52d"}

Pbtn = Button(btn_frame, text="Français", **btn_style, command=bigFunction2)
Pbtn.pack(side=LEFT, padx=20)

Dbtn = Button(btn_frame, text="العربية", **btn_style, command=bigFunction)
Dbtn.pack(side=LEFT, padx=20)

fenetre_P.mainloop()
