from connect import connect
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# trabalhando com expressões regulares
import re 


class screen(ctk.CTk,connect):
    
    def __init__(self):
        super().__init__()
        self.configurations()
        self.register_screan()
        
        
    def configurations(self):
        self.geometry('700x700')
        self.title("Carteira de Investimentos 1.0")
        self.resizable(0, 0) 
        self._set_appearance_mode("Dark")
    
    # ### Realizar o tratamento dessas variaveis !
    def get_entry(self):
        #desable = ["!","@","%"]
        #if desable in self.stockName_entry.get():
            #mgs = messagebox.showerror("Erro","caracter não suportado")
        #else:
            self.stockName = self.stockName_entry.get()
            self.price = self.price_entry.get()
            self.amount = self.amount_entry.get()
            self.data = self.data_entry.get()   
            self.brokerage = self.brokerage_entry.get()
            self.others = self.others_entry.get()
    
    def confirm_action(self):
        action = messagebox.askyesno("Confirmar cadastro","Você tem certeza que deseja cadastrar ?")
        if action:
            self.get_entry()
            self.insert_db(self.stockName, self.price, self.amount)
            action_confirmed = messagebox.showinfo("Confirmado!","cadastrado com sucesso ")
        else:
            return
           
    def register_screan(self):
        
        #self.frame_login.pack()
        self.frame_login = ctk.CTkFrame(self, width=650, height=600, corner_radius=5)
        self.frame_login.grid(row=0, column=0, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(self.frame_login, font=("Century Gothic bold", 18), text="Cadastre seus Ativos!")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.stockName_entry = ctk.CTkEntry(self.frame_login, width=330, corner_radius=5, placeholder_text="Nome do Ativo", font=("Century Gothic bold", 10))
        self.stockName_entry.grid(row=1, column=0, padx=15, pady=5, sticky='w')

        # Frame interno para alinhar price, amount e data
        self.info_frame = ctk.CTkFrame(self.frame_login)
        self.info_frame.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.price_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=5, placeholder_text="Preço por unidade", font=("Century Gothic bold", 10))
        self.price_entry.grid(row=0, column=0, padx=10, pady=5)
        self.price_entry.bind('<KeyRelease>', self.calc)

        self.amount_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=5, placeholder_text="Quantidade", font=("Century Gothic bold", 10))
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        self.amount_entry.bind('<KeyRelease>', self.calc)

        self.data_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=5, placeholder_text="DD/MM/AA", font=("Century Gothic bold", 10))
        self.data_entry.grid(row=0, column=2, padx=10, pady=5)

        
    # Frame para conter a cesão de custos gerais
        self.costs_frame = ctk.CTkFrame(self.frame_login)
        self.costs_frame.grid(row=3, column=0, padx=5, pady=5, sticky='E')
        
        self.brokerage_label = ctk.CTkLabel(self.costs_frame, font=("Century Gothic bold", 12), text="Custos de corretagem por ativo:")
        self.brokerage_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.brokerage_entry = ctk.CTkEntry(self.costs_frame, width=100, corner_radius=5, placeholder_text="0,00", font=("Century Gothic bold", 10))
        self.brokerage_entry.grid(row=0, column=1, padx=(10,10), pady=5)
        self.brokerage_entry.bind('<KeyRelease>', self.calc)
        
        self.others_label = ctk.CTkLabel(self.costs_frame, font=("Century Gothic bold", 12), text="Outros custos:")
        self.others_label.grid(row=1, column=0, padx=5, pady=5, sticky='W')

        self.others_entry = ctk.CTkEntry(self.costs_frame, width=100, corner_radius=5, placeholder_text="0,00", font=("Century Gothic bold", 10))
        self.others_entry.grid(row=1, column=1, padx=(10,10), pady=5)
        self.others_entry.bind('<KeyRelease>', self.calc)
        
        # exibir o valor total da operação!
        self.info_cousts_frame = ctk.CTkFrame(self.frame_login)
        self.info_cousts_frame.grid(row=4, column=0, padx=10, pady=10, sticky='E') 
        
        self.total_others_labe = ctk.CTkLabel(self.info_cousts_frame, font=("Century Gothic bold", 12), text="Custo total da operação:")
        self.total_others_labe.grid(row=0, column=0, padx=5, pady=5, sticky='W')
        
        self.total_others_label = ttk.Label(self.info_cousts_frame, font=("Century Gothic bold", 16), text="0,00")
        self.total_others_label.grid(row=0, column=1, padx=5, pady=5, sticky='E')
        
    # Botoes de ação da operação !   
        self.info_frame_button = ctk.CTkFrame(self.frame_login)
        self.info_frame_button.grid(row=5, column=0, padx=10, pady=10, sticky='E') 
         
        self.register_button = ctk.CTkButton(self.info_frame_button, width=200, height=30, corner_radius=5, text="Registrar Compra", command=self.validtes_stock)
        self.register_button.grid(row=4, column=0, sticky=ctk.W, padx=5, pady=5)
        
        self.Exit_register_button = ctk.CTkButton(self.info_frame_button, width=50, height=30, corner_radius=5, text="Sair", fg_color='#909899', command=self.calc)
        self.Exit_register_button.grid(row=4, column=1, sticky=E, padx=(50, 0), pady=5)
        
        
        
    def calc(self, event=None):
        try:
            brokerage = float(self.brokerage_entry.get()) 
        except:
            brokerage = 0
        try:
            others = float(self.others_entry.get()) 
        except:
            others = 0 
        try:
            price = float(self.price_entry.get())
            amount = float(self.amount_entry.get())
            #brokerage = float(self.brokerage_entry.get())
            #others = float(self.others_entry.get())  
        except:
            return False
        else:
            total = ((price + brokerage) * amount)  + others
            self.total_others_label.config(text=total)
        #return "12"
    
    def validtes_stock(self):
        try:
            stockName = self.stockName_entry.get()
            valid = '[a-zA-Z0-9]{4,7}'
            if re.match(valid, stockName):
                msg = messagebox.showinfo("Confirmado!","cadastrado com sucesso ")
        except:
            erro = messagebox.ERROR("erro","erro")
        else:
            return False      

if __name__ == '__main__':
    app = screen()
    app.mainloop()
    