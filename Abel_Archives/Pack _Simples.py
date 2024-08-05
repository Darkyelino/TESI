import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.janela.title('Pack Simples')

        lbl1 = tk.Label(self.janela,text='TOPO', fg='black', bg='yellow')
        lbl1.pack(side= tk.TOP, fill= tk.BOTH, expand=True)

        lbl4 = tk.Label(self.janela, text='RODAPÉ', fg='black', bg='cyan')
        lbl4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        lbl2 = tk.Label(self.janela, text='DIRETA', fg='black', bg='green')
        lbl2.pack(side= tk.RIGHT, fill= tk.X, expand=True)

        lbl3 = tk.Label(self.janela, text='ESQUERDA', fg='black', bg='red')
        lbl3.pack(side= tk.RIGHT, fill= tk.X, expand=True)

        
janela = tk.Tk()
app = Tela(janela)
janela.mainloop()