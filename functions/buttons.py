import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askquestion

from functions.janelaprincipal import janelaPrincipal
import main


#Botão de sair
def botaoDestroy():
  escolha = askquestion(
    title="Sair",
    message="Tem certeza?",
  )
  if escolha == "yes":
    janelaPrincipal.destroy()



#Janela de login criada após clicar no botao Login
def janelaLogin():
  janela_login = tk.Tk()
  janela_login.title("Login")
  janela_login.geometry("250x250")

  #Widgets de login
  label_usuario = ttk.Label(janela_login, text="Usuário:")
  label_usuario.pack()
  entry_usuario = ttk.Entry(janela_login)
  entry_usuario.pack()
  label_senha = ttk.Label(janela_login, text="Senha:")
  label_senha.pack()
  entry_senha = ttk.Entry(janela_login, show="*")
  entry_senha.pack()

  #Botão de entrar. Após fazer login, a tela de login é destruída e a tela principal é exibida para fazer o cadastro dos pets
  def login():
      usuario = entry_usuario.get()
      senha = entry_senha.get()
      if usuario == "admin" and senha == "admin":
        showinfo(
          title="Login",
          message="Login realizado com sucesso!"
        )
        janela_login.destroy()
        main.janela.destroy()
        janelaPrincipal()

      else:
          showinfo(
            title="Erro",
            message="Usuário ou senha incorretos!")

  #Botão de login
  botao_login = ttk.Button(janela_login, text="Entrar", command=login)
  botao_login.pack()

