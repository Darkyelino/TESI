import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.janela.title('Gerenciador Grid')

        lbl1 = tk.Label(self.janela, text='1', bg='red')
        lbl1.grid(row=1, column=2)

        lbl2 = tk.Label(self.janela, text='2', bg='blue')
        lbl2.grid(row=2, column=1)

        lbl3 = tk.Label(self.janela, text='3', bg='green')
        lbl3.grid(row=2, column=2)

        lbl4 = tk.Label(self.janela, text='4', bg='yellow')
        lbl4.grid(row=3, column=1)

        lbl5 = tk.Label(self.janela, text='5', bg='pink')
        lbl5.grid(row=3, column=2)

        lbl6 = tk.Label(self.janela, text='6', bg='cyan')
        lbl6.grid(row=3, column=3)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()