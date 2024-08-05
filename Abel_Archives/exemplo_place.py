import tkinter as tk

# Com "side" você pode definir o posicionamento das labels colocadas dentro da aplicação, sendo LEFT, RIGHT, TOP, DOWN
# Com "padx" ou "pady" você pode definir o espaçamento de uma label para outra, com um campo invisivel
#
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        lbl1 = tk.Label(self.janela,text='BANDEIRA', fg='black', bg='#009E60')
        lbl1.pack(side= tk.TOP, padx=20, fill= tk.BOTH, expand=True)
        lbl2 = tk.Label(self.janela, text='DO', fg='black', bg='#FCD116')
        lbl2.pack(side= tk.TOP, padx=20, fill= tk.BOTH, expand=True)
        lbl3 = tk.Label(self.janela, text='GABÃO', fg='black', bg='#4664B2')
        lbl3.pack(side= tk.TOP, padx=20, fill= tk.BOTH, expand=True)

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()