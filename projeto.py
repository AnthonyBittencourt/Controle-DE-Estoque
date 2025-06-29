
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
from pygame.locals import *
# Cores
coRpreto = "#000000"
coRbranco = "#feffff"
coRcinza = "#353535"
coRazul = "#38576b"
coRcinza2 = "#403d3d"
coRvermelho = "#ff0000"
coRvermelhoEsc = "#a40000"
# Variável para guardar credenciais (apenas exemplo, não persistente)
credenciais = ['1', '1']

# Criando janela principal
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(bg=coRbranco)



# Frames
frame_cima = Frame(janela, width=310, height=50, bg=coRbranco, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=coRbranco, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame_cima
l_nome = Label(frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy 25'), bg=coRbranco, fg=coRcinza2)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 25'), bg=coRcinza)
l_linha.place(x=10, y=45)

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin!!!')

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])

        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome do usuário ou a palavra passe')

def nova_janela():

    jogos_text = Label(frame_cima, text='OPÇÕES:', bg=coRbranco, fg=coRpreto, font=('Ivy 25 bold'),)
    jogos_text.place(x=85, y=10)
    linha = Label(frame_cima, text='', width=30, bg=coRcinza)
    linha.place(x=49, y=48)
    control_estoque_b = Button(frame_baixo, text='Controle de \n estoque', width=10, height=2, font=('Ivy 10 bold'),relief=RAISED, overrelief=SOLID, bg=coRazul, fg=coRbranco, command=abrir_janela_ctrlEstoque)
    control_estoque_b.place(x = 60, y = 5)
    vendas_b = Button(frame_baixo, text='Vendas', width=10, height=2, font=('Ivy 10 bold'), anchor='center',relief=RAISED, overrelief=SOLID, bg=coRazul, fg=coRbranco, command=abrir_janela_vendas)
    vendas_b.place(x = 160, y = 5)

def abrir_janela_cadastro():
    def salvar_cadastro():
        novo_nome = entry_nome.get()
        nova_senha = entry_Novasenha.get()
        senhaantiga = entry_senha.get()

        senhaINC_l = Label(janela_cadastro, text="Senha incorreta. Tente novamente", bg=coRbranco, fg=coRbranco, font=("Ivy", 7))
        senhaINC_l.place(x=90, y=90)
        
        while senhaantiga == credenciais[1]:
            senhaINC_l.config(fg = coRbranco)
            break

        if senhaantiga != credenciais[1]:
            senhaINC_l.config(fg = coRvermelho)

        elif len(nova_senha) < 8:
            Label(janela_cadastro, text="senha inválida. necessário no mínimo 8 caracteres.", bg=coRbranco, fg=coRvermelho, font=("Ivy", 7)).place(x=90, y=130)
        
        elif nova_senha == credenciais[1]:
            Label(janela_cadastro, text="a senha deve ser diferente da atual", bg=coRbranco, fg=coRvermelho, font=("Ivy", 6)).place(x=90, y=130)

        elif novo_nome and nova_senha:
            credenciais[0] = novo_nome
            credenciais[1] = nova_senha
            messagebox.showinfo("Cadastro", "Usuário atualizado com sucesso!")
            janela_cadastro.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    janela_cadastro = Toplevel(janela)
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("350x300")
    janela_cadastro.configure(bg=coRbranco)
    janela_cadastro.resizable(False, False)

    Label(janela_cadastro, text="    Nome:", bg=coRbranco, fg=coRcinza2, justify='right', font=("Ivy", 10)).place(x=10, y=30)
    entry_nome = Entry(janela_cadastro, width=40)
    entry_nome.place(x=90, y=30)

    Label(janela_cadastro, text="Senha atual:", bg=coRbranco, fg=coRcinza2, font=("Ivy", 10)).place(x=10, y=70)
    entry_senha = Entry(janela_cadastro, width=40, show="*")
    entry_senha.place(x=90, y=70)

    Label(janela_cadastro, text="Nova senha:", bg=coRbranco, fg=coRcinza2, font=("Ivy", 10)).place(x=10, y=110)
    entry_Novasenha = Entry(janela_cadastro, width=40, show="*")
    entry_Novasenha.place(x=90, y=110)

    Button(janela_cadastro, text="Atualizar", bg=coRcinza, fg=coRbranco, font=("Ivy", 10), command=salvar_cadastro).place(x=70, y=170)

