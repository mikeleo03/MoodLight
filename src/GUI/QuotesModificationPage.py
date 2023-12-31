# File : QuotesModificationPage.py 
# Berisi kelas boundary QuotesModificationPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas controller QuotesModificationController dengan pengguna luar 

from customtkinter import *
import os
from PIL import Image
from Quote.QuoteModificationController import QuoteModificationController

class QuotesModificationPage(CTk):

    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari QuotesModificationPage
    def __init__(self, master):
        # Menetapkan master dari QuotesModificationPage yaitu master
        self.master = master

        # Menginisialisasi keberadaan objek controller
        self.quotes_controller = QuoteModificationController()

        # Menciptakan frame pertama tempat mengubah data quotes
        self.quotes_modif_frame = CTkFrame(self.master, corner_radius=0, fg_color="#568ea6")
        self.quotes_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "img")
        
        self.quotes_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "img")
        self.quotes_logo_image = CTkImage(Image.open(os.path.join(self.quotes_image_path, "logo.png")), size=(150,30))
        self.quotes_logo_image_label = CTkLabel(self.quotes_modif_frame, text="", image=self.quotes_logo_image)
        self.quotes_logo_image_label.grid(row=0, column=1, padx=(0,100), pady=(10,0), sticky="ne")

        self.quotes_list_frame = CTkScrollableFrame(self.quotes_modif_frame,width=900,height=500,corner_radius=0,fg_color="#00b4d8")
        self.quotes_list_frame.grid(row=1,column=0,padx=250,pady=(30,20), columnspan=2)
        
        self.quotes_textboxes = []
        for i in range(len(self.quotes_controller.data)) :
            self.quotes_textboxes.append(CTkTextbox(self.quotes_list_frame,width=890,height=40,font=CTkFont(size=18)))
            self.quotes_textboxes[i].insert("0.0", self.quotes_controller.data[i].getContent() + " ~ " + self.quotes_controller.data[i].getAuthor())
            self.quotes_textboxes[i].grid(row=i,column=0,padx=10,pady=10)
        
        self.format_label = CTkLabel(self.quotes_modif_frame,text="Quote format : <Quote> ~ <Author>", text_color="white", font=CTkFont(size=20,weight="bold"))
        self.format_label.grid(row=2,column=0,padx=100,pady=15, columnspan=2)

        self.quotes_add = CTkButton(self.quotes_modif_frame, text="Add Quotes", font=CTkFont(size=18, weight="bold"), command=self.quotes_add_button_event, width=130, height=40, fg_color="#305f72")
        self.quotes_add.grid(row=3, column=0, padx=(350, 0), pady=15)
        
        self.quotes_save = CTkButton(self.quotes_modif_frame, text="Save", font=CTkFont(size=18, weight="bold"), command=self.quotes_save_button_event, width=130, height=40, fg_color="#305f72")
        self.quotes_save.grid(row=3, column=1, padx=(0,350), pady=15)

    # GETTER
    # Mengembalikan frame pertama dan utama dari QuotesModificationPage
    def get_frame(self):
        return self.quotes_modif_frame
    
    # EVENT ACTION
    # Menyimpan record yang telah diubah oleh pengguna di frame ke file data
    def quotes_save_button_event(self):
        id = 1
        for txt in (self.quotes_textboxes) :
            text = txt.get("0.0","end").strip()
            if (text != "") : # Jika tidak kosong, simpan sebagai quotes baru
                try :
                    content,author = text.split(" ~ ")
                except :
                    txt.destroy()
                    continue
                self.quotes_controller.createRecord(id,author,content)
                id += 1
            elif(self.quotes_controller.isInRecord(id)) :
                self.quotes_controller.deleteRecord(id)
            txt.destroy()
        self.quotes_textboxes.clear()
        
        for i in range(len(self.quotes_controller.data)) :
            self.quotes_textboxes.append(CTkTextbox(self.quotes_list_frame,width=890,height=40,font=CTkFont(size=18)))
            self.quotes_textboxes[i].insert("0.0", self.quotes_controller.data[i].getContent() + " ~ " + self.quotes_controller.data[i].getAuthor())
            self.quotes_textboxes[i].grid(row=i,column=0,padx=10,pady=10)
    
    # Menambahkan textbox baru
    def quotes_add_button_event(self):
        self.quotes_textboxes.append(CTkTextbox(self.quotes_list_frame,width=890,height=40,font=CTkFont(size=18)))
        self.quotes_textboxes[len(self.quotes_textboxes)-1].grid(row=len(self.quotes_textboxes)-1,column=0,padx=10,pady=10)
    