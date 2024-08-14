import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Lista de Produtos")

# Criar o Treeview com 4 colunas
columns = ("Produto", "Preço", "Estoque", "Categoria")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Configurar os cabeçalhos das colunas
for col in columns:
    tree.heading(col, text=col)

# Inserir dados nos itens
tree.insert('', 'end', text="Produto 1", values=("Notebook", 3500, 10, "Eletrônicos"))
tree.insert('', 'end', text="Produto 2", values=("Smartphone", 2000, 20, "Eletrônicos"))
tree.insert('', 'end', text="Produto 3", values=("Fones de Ouvido", 250, 50, "Eletrônicos"))
tree.insert('', 'end', text="Produto 4", values=("Camiseta", 50, 100, "Vestuário"))
tree.insert('', 'end', text="Produto 5", values=("Calça Jeans", 100, 80, "Vestuário"))
tree.insert('', 'end', text="Produto 6", values=("Livro", 50, 200, "Livros"))

# Exibir o Treeview
tree.pack(pady=20)

root.mainloop()