# Campos do login
l_nome = Label(frame_baixo, text="Name *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
e_nome.place(x=14, y=40)

l_pass = Label(frame_baixo, text="Password *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
l_pass.place(x=10, y=90)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
e_pass.place(x=14, y=110)

# Botões
botao_confirmar = Button(frame_baixo, text="Entrar", width=39, height=2, bg=coRcinza, fg=coRbranco, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=15, y=150)

botao_cadastrar = Button(frame_baixo, text="Atualizar", width=39, height=2, bg=coRazul, fg=coRbranco, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_janela_cadastro)
botao_cadastrar.place(x=15, y=200)

def abrir_janela_ctrlEstoque():
    def abrir_adicionar_estoque():
        jnl_adicionar_estoque = Toplevel(janela)
        jnl_adicionar_estoque.title("estoque")
        jnl_adicionar_estoque.geometry("260x250")
        jnl_adicionar_estoque.configure(bg=coRbranco)
        jnl_adicionar_estoque.resizable(False, False)

        frame_cimaAddE = Frame(jnl_adicionar_estoque, width=260, height=50, bg=coRbranco, relief='flat')
        frame_cimaAddE.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixoAddE = Frame(jnl_adicionar_estoque, width=260, height=300, bg=coRbranco, relief="flat")
        frame_baixoAddE.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        l_preco = Label(frame_cimaAddE, text="preço", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
        l_preco.place(x=14, y=1)
        e_preco = Entry(frame_cimaAddE, width=15, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
        e_preco.place(x=14, y=20)

        l_produto = Label(frame_baixoAddE, text="Produto", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
        l_produto.place(x=10, y=5)
        e_produto = Entry(frame_baixoAddE, width=15, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
        e_produto.place(x=14, y=25)

        l_quantidade = Label(frame_baixoAddE, text="quantidade", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
        l_quantidade.place(x=10, y=65)
        e_quantidade = Entry(frame_baixoAddE, width=3, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
        e_quantidade.place(x=14, y=85)

        def salvar_produtos():
            prod = str(e_produto.get())
            quant = str(e_quantidade.get())
            preco = str(e_preco.get())
            with open('estoque.txt', 'a') as arquivo:
                arquivo.write(f'{prod} \n {preco} \n {quant}\n')
        
        def voltar_pag():
            jnl_adicionar_estoque.destroy()


        botao_salvar = Button(frame_baixoAddE, text='Adicionar', width=8, font=('Arial 10 bold'), bg=coRazul, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=salvar_produtos)
        botao_salvar.place(x=15, y = 140)
        botao_voltar = Button(frame_baixoAddE, text='Sair', width=8, relief=RAISED, font=('Arial 10 bold'), bg=coRcinza2, fg=coRbranco, overrelief=SOLID, command= voltar_pag)
        botao_voltar.place(x=90, y=140)
    def abrir_remover_estoque():
        jnl_remover_estoque = Toplevel(janela)
        jnl_remover_estoque.title("estoque")
        jnl_remover_estoque.geometry("260x250")
        jnl_remover_estoque.configure(bg=coRbranco)
        jnl_remover_estoque.resizable(False, False)

        frame_cimaremoverE = Frame(jnl_remover_estoque, width=260, height=50, bg=coRbranco, relief='flat')
        frame_cimaremoverE.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
        frame_baixoremoverE = Frame(jnl_remover_estoque, width=260, height=300, bg=coRbranco, relief="flat")
        frame_baixoremoverE.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        l_remover = Label(frame_cimaremoverE, text="Qual produto deseja remover?", height=1, anchor=NW, font=("Ivy 10 bold"), bg=coRbranco, fg=coRcinza2)
        l_remover.place(x=14, y=25)
        e_remover = Entry(frame_baixoremoverE, width=15, justify='left', font=("", 15), highlightbackground=coRbranco, relief="solid")
        e_remover.place(x=14, y=25)


        def remover_produto():
            prodremove = e_remover.get().strip().lower()
            try:
                with open('estoque.txt', 'r') as arquivo:
                    linhas = arquivo.readlines()

                nova_lista = []
                i = 0
                while i < len(linhas):
                    produto = linhas[i].strip().lower()
                    if produto == prodremove:
                        # pula as 3 linhas (produto, preço, quantidade)
                        i += 3
                        continue
                    else:
                        # mantém as linhas se não for o produto a remover
                        nova_lista.extend(linhas[i:i+3])
                        i += 3

                with open('estoque.txt', 'w') as arquivo:
                    arquivo.writelines(nova_lista)

                messagebox.showinfo('Remover produto', f'Produto "{prodremove}" removido com sucesso!')
            except FileNotFoundError:
                messagebox.showerror('Erro', 'Arquivo de estoque não encontrado.')
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao remover produto: {e}')
        def sair_jnl_remover():
            jnl_remover_estoque.destroy()
        confirm_remover_b = Button(frame_baixoremoverE,text='remover', width=15, font=('Arial 10 bold'), bg=coRvermelhoEsc, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=remover_produto)
        confirm_remover_b.place(x=5, y=100)
        sair_remover_b = Button(frame_baixoremoverE,text='sair', width=7, font=('Arial 10 bold'), bg=coRvermelhoEsc, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=sair_jnl_remover)
        sair_remover_b.place(x=140, y=100)


        

    janela_estoque = Toplevel(janela)
    janela_estoque.title("estoque")
    janela_estoque.geometry("350x300")
    janela_estoque.configure(bg=coRbranco)
    janela_estoque.resizable(False, False)

    frame_cimaE = Frame(janela_estoque, width=350, height=50, bg=coRbranco, relief='flat')
    frame_cimaE.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixoE = Frame(janela_estoque, width=350, height=300, bg=coRbranco, relief="flat")
    frame_baixoE.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    ctrlE_txt = Label(frame_cimaE, text='Controle de Estoque', width=20, font=("Ivy 15 bold"), bg=coRbranco, fg=coRpreto)
    ctrlE_txt.place(x=50, y=15)
    ctrlE_linha = Label(frame_cimaE, text='', width=500, font=('Arial 1'), bg=coRcinza)
    ctrlE_linha.place(x=0, y=45)
    adicionar_b = Button(frame_baixoE,text='Adicionar ao Estoque', width=17, height=2, font=('Ivy 10 bold'), bg=coRazul, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=abrir_adicionar_estoque)
    adicionar_b.place(x=95, y=5)
    remover_b = Button(frame_baixoE,text='Remover do Estoque', width=17, height=2, font=('Ivy 10 bold'), bg=coRazul, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=abrir_remover_estoque)
    remover_b.place(x=95, y=50)

    def voltar_ctrl_estoque():
        janela_estoque.destroy()
    voltar_b = Button(frame_baixoE,text='voltar', width=8, height=1, font=('Ivy 10 bold'), bg=coRvermelhoEsc, fg=coRbranco, relief=RAISED, overrelief=SOLID, command=voltar_ctrl_estoque)
    voltar_b.place(x=270, y=210)

precoVendido = 0.0
def abrir_janela_vendas():
    janela_vendas = Toplevel(janela)
    janela_vendas.title("vendas")
    janela_vendas.geometry("350x300")
    janela_vendas.configure(bg=coRbranco)
    janela_vendas.resizable(False, False)

    frame_cimaV = Frame(janela_vendas, width=350, height=50, bg=coRbranco, relief='flat')
    frame_cimaV.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixoV = Frame(janela_vendas, width=350, height=300, bg=coRbranco, relief="flat")
    frame_baixoV.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    venda_txt = Label(frame_cimaV, text='Vendas', width=20, font=("Ivy 15 bold"), bg=coRbranco, fg=coRpreto)
    venda_txt.place(x=50, y=15)
    venda_linha = Label(frame_cimaV, text='', width=500, font=('Arial 1'), bg=coRcinza)
    venda_linha.place(x=0, y=40)
    def vender_produtos():
        for widget in frame_cimaV.winfo_children():
            widget.destroy()
        for widget in frame_baixoV.winfo_children():
            widget.destroy()

        texto_vender = Label(frame_cimaV, text='Produto', fg=coRpreto, font=('Ivy 10 bold'),)
        texto_vender.place(x = 15, y = 5)
        produtoVendido_e = Entry(frame_baixoV,width=20, justify='left', font=('', 10), highlightbackground=coRbranco, relief=SOLID)
        produtoVendido_e.place(x=15, y= 5)

        texto_venderq = Label(frame_baixoV, text='quantidade', fg=coRpreto, font=('Ivy 10 bold'),)
        texto_venderq.place(x = 15, y = 30)
        quantidadeVendida_e = Entry(frame_baixoV,width=20, justify='left', font=('', 10), highlightbackground=coRbranco, relief=SOLID)
        quantidadeVendida_e.place(x=15, y= 50)

        def venderProdutos():
            produto_nome = produtoVendido_e.get().strip().lower()
            try:
                qtd_vendida = int(quantidadeVendida_e.get().strip())
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida.")
                return

            try:
                with open('estoque.txt', 'r') as arquivo:
                    linhas = arquivo.readlines()

                atualizado = False
                nova_lista = []
                i = 0
                
                while i < len(linhas):
                    nome = linhas[i].strip().lower()
                    preco = float(linhas[i+1].strip())
                    quantidade = int(linhas[i+2].strip())

                    if nome == produto_nome:
                        if quantidade >= qtd_vendida:
                            quantidade -= qtd_vendida
                            atualizado = True
                            global precoVendido
                            precoVendido += float(preco) * qtd_vendida
                            if quantidade > 0:
                                nova_lista.extend([f"{nome}\n", f"{preco}\n", f"{quantidade}\n"])
                            # Se quantidade == 0, não adiciona às novas linhas → o produto é removido
                        else:
                            messagebox.showwarning("Estoque insuficiente", f"Apenas {quantidade} disponíveis.")
                            return
                    else:
                        nova_lista.extend(linhas[i:i+3])
                    i += 3

                if not atualizado:
                    messagebox.showwarning("Erro", "Produto não encontrado.")
                    return

                with open('estoque.txt', 'w') as arquivo:
                    arquivo.writelines(nova_lista)

                messagebox.showinfo("Venda", "Venda realizada com sucesso!")
                produtoVendido_e.delete(0, END)
                quantidadeVendida_e.delete(0, END)

            except FileNotFoundError:
                messagebox.showerror("Erro", "Arquivo de estoque não encontrado.")

        botao_vender = Button(frame_baixoV, text='Vender', width=10, bg=coRazul, fg=coRbranco, font=('Ivy 10 bold'),
                            relief=RAISED, overrelief=SOLID, command=venderProdutos)
        botao_vender.place(x=15, y=100)

        def voltar_vender_produtos():
            janela_vendas.destroy()
            abrir_janela_vendas()

        botao_voltar = Button(frame_baixoV, text='voltar', width=10, bg=coRvermelhoEsc, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=SOLID, command=voltar_vender_produtos)
        botao_voltar.place(x=150, y=200)
    def ver_total_produtos():
        for widget in frame_cimaV.winfo_children():
            widget.destroy()
        for widget in frame_baixoV.winfo_children():
            widget.destroy()
        
        global precoVendido
        total_produtostxt = Label(frame_cimaV, text='Total Vendido', font=('Ivy 10 bold'), bg=coRbranco, fg=coRpreto).place(x=5, y=5)
        total_produtosquant = Label(frame_cimaV, text=f'R$ {precoVendido:.2f}', font=('Ivy 10 bold'), bg=coRbranco, highlightbackground= coRbranco, fg=coRpreto).place(x=40, y=5)

        def reiniciar_total():
            global precoVendido
            precoVendido = 0.0
            messagebox.showinfo("Reset", "Total de vendas reiniciado.")
            ver_total_produtos()  # Atualiza a tela com o novo total
        
        botao_reiniciar = Button(frame_baixoV, text='Reiniciar Total', width=15, height=2, bg=coRvermelho, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=SOLID, command=reiniciar_total)
        botao_reiniciar.place(x=100, y=50)

        # Botão para voltar à tela principal de vendas
        def voltar_ver_total():
            janela_vendas.destroy()
            abrir_janela_vendas()

        botao_voltar = Button(frame_baixoV, text='Voltar', width=10, bg=coRvermelhoEsc, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=SOLID, command=voltar_ver_total)
        botao_voltar.place(x=125, y=120)

        
    vender_b = Button(frame_baixoV, text="Venda", width=15, height=2, bg=coRazul, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, command=vender_produtos)
    vender_b.place(x=120, y=5)
    ver_total_b = Button(frame_baixoV, text='Total vendido', width=15, height=2, bg= coRazul, fg=coRbranco, font=('Ivy 10 bold'), relief=RAISED, overrelief=SOLID, command=ver_total_produtos)
    ver_total_b.place(x=120, y=50)


janela.mainloop()