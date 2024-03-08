from PIL import Image as PILImage
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
import tkinter
import re
import tkinter.messagebox as messagebox
import csv
import os

# Cria a lista de ambas as pessoas para transforma-las em um arquivo CSV
pessoas_fisicas_cadastradas = []
pessoas_juridicas_cadastradas = []


# Verifica se e-mail digitado é um e-mail válido
def email_valido(email):
    email = email.strip()
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-za-z]{3,}$')
    return bool(email_pattern.match(email))

# Transforma as pessoas físicas em arquivo CSV (salvando-as)
def carregar_csv_fisicas():
    global pessoas_fisicas_cadastradas
    try:
        with open('Pessoa Fisíca.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            pessoas_fisicas_cadastradas = [row for row in reader]
    except FileNotFoundError:
        pessoas_fisicas_cadastradas = []

# Transforma as pessoas jurídicas em arquivo CSV (salvando-as)
def carregar_csv_juridicas():
    global pessoas_juridicas_cadastradas
    try:
        with open('Pessoa Juridíca.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            pessoas_juridicas_cadastradas = [row for row in reader]
    except FileNotFoundError:
        pessoas_juridicas_cadastradas = []

# Lista as pessoas jurídicas cadastradas
def listar_pessoas_juridicas_cadastradas(nome_pesquisa=""):
    global pessoas_juridicas_cadastradas
    nova_janela_listagem = Toplevel(janela_principal)
    carregar_csv_juridicas()

    encontradas = []
    for idx, pessoa_info in enumerate(pessoas_juridicas_cadastradas, start=1):
        if pessoa_info and nome_pesquisa.lower() in pessoa_info[0].lower():
            encontradas.append(pessoa_info)
            pessoa_info_text = "\n".join(pessoa_info)
            label_info = Label(nova_janela_listagem, text=f"Informações da {idx}º pessoa:\n{pessoa_info_text}\n{'=' * 30}")
            label_info.pack()   

    if not encontradas:
        messagebox.showerror("Erro", "Não existe nenhuma pessoa cadastrada.")

# define a listagem da pessoa física
def listar_pessoas_fisicas_cadastradas(nome_pesquisa=""):
    global pessoas_fisicas_cadastradas
    nova_janela_listagem = Toplevel(janela_principal)
    carregar_csv_fisicas()

    encontradas = []
    for idx, pessoa_info in enumerate(pessoas_fisicas_cadastradas, start=1):
        if pessoa_info and nome_pesquisa.lower() in pessoa_info[0].lower():
            encontradas.append(pessoa_info)
            pessoa_info_text = "\n".join(pessoa_info)
            label_info = Label(nova_janela_listagem, text=f"Informações da {idx}º pessoa: \n{pessoa_info_text}\n {'='*30}")
            label_info.pack()

    if not encontradas:
        messagebox.showerror("Erro", "Não existe nenhuma pessoa cadastrada.")


# Cria as janelas de ambas as pessoas 
def criar_janela(tipo):
    nova_janela = Toplevel(janela_principal)
    nova_janela.title("Cadastro Pessoa Física")
                                           # with = ALTURA
    largura_tela = nova_janela.winfo_screenwidth()
                                            # height = LARGURA
    altura_tela = nova_janela.winfo_screenheight()

    nova_janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

# Define o que acontece com a pessoa física
    if tipo == "Pessoa Física":
        nova_janela.title("Cadastro Pessoa Física")

        def cadastro_concluido():
            user_input_nome = str(ed.get()).strip()
            user_input_cpf = str(ed2.get()).strip()
            user_input_email = str(ed3.get()).strip()
            user_input_endereco = str(ed4.get()).strip()
            user_input_complemento = str(ed5.get()).strip() 
            user_input_telefone = str(ed6.get()).strip()

            if not all([user_input_nome, user_input_cpf, user_input_email, user_input_endereco, user_input_telefone]):
                lb["text"] = "Por favor, preencha todos os campos"
            elif not user_input_nome.replace(" ", "").isalpha():
                lb["text"] = "Por favor, digite apenas letras no campo Nome"
            elif not user_input_cpf.isdigit() or len(user_input_cpf) != 11:
                lb["text"] = "Por favor, digite um CPF válido"
            elif not email_valido(user_input_email):
                lb["text"] = "Por favor, digite um e-mail válido"
            elif not user_input_telefone.isdigit or len(user_input_telefone) != 11:
                lb["text"] = "Por favor digite um número de telefone válido! "
            else:
                user_info = [
                    f"Nome: {(user_input_nome)}",
                    f"CPF: {user_input_cpf}",
                    f"E-mail: {(user_input_email)}",
                    f"Endereço: {user_input_endereco}",
                    f"Complemento (Opcional): {(user_input_complemento)}",
                    f"Telefone: {user_input_telefone}",
                ]
                lb["text"] = "Cadastro concluído"
                carregar_csv_fisicas()
                pessoas_fisicas_cadastradas.append(user_info)
                with open('Pessoa Fisíca.csv', mode='a', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(user_info)



        lb2 = Label(nova_janela, text="Nome ")
        lb2.place(x=10, y=30)

        lb3 = Label(nova_janela, text="CPF ")
        lb3.place(x=10, y=70)

        lb4 = Label(nova_janela, text="E-mail ")
        lb4.place(x=10, y=100)

        lb5 = Label(nova_janela, text="Endereço ")
        lb5.place(x=10, y=140)

        lb6 = Label(nova_janela, text="Complemento (Opcional) ")
        lb6.place(x=10, y=170)

        lb7 = Label(nova_janela, text="Telefone ")
        lb7.place(x=10, y=200)

        ed = ttk.Entry(nova_janela, width=20)
        ed.place(x=155, y=30)

        ed2 = ttk.Entry(nova_janela, width=20)
        ed2.place(x=155, y=70)

        ed3 = ttk.Entry(nova_janela, width=20)
        ed3.place(x=155, y=100)

        ed4 = ttk.Entry(nova_janela, width=20)
        ed4.place(x=155, y=140)

        ed5 = ttk.Entry(nova_janela, width=20)
        ed5.place(x=155, y=170)

        ed6 = ttk.Entry(nova_janela, width=20)
        ed6.place(x=155, y=200)

        botao_cadastro = ttk.Button(nova_janela, text="Fazer o cadastro", width=20, command=cadastro_concluido)
        botao_cadastro.place(x=10, y=250)

        lb = Label(nova_janela, fg="red", font=("Arial", 9, "bold"))
        lb.place(x=10, y=280)

# Define o que acontece com a pessoa jurídica
    elif tipo == "Pessoa Jurídica":
        nova_janela.title("Cadastro de Pessoa Jurídica")

        def cadastro_concluido_juridica():
            user_input_nome_juridica = str(ed.get()).strip()
            user_input_cnpj = str(ed2.get()).strip()
            user_input_email_juridica = str(ed3.get()).strip()
            user_input_endereco_juridica = str(ed4.get()).strip()
            user_input_complemento_juridica = str(ed5.get()).strip()
            user_input_telefone_juridica = str(ed6.get()).strip()

            if not all([user_input_nome_juridica, user_input_cnpj, user_input_email_juridica, user_input_endereco_juridica,
                        user_input_telefone_juridica]):
                lb["text"] = "Por favor, preencha todos os campos"
            elif not user_input_nome_juridica.replace(" ", "").isalpha():
                lb["text"] = "Por favor, digite apenas letras no campo Nome"
            elif not user_input_cnpj.isdigit() or len(user_input_cnpj) != 14:
                lb["text"] = "Por favor, digite um CNPJ válido"
            elif not email_valido(user_input_email_juridica):
                lb["text"] = "Por favor, digite um e-mail válido"
            elif not user_input_telefone_juridica.isdigit or len(user_input_telefone_juridica) != 11:
                lb["text"] = "Por favor digite um número de telefone válido! "
            else:
                user_info_juridica = [
                    f"Nome: {(user_input_nome_juridica)}",
                    f"CNPJ: {user_input_cnpj}",
                    f"E-mail: {(user_input_email_juridica)}",
                    f"Endereço: {user_input_endereco_juridica}",
                    f"Complemento (Opcional): {(user_input_complemento_juridica)}",
                    f"Telefone: {user_input_telefone_juridica}",
                ]
                lb["text"] = "Cadastro concluído"
                carregar_csv_juridicas()
                pessoas_juridicas_cadastradas.append(user_info_juridica)
                with open('Pessoa Juridíca.csv', mode='a', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(user_info_juridica)




        lb2 = Label(nova_janela, text="Nome ")
        lb2.place(x=10, y=30)

        lb3 = Label(nova_janela, text="CNPJ ")
        lb3.place(x=10, y=70)

        lb4 = Label(nova_janela, text="E-mail ")
        lb4.place(x=10, y=100)

        lb5 = Label(nova_janela, text="Endereço ")
        lb5.place(x=10, y=140)

        lb6 = Label(nova_janela, text="Complemento (Opcional) ")
        lb6.place(x=10, y=170)

        lb7 = Label(nova_janela, text="Telefone ")
        lb7.place(x=10, y=200)

        ed = ttk.Entry(nova_janela, width=20)
        ed.place(x=155, y=30)

        ed2 = ttk.Entry(nova_janela, width=20)
        ed2.place(x=155, y=70)

        ed3 = ttk.Entry(nova_janela, width=20)
        ed3.place(x=155, y=100)

        ed4 = ttk.Entry(nova_janela, width=20)
        ed4.place(x=155, y=140)

        ed5 = ttk.Entry(nova_janela, width=20)
        ed5.place(x=155, y=170)

        ed6 = ttk.Entry(nova_janela, width=20)
        ed6.place(x=155, y=200)

        botao_cadastro = ttk.Button(nova_janela, text="Fazer o cadastro", width=20, command=cadastro_concluido_juridica)
        botao_cadastro.place(x=10, y=250)

        lb = Label(nova_janela, fg="red", font=("Arial", 9, "bold"))
        lb.place(x=10, y=280)


# Define a função para o botão apagar todas as pessoas cadastradas
def botao_apagar_todos_fisicas():
    try:
        with open('Pessoa Fisíca.csv', "w", newline='') as arquivo:
            arquivo.truncate(0)
        messagebox.showinfo("Aviso", "Todas as pessoas físicas foram apagadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("ERRO", "Ocorreu um erro ao apagar todas as pessoas físicas cadastradas.")

def botao_apagar_todos_juridicas():
    try:
        with open('Pessoa Juridíca.csv', "w", newline='') as arquivo:
            arquivo.truncate(0)
        messagebox.showinfo("Aviso", "Todas as pessoas jurídicas foram apagadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("ERRO", "Ocorreu um erro ao apagar todas as pessoas jurídicas cadastradas.")



#Define o que acontece quando um tipo de pessoa é selecionada
def pessoa_selecionada():
    tipo_selecionado = selecionar_tipo.get()
    if tipo_selecionado in ["Pessoa Física", "Pessoa Jurídica"]:
        criar_janela(tipo_selecionado)

#Define a janela principal e nome título
janela_principal = Tk()
janela_principal.title("Programa Cadastro de Pessoas")

#Permite ou não maximizar a janela
janela_principal.resizable(width=False, height=False)

#Importa imagem de fundo
imagem_path = "gta-6-teaser-1680x1050-13559.png.png"

if os.path.exists(imagem_path):
    imagem_fundo = PILImage.open(imagem_path)

    
    largura_tela = janela_principal.winfo_screenwidth()
    
    altura_tela = janela_principal.winfo_screenheight()

    imagem_fundo.thumbnail((largura_tela, altura_tela))

    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

    canvas = Canvas(janela_principal, width=largura_tela, height=altura_tela)

    canvas.pack()

    canvas.create_image(0, 0, anchor="nw", image=imagem_fundo)

else:
    print(f"Erro: Não foi possível encontrar o arquivo de imagem: {imagem_path}")



#Define a caixa de diálogo e o que contém dentro dela
tipo_de_pessoa = ["Pessoa Física", "Pessoa Jurídica"]
selecionar_tipo = tkinter.ttk.Combobox(values=tipo_de_pessoa)
selecionar_tipo.place(x=30, y=55)

#Define a Label do tipo de pessoa
texto = Label(janela_principal, text="Escolha o tipo de pessoa para cadastro", font=("Arial", 9, "bold"))
texto.place(x=28, y=30)


#Define o botão para listar as pessoas físicas
texto1 = ttk.Button(janela_principal, text="Listar Pessoas Físicas Cadastradas", style="TButton",command=listar_pessoas_fisicas_cadastradas )
texto1.place(x=28, y=120)

#Define o botão para listar as pessoas juridicas
texto2 = ttk.Button(janela_principal, text="Listar Pessoas Jurídicas Cadastradas", style="TButton",command=listar_pessoas_juridicas_cadastradas)
texto2.place(x=28, y=160)

texto3 = ttk.Button(janela_principal, text="Apagar pessoas físicas cadastradas", style="TButton",command=botao_apagar_todos_fisicas)
texto3.place(x=220, y=120)

texto4 = ttk.Button(janela_principal, text="Apagar pessoas jurídicas cadastradas", style="TButton",command=botao_apagar_todos_juridicas)
texto4.place(x=230, y=160)

#Define a função do botão criar
botao = ttk.Button(janela_principal, width=20, text="Criar",style="TButton", command=pessoa_selecionada)
botao.place(x=270, y=52)

#Define as dimensões da janela principal
janela_principal.geometry("490x300+600+300")
janela_principal.mainloop()