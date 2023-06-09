from tkinter import *
from PIL import Image
from tkinter import messagebox

def bigFunction():
    def validation2():
          with open("data.txt", "r") as file:
           lignes = file.readlines()
          informations = [ligne.strip().split(",") for ligne in lignes]
          mot_de_passe_entre = user2.get()
          for info in informations:
            if mot_de_passe_entre == info[0]:
                hello2(info)
                return
          message2.config(text="كلمة المرور غير صحيحة")
    def changer_mot_de_passe2():
        fenetre_changer_mdp = Toplevel(fenetre_principale2)
        fenetre_changer_mdp.geometry("400x300")
        fenetre_changer_mdp.title("تغيير كلمة المرور")

        def valider2():
            new_password = entry_mdp.get()
            if new_password:
              with open("data.txt", "r+") as file:
                lignes = file.readlines()
                informations = [ligne.strip().split(",") for ligne in lignes]
                mot_de_passe_entre = user2.get()
                for i, info in enumerate(informations):
                    if mot_de_passe_entre == info[0]:
                        informations[i][0] = new_password
                        file.seek(0)
                        file.truncate()
                        for info in informations:
                            file.write(",".join(info) + "\n")
                        messagebox.showinfo("Succès", "لقد تم تغببر كلمة المرور بنجاح")
                        fenetre_changer_mdp.destroy()
                        return
            messagebox.showerror("Erreur", "كلمة المرور الجديدة غير صالحة")

        label_mdp = Label(fenetre_changer_mdp, text="كلمة المرور الجديدة",fg="#365972",font=('Courier New',15,'bold'))
        label_mdp.place(x=100,y=60)
        entry_mdp = Entry(fenetre_changer_mdp, show="*")
        entry_mdp.place(x=150,y=120)
        button_valider = Button(fenetre_changer_mdp, text="تغيير", command=valider2,font= ("Arial", 15, "bold"), bg= "#fdcd56", fg= "#365972", width= 10, height= 2, bd= 0,activebackground= "#f9b52d")
        button_valider.place(x=150,y=200)      

    def hello2(info):
      global man
      fenetre_hello = Toplevel(fenetre_principale2)
      fenetre_hello.geometry("925x550+300+200")
      man = PhotoImage(file='C:\\Users\\ADMIN\\Pictures\\well.png')
      background = Label(fenetre_hello, image=man)
      background.place(x=8, y=30)
      salut = Label(fenetre_hello, text=f" {info[2]} {info[1]} مرحبا", font=('Courier New', 20, 'bold'), fg="#074af1" ,bg="white")
      salut.place(x=400, y=150)
      bouton_next = Button(fenetre_hello, text="التالي", command=lambda: next_window(info[0], info[1], info[2], info[3], info[4]), bg="#074af1", fg="white", width=25, pady=10, font=(20))
      bouton_next.place(x=400, y=400)
      bouton_retour = Button(fenetre_hello, text="الرجوع", command=fenetre_hello.destroy, bg="#074af1", fg="white", width=25, pady=10, font=(20))
      bouton_retour.place(x=650, y=400)

    def next_window(password, nom, prenom, solde, telephone):
      fenetre_options = Toplevel(fenetre_principale2)
      fenetre_options.geometry("925x550+300+200")
      selc=Label(fenetre_options,text="اختر خدمة :",fg="#074af1",font=("Arail",20,'bold'))
      selc.place(x=310,y=10)
      cana=Canvas(fenetre_options,bg="#f46f51",width=265,height=700)
      cana.place(x=0,y=80)
      canaV=Canvas(fenetre_options,bg="#f46f51",width=265,height=700)
      canaV.place(x=655,y=80)
      bouton_transfer = Button(fenetre_options, text="تحويل", command=lambda:afficher_fenetre_transfer2(), border=0,bg="#074af1",width=35,pady=25,fg="white",font=(20))
      bouton_retirer = Button(fenetre_options, text="سحب", command=lambda:retirer2(password, solde),border=0,bg="#074af1",width=35,pady=25,fg="white",font=(20))   
      bouton_changer_mdp = Button(fenetre_options, text="تغيير كلمة المرور",command=changer_mot_de_passe2, border=0,bg="#074af1",width=35,pady=25,fg="white",font=(20))
      bouton_informations = Button(fenetre_options, text="معلوماتكم", command=lambda: infos2(password, nom, prenom, solde, telephone) ,border=0,bg="#074af1",width=35,pady=25,fg="white",font=(20))
      bouton_quetter = Button(fenetre_options, text="الرجوع", command=fenetre_options.destroy ,border=0,bg="#074af1",width=35,pady=25,fg="white",font=(20))
      bouton_retirer.place(x=100,y=135)
      bouton_changer_mdp.place(x=300,y=280)
      bouton_informations.place(x=100,y=420)
      bouton_transfer.place(x=530,y=135)
      bouton_quetter.place(x=530,y=420)
     
    
    def afficher_fenetre_transfer2():
        fenetre_transfer = Toplevel(fenetre_principale2)
        fenetre_transfer.geometry("600x550+300+200")
        
        fenetre_transfer.title("التحويل")

        label_compte_source = Label(fenetre_transfer, text="المرسل", fg="#365972", 
                                font=("Giorgia", 15, "italic", "bold"))
        label_compte_source .place(x=100,y=30)
       
        compte_source_entry = Entry(fenetre_transfer)
      
        compte_source_entry .place(x=300,y=30)

        label_compte_dest = Label(fenetre_transfer, text="المرسل اليه", fg="#365972",
                                font=("Giorgia", 15, "italic", "bold"))
        label_compte_dest.place(x=100,y=120)
  
        compte_dest_entry = Entry(fenetre_transfer)
       
        compte_dest_entry .place(x=300,y=120)

        label_montant = Label(fenetre_transfer, text="المبلغ", fg="#365972",
                                font=("Giorgia", 15, "italic", "bold"))
        label_montant.place(x=100,y=220)
      
        montant_entry = Entry(fenetre_transfer)
       
        montant_entry .place(x=300,y=220)

        bouton_envoyer = Button(fenetre_transfer, text="ارسال",fg="white", font=("Georgia", 10, "bold", "italic"),command=lambda: envoyer_argent2(compte_source_entry, compte_dest_entry, montant_entry), background="#fdcd56" , bd=3, relief="groove")
    
        bouton_envoyer.place(x=50,y=350)

        quitt_button = Button(fenetre_transfer,fg="white", text="الرجوع", command=fenetre_transfer.destroy,
                                font=("Georgia", 10, "bold", "italic"), bd=3, relief="groove", background="#fdcd56")
        quitt_button.place(x=450,y=350)
    def envoyer_argent2(compte_source_entry,compte_dest_entry,montant_entry):
        compte_source = compte_source_entry.get()
        compte_dest = compte_dest_entry.get()
        montant = float(montant_entry.get())
        with open("data.txt", "r") as file:
            lignes = file.readlines()
            informations = [ligne.strip().split(",") for ligne in lignes]

            solde_source = None
            solde_dest = None

            for info in informations:
                if info[1] == compte_source:
                    solde_source = float(info[3])
                    break
            else:
                messagebox.showerror("Erreur", "حساب مصدر غير صالح")
                return

            for info in informations:
                if info[1] == compte_dest:
                    solde_dest = float(info[3])
                    break
            else:
                messagebox.showerror("Erreur", "حساب وجهة غير صالح")
                return
        if montant > solde_source:
            messagebox.showerror("Erreur", "رصيد غير كاف في حساب المصدر")
            return

        solde_source -= montant
        solde_dest += montant

        with open("data.txt", "w") as file:
            for info in informations:
                if info[1] == compte_source:
                    info[3] = str(solde_source)
                elif info[1] == compte_dest:
                    info[3] = str(solde_dest)

                line = ",".join(info)
                file.write(line + "\n")

        messagebox.showinfo("Succès", "تم التحويل بنجاح")

        fenetre_principale2.destroy()
    
    def infos2(password, nom, prenom, solde, telephone):
        fenetre_informations = Toplevel()
        fenetre_informations.title("معلومات")
        fenetre_informations.configure(bg="#f0f0f0")
        fenetre_informations.geometry("400x400")
        
        label_style = {"font": ("Arial", 14), "bg": "#f0f0f0", "fg": "#365972"}
        value_style = {"font": ("Arial", 14), "bg": "#f0f0f0"}
        button_style = {"font": ("Arial", 14, "bold"), "bg": "#fdcd56", "fg": "white", "bd": 0, "width": 10, "height": 2}
        
        Label(fenetre_informations, text="كلمة المرور", **label_style).grid(row=0, column=1, padx=10, pady=10)
        Label(fenetre_informations, text=password, **value_style).grid(row=0, column=0, padx=10, pady=10)
        Label(fenetre_informations, text="النسب", **label_style).grid(row=1, column=1, padx=10, pady=10)
        Label(fenetre_informations, text=prenom, **value_style).grid(row=1, column=0, padx=10, pady=10)
        Label(fenetre_informations, text="الاسم", **label_style).grid(row=2, column=1, padx=10, pady=10)
        Label(fenetre_informations, text=nom, **value_style).grid(row=2, column=0, padx=10, pady=10)
        Label(fenetre_informations, text="الرصيد", **label_style).grid(row=3, column=1, padx=10, pady=10)
        Label(fenetre_informations, text=solde, **value_style).grid(row=3, column=0, padx=10, pady=10)
        Label(fenetre_informations, text="الهاتف", **label_style).grid(row=4, column=1, padx=10, pady=10)
        Label(fenetre_informations, text=telephone, **value_style).grid(row=4, column=0, padx=10, pady=10)

        bouton_retour = Button(fenetre_informations, text="رجوع", **button_style, command=fenetre_informations.destroy)
        bouton_retour.place(x=130,y=300)

    def retirer2( password, solde):
        def retirer_solde():
            nonlocal solde
            montant = float(montant_entry.get())
            solde = float(solde)
            if montant > solde:
                msg = Label(fenetre_retirer)
                msg.config(text="المبلغ المطلوب أكبر من رصيدك.", fg="red", font=("georgia", 8),
                           bg="#14213D")
                msg.pack()
            else:
                solde -= montant
                msg1 = Label(fenetre_retirer)
                msg1.config(text="لقد تم سحب المبلغ بنجاح", fg="green", font=("georgia", 8),
                            bg="#14213D")
                msg1.pack()
                with open("data.txt", "r") as file:
                    lignes = file.readlines()
                with open("data.txt", "w") as file:
                    for ligne in lignes:
                        info = ligne.strip().split(",")
                        if info[0] == password:
                            info[3] = str(solde)
                            ligne = ",".join(info) + "\n"
                        file.write(ligne)

        fenetre_retirer = Toplevel()
        fenetre_retirer.geometry("600x550+300+200")
        fenetre_retirer.title("السحب")
        

        Label(fenetre_retirer, text="المبلغ", font=("Georgia",15, "bold", "italic"),fg="#365972").place(x=100, y=120)
        montant_entry = Entry(fenetre_retirer)
        montant_entry.place(x=400, y=120)

        valider_button =Button(fenetre_retirer, text="تأكيد",fg="white", font=("Georgia", 10, "bold", "italic"),command=retirer_solde, background="#fdcd56" , bd=3, relief="groove")

        valider_button.place(x=120, y=300)

        quitt_button = Button(fenetre_retirer,fg="white", text="رجوع", command=fenetre_retirer.destroy,
                                font=("Georgia", 10, "bold", "italic"), bd=3, relief="groove", background="#fdcd56")
        quitt_button.place(x=480, y=300)
    


  
    def on_keypress(key):
      current = user2.get()
      if key.isdigit():
         user2.delete(0, END)
         user2.insert(0, current + key)
  
    fenetre_principale2 = Toplevel()
    fenetre_principale2.geometry("925x550+300+200")
   
    titre2 = Label(fenetre_principale2, text="البنك هذا لاختياركم شكرا", fg='#fdcd56', bg='#f0f0f0', font=("Georgia", 30, 'bold'))
    titre2.pack()
    
    heading2 = Label(fenetre_principale2, text='ادخل كلمة المرور ',  fg='#365972', bg='#f0f0f0', font=('Courier New', 13, 'bold'))
    heading2.place(x=380, y=60)
    filename22 = PhotoImage(file='C:\\Users\\ADMIN\\Pictures\\icon.png')
    background_label22 = Label(fenetre_principale2, image=filename22)
    background_label22.place(x=900, y=157)
    user2 = Entry(fenetre_principale2, width=30, fg='#365972', border=0, bg='#f0f0f0', font=(9),show="*")
    user2.place(x=400, y=130)
    
   
    keyboard_frame = Frame(fenetre_principale2, bg='#f0f0f0')
    keyboard_frame.place(x=370, y=200)

    buttons = []
    for i in range(10):
      button = Button(keyboard_frame, text=str(i), width=3, height=1, font=('Courier New', 13, 'bold'))
      button.grid(row=i//3, column=i%3, padx=5, pady=5)
      button.config(command=lambda digit=i: on_keypress(str(digit)))
      buttons.append(button)

    Frame(fenetre_principale2, width=295, height=2, bg='#365972').place(x=300, y=150)
    Button(fenetre_principale2,pady=2,  text="تأكيد",command=validation2 ,bg='#fdcd56', fg='white', border=0,
       font=('Courier New', 13, 'bold')).place(x=430, y=340)
    message2 = Label(fenetre_principale2, fg="red")
    message2.place(x=350, y=100)
if __name__ == "__main__":
  bigFunction()    
   

   
