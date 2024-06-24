from connect import connect
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

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
        desable = ["!","@","%"]
        if desable in self.stockName_entry.get():
            mgs = messagebox.showerror("Erro","caracter não suportado")
        else:
            self.stockName = self.stockName_entry.get()
            self.price = self.price_entry.get()
            self.amount = self.amount_entry.get()
            self.data = self.data_entry.get()   
        
    
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

        self.title_label = ctk.CTkLabel(self.frame_login, font=("Century Gothic bold", 16), text="Cadastre seus Ativos!")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.stockName_entry = ctk.CTkEntry(self.frame_login, width=350, corner_radius=10, placeholder_text="Nome do Ativo", font=("Century Gothic bold", 10))
        self.stockName_entry.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Frame interno para alinhar price, amount e data
        self.info_frame = ctk.CTkFrame(self.frame_login)
        self.info_frame.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.price_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=10, placeholder_text="Preço por unidade", font=("Century Gothic bold", 10))
        self.price_entry.grid(row=0, column=0, padx=10, pady=5)

        self.amount_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=10, placeholder_text="Quantidade", font=("Century Gothic bold", 10))
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.data_entry = ctk.CTkEntry(self.info_frame, width=100, corner_radius=10, placeholder_text="Data da compra", font=("Century Gothic bold", 10))
        self.data_entry.grid(row=0, column=2, padx=10, pady=5)

        self.info_frame_button = ctk.CTkFrame(self.frame_login)
        self.info_frame_button.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        
    # Botoes de ação da operação !
            
        self.register_button = ctk.CTkButton(self.info_frame_button, width=200, corner_radius=10, text="Registrar", command=self.get_entry)
        self.register_button.grid(row=3, column=0, sticky=ctk.W, padx=5, pady=5)
        
        self.Exit_register_button = ctk.CTkButton(self.info_frame_button, width=75, corner_radius=10, text="Sair", fg_color='#909899')
        self.Exit_register_button.grid(row=3, column=1, sticky=ctk.W, padx=(50, 0), pady=5)
        
        
         
    
              

if __name__ == '__main__':
    app = screen()
    app.mainloop()
    