import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion



import dados

janela_add_pet = tk.Tk()


def add_pet(name, raça):
  dados.pets.append(dados.Pet(name, raça))

def inputname():
  name = input("Nome do pet: ")
  return name

def inputraça():
  raça = input("Raça do pet: ")
  return raça