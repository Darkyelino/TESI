import tkinter as tk

# Com "side" você pode definir o posicionamento das labels colocadas dentro da aplicação, sendo LEFT, RIGHT, TOP, DOWN
# Com "padx" ou "pady" você pode definir o espaçamento de uma label para outra, com um campo invisivel
#
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        lbl1 = tk.Label(self.janela,text='BANDEIRA', fg='black', bg='#009E60')
        lbl1.grid(row=2, column=0)
        lbl2 = tk.Label(self.janela, text='DO', fg='black', bg='#FCD116')
        lbl2.grid(row=2, column=1)
        lbl3 = tk.Label(self.janela, text='GABÃO', fg='black', bg='#4664B2')
        lbl3.grid(row=2, column=2)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()