import tkinter as tk


class Tela:
    def clicou(self, event):
        self.lbl.config(text='Clicou!')

    def log(self, master):
        print(event)

    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Clique!')
        self.btn.bind('<Return>', self.clicou)
        self.btn.bind('<Button-1>', self.clicou)
        self.btn.bind('<Key>', self.log)
        self.btn.pack()
        self.lbl = tk.Label(self.janela)
        self.lbl.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
