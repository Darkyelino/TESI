import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        colunas = ['nome', 'email', 'telefone']

        self.tvw_pessoas = ttk.Treeview(self.janela, show='headings', columns=colunas, height=5)

        self.tvw_pessoas.heading(0, text='Nome')
        self.tvw_pessoas.heading('email', text='E-mail')
        self.tvw_pessoas.heading(2, text='Telefone')

        self.tvw_pessoas.column('nome', minwidth=0, width=100)

        self.tvw_pessoas.insert('', 'end', values=('Fulano','Fulano@email.com', '123456789'))
        self.tvw_pessoas.insert('', 'end', values=('Ciclano', 'Ciclano@email.com', '987654321'))
        self.tvw_pessoas.insert('', 'end', values=('Beltrano', 'Beltrano@email.com', '999999999'))
        self.tvw_pessoas.insert('', 'end', values=('Milano', 'Milano@email.com', '112233445'))
        self.tvw_pessoas.insert('', 'end', values=('Pelano', 'Pelano@email.com', '123498765'))

        # pai = self.tvw_pessoas.insert('', 'end', text='Pessoas')
        # self.tvw_pessoas.insert(pai, 'end', text='Claudinor')
        # self.tvw_pessoas.insert(pai, 'end', text='Macilon')
        self.tvw_pessoas.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()