import tkinter as tk
from tkinter import ttk

class Tela:

    def cad(self):
        self.janela.config(bg="lightblue")

        # CRIAÇÃO DO FRAME INFERNAL
        frame_cadastro = tk.Frame(self.janela, bg="lightblue")
        frame_cadastro.place(relx=0.5, rely=0.5, anchor='center')
        frame_cadastro.grid_columnconfigure(0, weight=1)
        frame_cadastro.grid_columnconfigure(1, weight=1)
        frame_cadastro.grid_rowconfigure(0, weight=1)
        frame_cadastro.grid_rowconfigure(1, weight=1)
        frame_cadastro.grid_rowconfigure(2, weight=1)
        frame_cadastro.grid_rowconfigure(3, weight=1)

        # INSERÇÃO DO NOME
        label_nome = tk.Label(frame_cadastro, text="NOME COMPLETO:", bg="lightblue")
        label_nome.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.entrada_nome = tk.Entry(frame_cadastro)
        self.entrada_nome.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DA DATA
        label_datanasc = tk.Label(frame_cadastro, text="DATA DE NASCIMENTO:", bg="lightblue")
        label_datanasc.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.entrada_datanasc = tk.Entry(frame_cadastro)
        self.entrada_datanasc.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DE DOCUMENTOS
        label_documento = tk.Label(frame_cadastro, text="DOCUMENTOS:", bg="lightblue")
        label_documento.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.entrada_documento = tk.Entry(frame_cadastro)
        self.entrada_documento.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        # BUTÃO
        self.butao_enviar = tk.Button(frame_cadastro, text='Enviar')
        self.butao_enviar.grid(columnspan=4, row=3, padx=20, pady=20, sticky='nsew')


    def __init__(self, master):
        self.janela = master
        self.janela.title('Sistema de Cadastramento')
        self.janela.geometry('500x300')

        #CRIAÇÃO DA BARRA DE MENU
        self.menu_barra = tk.Menu(self.janela)

        #PRIMEIRO ITEM DA BARRA DE MENU: "HOME"
        self.menu_home = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Home', menu=self.menu_home)
        self.menu_home.add_command(label='Tela Inicial')
        self.menu_home.add_command(label='Sair', command=self.janela.quit)

        #SEGUNDO ITEM DA BARRA DE MENU: "CADASTROS"
        self.menu_cadastro = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Cadastros', menu=self.menu_cadastro)
        self.menu_cadastro.add_command(label='Fazer cadastro', command=self.cad)
        self.menu_cadastro.add_command(label='Visualizar cadastro')
        
        #CONFIGURAÇÕES DA BARRA DE MENU
        self.janela.config(menu=self.menu_barra)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()