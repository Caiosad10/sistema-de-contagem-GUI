import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion

from functions.buttons import botaoDestroy

#Janeça principal do sistema de contagem
def janelaPrincipal():
  janelaPrincipal = tk.Tk()
  janelaPrincipal.title("Sistema de contagem de pets")
  janelaPrincipal.geometry("250x500")

  botao_add_pet = ttk.Button(janelaPrincipal, text="Adicionar Pet")
  botao_add_pet.pack()

  botao_lista_pets = ttk.Button(janelaPrincipal, text="Lista de Pets")
  botao_lista_pets.pack()

  botao_destroy = ttk.Button(janelaPrincipal, text="sair", command=botaoDestroy)
  botao_destroy.pack()

  janelaPrincipal.mainloop()

