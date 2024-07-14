import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion

from functions.buttons import janelaLogin

#Janela de boas vindas
janela = tk.Tk()
janela.title("Sistema de contagem de pets")
janela.geometry("250x500")

#Mensagem de boas vindas
mensagem = ttk.Label(janela, text="Bem vindo ao sistema de contagem de pets!")
mensagem.pack()
#Botão de login
botao = ttk.Button(janela, text="Login", command=janelaLogin)
botao.pack()

      
janela.mainloop()