import tkinter as tk
from tkinter import ttk


class Tela:

    def cad(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Cadastro")
        nova_janela.geometry("400x250")
        nova_janela.config(bg="lightblue")

        # CRIAÇÃO DO FRAME INFERNAL
        frame_cadastro = tk.Frame(nova_janela, bg="lightblue")
        frame_cadastro.place(relx=0.5, rely=0.5, anchor='center')
        frame_cadastro.grid_columnconfigure(0, weight=1)
        frame_cadastro.grid_columnconfigure(1, weight=1)
        frame_cadastro.grid_rowconfigure(0, weight=1)
        frame_cadastro.grid_rowconfigure(1, weight=1)
        frame_cadastro.grid_rowconfigure(2, weight=1)
        frame_cadastro.grid_rowconfigure(3, weight=1)
        frame_cadastro.grid_rowconfigure(4, weight=1)
        frame_cadastro.grid_rowconfigure(5, weight=1)

        # INSERÇÃO DO NOME
        label_nome = tk.Label(frame_cadastro, text="NOME COMPLETO:", bg="lightblue", fg='black')
        label_nome.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.entrada_nome = tk.Entry(frame_cadastro)
        self.entrada_nome.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DA DATA
        label_datanasc = tk.Label(frame_cadastro, text="DATA DE NASCIMENTO:", bg="lightblue", fg='black')
        label_datanasc.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.entrada_datanasc = tk.Entry(frame_cadastro)
        self.entrada_datanasc.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DE DOCUMENTOS
        label_documento = tk.Label(frame_cadastro, text="DOCUMENTOS:", bg="lightblue", fg='black')
        label_documento.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.entrada_documento = tk.Entry(frame_cadastro)
        self.entrada_documento.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DO EMAIL
        label_email = tk.Label(frame_cadastro, text="EMAIL:", bg="lightblue", fg='black')
        label_email.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        self.entrada_email = tk.Entry(frame_cadastro)
        self.entrada_email.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        # INSERÇÃO DO TELEFONE
        label_telefone = tk.Label(frame_cadastro, text="TELEFONE:", bg="lightblue", fg='black')
        label_telefone.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        self.entrada_telefone = tk.Entry(frame_cadastro)
        self.entrada_telefone.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

        # BUTÃO
        self.butao_enviar = tk.Button(frame_cadastro, text='Enviar', command=self.salvar_cadastro)
        self.butao_enviar.grid(columnspan=5, row=5, padx=20, pady=20, sticky='nsew')

    def salvar_cadastro(self):
        nome = self.entrada_nome.get()
        data_nasc = self.entrada_datanasc.get()
        documento = self.entrada_documento.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()

        self.funcionarios.append((nome, data_nasc, documento, email, telefone))

    def visualizar_cadastro(self):
        nova_janela = tk.Toplevel(self.janela)
        nova_janela.title("Visualizar Cadastros")
        nova_janela.geometry("900x300")

        colunas = ("Nome", "Data de Nascimento", "Documento", "Email", "Telefone")
        tree = ttk.Treeview(nova_janela, columns=colunas, show="headings")

        tree.heading("Nome", text="Nome")
        tree.heading("Data de Nascimento", text="Data de Nascimento")
        tree.heading("Documento", text="Documento")
        tree.heading("Email", text="Email")
        tree.heading("Telefone", text="Telefone")

        tree.column("Nome", width=150)
        tree.column("Data de Nascimento", width=150)
        tree.column("Documento", width=150)
        tree.column("Email", width=150)
        tree.column("Telefone", width=150)

        for funcionario in self.funcionarios:
            tree.insert("", "end", values=funcionario)

        tree.pack(fill=tk.BOTH, expand=True)

    def __init__(self, master):
        self.janela = master
        self.janela.title("Sistema de Cadastramento")
        self.janela.geometry("500x300")
        self.janela.config(bg="#92D975")

        # LISTA PARA ARMAZENAR CADASTROS
        self.funcionarios = []

        label_inicio = tk.Label(self.janela, text="Boas vindas ao sistema de cadastramento!", fg='black', font=("Arial", 16),
                                bg="#92D975", )
        label_inicio.pack(pady=20)

        # CRIAÇÃO DA BARRA DE MENU
        self.menu_barra = tk.Menu(self.janela)

        # PRIMEIRO ITEM DA BARRA DE MENU: "HOME"
        self.menu_home = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Home', menu=self.menu_home)
        self.menu_home.add_command(label='Tela Inicial')
        self.menu_home.add_command(label='Sair', command=self.janela.quit)

        # SEGUNDO ITEM DA BARRA DE MENU: "CADASTROS"
        self.menu_cadastro = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Cadastros', menu=self.menu_cadastro)
        self.menu_cadastro.add_command(label='Fazer cadastro', command=self.cad)
        self.menu_cadastro.add_command(label='Visualizar cadastro', command=self.visualizar_cadastro)

        # CONFIGURAÇÕES DA BARRA DE MENU
        self.janela.config(menu=self.menu_barra)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()