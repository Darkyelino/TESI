import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.geometry('300x100')
janela.title('Progressbar')
def iniciar():
    prb.step(10)
def parar():
    prb.stop()
prb = ttk.Progressbar(janela, orient='horizontal', mode='determinate', length=200)
prb.pack()
btn_start = ttk.Button(janela, text='Start', command=iniciar)
btn_start.pack()
btn_stop = ttk.Button(janela, text='Stop', command=parar)
btn_stop.pack()
janela.mainloop()