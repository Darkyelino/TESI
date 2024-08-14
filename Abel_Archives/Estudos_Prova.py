
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Título")
        self.janela.geometry("1200x500")
        self.janela.minsize(1200, 500) #Tamanho mínimo
        self.janela.maxsize(1200, 500) #Tamanho máximo
        self.janela.config(bg="lightblue")

        self.menu_barra = tk.Menu(self.janela)

        self.menu_home = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Exemplo', menu=self.menu_home)
        self.menu_home.add_command(label='Item1')
        self.menu_home.add_command(label='Item2')

        self.janela.config(menu=self.menu_barra)

        self.scroll = tk.Scrollbar(self.janela)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.texto = tk.Text(self.janela, height = 5, width = 50, yscrollcommand=self.scroll.set)
        self.texto.pack(side=tk.LEFT, fill=tk.BOTH)

        self.label = tk.Label(self.janela, text='Teste',
                                    bg='green', fg='black', padx=20,
                                    pady=50, width=100, height=3,
                                    font=('Ubuntu', 24, 'bold'))
        self.label.pack()
        self.botao = tk.Button(self.janela, text='Aperte!', width=25, height= 6,
                               #command= Coloque aqui o comando
                               )
        self.botao.pack()
        self.entrada = tk.Entry(self.janela, width=20,
                                # show='*'
                                )
        self.entrada.pack()

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()