import tkinter as tk

#A SOMA É SIMPLES MAS O CODIGO NAO TEM NADA DE SIMPLES

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('250x100')
        self.janela.title('Soma Simples')

        janela.resizable(0, 0)

        #Aqui vai ser a entrada do primeiro número:

        lbl_num1 = tk.Label(self.janela, text="Número 1:")
        lbl_num1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.ent_num1 = tk.Entry(self.janela)
        self.ent_num1.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        #Aqui vai ser a entrada do segundo número:

        lbl_num2 = tk.Label(self.janela, text="Número 2:")
        lbl_num2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.ent_num2 = tk.Entry(self.janela)
        self.ent_num2.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        #Aqui vai ser a declaração do botão de somar
        #Falta corrigir retorno!

        btn_soma = tk.Button(self.janela, text="Somar>>", command=self.calcular)
        btn_soma.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.lbl_resultado = tk.Label(self.janela, text=" ", bg="white", fg="black", width=10)
        self.lbl_resultado.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    #Criei uma nova função pra fazer a soma

    def calcular(self):
        num1 = float(self.ent_num1.get())
        num2 = float(self.ent_num2.get())
        resultado = num1 + num2
        self.lbl_resultado.config(text=f"{resultado}")

#Bota pra rodar

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()