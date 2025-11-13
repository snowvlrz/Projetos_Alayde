import tkinter as tk

# função para adicionar números e operadores na tela
def click(botao):
    tela.insert(tk.END, botao)

# função para calcular o resultado
def calcular():
    try:
        resultado = eval(tela.get())
        tela.delete(0, tk.END)
        tela.insert(tk.END, str(resultado))
    except:
        tela.delete(0, tk.END)
        tela.insert(tk.END, "Erro")

# função para limpar a tela
def limpar():
    tela.delete(0, tk.END)

# criar a janela
janela = tk.Tk()
janela.title("Calculadora")

# criar tela de entrada
tela = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="ridge")
tela.grid(row=0, column=0, columnspan=4)

# botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# criar e posicionar os botões
linha = 1
coluna = 0
for botao in botoes:
    if botao == "=":
        tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 18), command=calcular).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 18), command=lambda b=botao: click(b)).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# botão de limpar
tk.Button(janela, text="C", width=5, height=2, font=("Arial", 18), command=limpar).grid(row=linha, column=0)

janela.mainloop()
