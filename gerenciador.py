import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from logica import listar_despesas


def adicionar():
    valor = valor_input.get()
    data = input_data.get()
    status = status_var.get()

    if not valor or data or status:
        messagebox.showwarning('Erro', 'Preencha todos os dados')


def atualizar_lista():
    listbox_despesas.delete(0, tk.END)
    for d in listar_despesas():
        texto = f"{d['data']} - R${d['valor']:.2f} ({d['status']})"
        listbox_despesas.insert(tk.END, texto)




janela = tk.Tk()

janela.title('Gerenciador de Despesa')

tk.Label(janela, text='Valor (R$): ').grid(row=0, column=0, sticky='e')
valor_input = tk.Entry(janela)
valor_input.grid(row=0, column=1, sticky='w')

tk.Label(janela, text='Data (dd/mm/aaaa): ').grid(row=2, column=0, sticky='e')
input_data = tk.Entry(janela)
input_data.grid(row=2, column=1, sticky='w')


tk.Label(janela, text='Status: ').grid(row=3, column=0, sticky='e')
status_var = tk.StringVar(value="Pendente")
status_menu = ttk.Combobox(janela, textvariable=status_var, values=["Paga", "Pendente"])
status_menu.grid(row=3, column=1, sticky='w')


botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar)
botao_adicionar.grid(row=5, column=0, sticky='e')


tk.Label(janela, text="Despesas:").grid(row=6, column=0, columnspan=2)
listbox_despesas = tk.Listbox(janela, width=50)
listbox_despesas.grid(row=6, column=0, columnspan=2, padx=10, pady=5)


fig = plt.Figure(figsize=(5, 3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

janela.mainloop()





