import tkinter as tk

class MinhaJanela:
    def __init__(self, master):
        self.janela = master

        # Criando o botão
        self.botao = tk.Button(self.janela, text='Aperte!', width=25, height=6,
                               command=self.minha_funcao)

        # Colocando o botão na janela (usando grid por exemplo)
        self.botao.grid(row=0, column=0)

    def minha_funcao(self):
        # Uma label dizendo que o botão foi clicado vai aparecer abaixo do botão
        self.label = tk.Label(text="O botão foi clicado!")
        self.label.grid(column=0, row=1)

janela = tk.Tk()
app = MinhaJanela(janela)
janela.mainloop()