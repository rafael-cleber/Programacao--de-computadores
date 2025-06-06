import tkinter as tk




janela = tk.Tk()

janela.title('Gerenciador de Despesa')

tk.Label(janela, text='Valor (R$): ').grid(row=0, column=0, sticky='e')
valor_input = tk.Entry(janela)
valor_input.grid(row=0, column=1, sticky='w')




