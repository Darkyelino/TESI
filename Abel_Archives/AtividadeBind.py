import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Tela:


    def log(self, event):
        self.w = tk.Label(self.janela,text="Key Pressed:"+event.char)
        self.w.pack()

    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Precione qualquer tecla')
        self.janela.bind('<Return>', self.log)
        self.janela.bind('<Button-1>', self.log)
        self.janela.bind('<KeyPress>', self.log)
        self.btn.pack()
        self.lbl = tk.Label(self.janela)
        self.lbl.pack()

        # Criação do ScrolledText
        self.texto = ScrolledText()
        self.texto.pack()

        # Criação do botão limpar tela
        self.limpa = tk.Button(self.janela, text='Limpar Tela')
        self.limpa.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
