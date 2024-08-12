import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('300x100')
janela.title('Progressbar')

prb = ttk.Progressbar(janela, orient='horizontal',
mode='indeterminate')
prb.pack()

btn_start = ttk.Button(janela, text='Start', command=prb.start(10))
btn_start.pack()

btn_stop = ttk.Button(janela, text='Stop', command=prb.stop)
btn_stop.pack()

janela.mainloop()