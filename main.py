import connect
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

class screen(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.configurations()
        self.register_screan()
        
    def configurations(self):
        self.geometry('700x700')
        self.title("Carteira de Investimentos 1.0")
        self.resizable(0, 0) 
        
    def register_screan(self):
        
        
        
        #self.frame_login.pack()
        
        self.title = ctk.CTkLabel(self, font=("Century Gothic bold", 16), text="Cadastre seus Ativos!")
        self.title.grid(row=0, column=0, padx=5, pady=5)
        
        self.stockName_entry = ctk.CTkEntry(self, width=350, corner_radius=15, placeholder_text="Nome do Ativo", font=("Century Gothic bold", 12))
        self.stockName_entry.grid(row=1, column=0, padx=5, pady=5 )
        
        
        # Frame com informaçoes de data, preço e quantidade 
        self.frame_login = ctk.CTkFrame(self, width=500, height=600)
        self.frame_login.grid(row=2, column=0)
         
        self.price_entry = ctk.CTkEntry(self.frame_login, width=150, corner_radius=15, placeholder_text="Preço por unidade", font=("Century Gothic bold", 12))
        self.price_entry.grid(row=0, column=0, padx=5, pady=5, sticky=W )
        
        self.amount_entry = ctk.CTkEntry(self.frame_login, width=150, corner_radius=15, placeholder_text="Quantidade", font=("Century Gothic bold", 12))
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.data_entry = ctk.CTkEntry(self.frame_login, width=150, corner_radius=15, placeholder_text="Data da compra", font=("Century Gothic bold", 12))
        self.data_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        self.login_button = ctk.CTkButton(self.frame_login, text="Registrar")
        self.login_button.grid(column=1, row=3, sticky=ctk.E, padx=5, pady=5)

if __name__ == '__main__':
    app = screen()
    app.mainloop()
    