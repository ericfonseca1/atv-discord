# Importar bibliotecas necessárias
import random # Fornece funções para geração de números aleatórios, usadas para gerar notas aleatórias.
import tkinter as tk # Biblioteca GUI para criação de janelas, botões e outros elementos de UI.importar tkinter como tk
from tkinter import ttk # Extensão do tkinter que fornece um conjunto de widgets temáticos.
from tkinter import messagebox # Usada para criar caixas de diálogo modais padrão, como mensagens de alerta.
from tkinter import * # Biblioteca principal do tkinter 
import webbrowser #utilizado pra criar um hiperlink para o discord

# Define uma classe 'Aluno' para representar o aluno
class Aluno:
    def __init__(self, nome, comunidade, media):
        self.nome = nome
        self.comunidade = comunidade
        self.media = media

# Cria uma lista de objetos 'Aluno' representando os alunos
alunos = [
    Aluno("Albert Duarte Costa", "Discord", 0.0),
    Aluno("Altair de Jesus Santos Junior", "Trello", 0.0),
    Aluno("Amanda Oliveira da Silva", "Softskills", 0.0),
    Aluno("Ana Caroline da Silva Muniz", "Empregabilidade", 0.0),
    Aluno("Antonio de Sousa Silva", "Empregabilidade", 0.0),
    Aluno("Átila Conceição de Goes", "Lideres", 0.0),
    Aluno("Caique Vidal Gonzaga de Freitas", "Monitoria", 0.0),
    Aluno("Douglas Henrique da Conceição Souza", "Notícias Tech", 0.0),
    Aluno("Eduardo Santos da Conceicão", "Trello", 0.0),
    Aluno("Eric dos Santos Fonseca", "Discord", 0.0),
    Aluno("Erick Macedo de Almeida", "Github", 0.0),
    Aluno("Filipe Da Silva Santos", "Monitoria", 0.0),
    Aluno("Filipe Sobreira Campos", "Notícias Tech", 0.0),
    Aluno("Gabriele de Jesus da Costa", "Monitoria", 0.0),
    Aluno("Liliana Lima do Carmo", "Empregabilidade", 0.0),
    Aluno("Luiz Claudio Meneses dos Santos", "Discord", 0.0),
    Aluno("Marlon Gabriel Araujo dos Santos", "Monitoria", 0.0),
    Aluno("Marta São Pedro de Santana Cordolino", "Trello", 0.0),
    Aluno("Mateus Ferreira de Oliveira", "Notícias Tech", 0.0),
    Aluno("Matheus Santa Rita dos Santos", "Lideres", 0.0),
    Aluno("Pedro César Da Silva Santos Júnior", "Github", 0.0),
    Aluno("Ramon Fernando Miranda de Oliveira", "Empregabilidade", 0.0),
    Aluno("Sédriky Logan Dantas de Oliveira", "Softskills", 0.0),
    Aluno("Tamires dos Santos de Jesus", "Softskills", 0.0),
    Aluno("Tawan Correia Leonel", "Empregabilidade", 0.0),
    Aluno("Thalys Márcio Bezerra Neves", "Monitoria", 0.0)
]

# Função para mostrar uma caixa de diálogo de mensagem
def mostrar_mensagem(mensagem):
    messagebox.showinfo("Mensagem", mensagem)

# Função para o primeiro menu
def meni1():
    janela = tk.Tk() # Cria a janela principal do Tkinter
    janela.title("DISCORD") # Define o título da janela
    janela.geometry("400x350") # Define o tamanho da janela
    janela.configure(background="#ADD8E6") # Define a cor de fundo
    
    # Função para abrir link do Discord
    def link_discord():
        mostrar_mensagem(f'Link para acessar o Discord: \n\n{webbrowser.open("https://discord.com/channels/1142723554476044338/1142723554941608006")}')

    # Função para acessar comunidades
    def acessar_comunidades():
        janela.destroy()
        meni2()
       
    # Função para acessar o boletim (notas)    
    def acessar_boletim():
        janela.destroy()
        boletim()

    # Configura estilo do botão
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))

    # Carrega e exibe o logotipo do Discord    
    imagem_discord = PhotoImage(file='logodc.png')
    proporcao = 2
    imagem_reduzida = imagem_discord.subsample(proporcao, proporcao)
    lbl_discord = Label(janela, image=imagem_reduzida, bg="#ADD8E6")
    lbl_discord.pack(pady=15)

    # Cria botões para diversas ações
    btn_link = ttk.Button(janela, text="Acessar Link",style='RoundedButton.TButton', command=link_discord)
    btn_link.pack(pady=10)

    btn_comunidades = ttk.Button(janela, text="Acessar Comunidades",style='RoundedButton.TButton', command=acessar_comunidades)
    btn_comunidades.pack(pady=10)
    
    btn_boletim = ttk.Button(janela, text="Acessar Boletim",style='RoundedButton.TButton', command=acessar_boletim)
    btn_boletim.pack(pady=10)
    
    btn_sair = ttk.Button(janela, text="Sair do sistema",style='RoundedButton.TButton', command=janela.destroy)
    btn_sair.pack(pady=10)
    
    janela.mainloop()
    
def meni2():
    janela = tk.Tk() # Função para o segundo menu
    janela.title("COMUNIDADES") # Define o título da janela
    janela.geometry("450x560") # Define o tamanho da janela
    janela.configure(background="#ADD8E6") # Define a cor de fundo
   
    # Carrega e exibe a imagem 
    imagem_comu = PhotoImage(file='comu.png')
    lbl_comu = Label(janela, image=imagem_comu, bg="#ADD8E6")
    lbl_comu.pack(pady=10)
    
    # Função para acessar uma comunidade específica
    def acessar_comunidade(comunidade):
        membros = obter_membros_comunidade(comunidade)
        mostrar_membros_comunidade(comunidade, membros)
    
    # Função para obter membros de uma comunidade
    def obter_membros_comunidade(comunidade):
        membros = [aluno.nome for aluno in alunos if aluno.comunidade == comunidade]
        return membros

    # Função para exibir membros de uma comunidade em uma nova janela
    def mostrar_membros_comunidade(comunidade, membros):
        janela = tk.Tk()
        janela.title(f"Membros da Comunidade - {comunidade}")
        janela.configure(background="#ADD8E6")

        label = tk.Label(janela, text=f"Membros da Comunidade - {comunidade}", font=("Helvetica", 16,'bold'),bg="#ADD8E6")
        label.pack(pady=10)

        if membros:
            for membro in membros:
                label_membro = tk.Label(janela, text=membro,bg="#ADD8E6",font=("Helvetica", 11))
                label_membro.pack()
                
        style = ttk.Style()
        style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))
        btn_ok = ttk.Button(janela, text="OK",style='RoundedButton.TButton', command=janela.destroy)
        btn_ok.pack(pady=10)

        janela.mainloop()
    
    # Função para voltar ao primeiro menu 
    def cmd1():
        janela.destroy()
        meni1()
        
    # Configura estilo do botão
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))

    # Cria botões para cada comunidade e um botão para voltar
    btn_empregabilidade = ttk.Button(janela, text="Empregabilidade",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Empregabilidade"))
    btn_empregabilidade.pack(pady=10)
    
    btn_noticias_tech = ttk.Button(janela, text="Notícias Tech",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Notícias Tech"))
    btn_noticias_tech.pack(pady=10)

    btn_trello = ttk.Button(janela, text="Trello",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Trello"))
    btn_trello.pack(pady=10)

    btn_github = ttk.Button(janela, text="Github",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Github"))
    btn_github.pack(pady=10)

    btn_monitoria = ttk.Button(janela, text="Monitoria",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Monitoria"))
    btn_monitoria.pack(pady=10)

    btn_lideres = ttk.Button(janela, text="Lideres",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Lideres"))
    btn_lideres.pack(pady=10)

    btn_softskills = ttk.Button(janela, text="Softskills",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Softskills"))
    btn_softskills.pack(pady=10)

    btn_discord = ttk.Button(janela, text="Discord",style='RoundedButton.TButton', command=lambda: acessar_comunidade("Discord"))
    btn_discord.pack(pady=10)

    btn_voltar = ttk.Button(janela, text="Voltar",style='RoundedButton.TButton', command=cmd1)
    btn_voltar.pack(pady=10)
    janela.mainloop()

# Função para menu de boletim   
def boletim():
    janela = tk.Tk() 
    janela.title("BOLETIM")
    janela.configure(background="#ADD8E6")
    janela.geometry("300x250")
    proporcao = 4
    imagem_bole = PhotoImage(file='boletim.png')
    imagem_reduzida = imagem_bole.subsample(proporcao, proporcao)
    lbl_bole = Label(janela, image=imagem_reduzida, bg="#ADD8E6")
    lbl_bole.pack(pady=10)
    
    #Função para adicionar notas manualmente  
    def adicionar_notas():
        top_window = tk.Toplevel()
        top_window.title("Adicionar Notas")
        top_window.configure(background="#ADD8E6")
        label = tk.Label(top_window, text="Adicionar Notas", font=("Helvetica", 16), bg="#ADD8E6")
        label.grid(row=0, column=0, columnspan=3, pady=10)

        canvas = tk.Canvas(top_window)
        canvas.grid(row=1, column=0, columnspan=3)

        scrollbar = tk.Scrollbar(top_window, orient="vertical", command=canvas.yview, bg="#ADD8E6")
        scrollbar.grid(row=1, column=3, sticky="ns")

        frame = tk.Frame(canvas, bg="#ADD8E6")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        entry_notas = {}
        for i, aluno in enumerate(alunos, start=1):
            label_aluno = tk.Label(frame, text=f"{aluno.nome}: ", bg="#ADD8E6", font=("Helvetica", 10))
            label_aluno.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            entry_nota = tk.Entry(frame)
            entry_nota.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entry_notas[aluno] = entry_nota

            canvas.update_idletasks()

            canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set, bg="#ADD8E6")

        def salvar_notas():
            for aluno in alunos:
                try:
                    nota = float(entry_notas[aluno].get())
                    if 0.0 <= nota <= 10.0:
                        aluno.media = nota
                    else:
                        mostrar_mensagem("Nota inválida! Deve estar entre 0.0 e 10.0.")
                        return
                except ValueError:
                    mostrar_mensagem("Nota inválida! Deve ser um número.")
                    return
                
            mostrar_mensagem("Notas salvas com sucesso!")
            verificar_aprovacao()
            top_window.destroy()

        def verificar_aprovacao():
            aprovados = [aluno.nome for aluno in alunos if aluno.media >= 7.0]
            reprovados = [aluno.nome for aluno in alunos if aluno.media < 7.0]

            mensagem_aprovacao = f"\nAprovados: {', '.join(aprovados)}" if aprovados else "\nNenhum aluno aprovado."
            mensagem_reprovacao = f"\nReprovados: {', '.join(reprovados)}" if reprovados else "\nNenhum aluno reprovado."

            mensagem_final = f"Resultados:\n{mensagem_aprovacao}\n{mensagem_reprovacao}"

            messagebox.showinfo("Resultados", mensagem_final)
            
        btn_salvar = ttk.Button(top_window, text="Salvar Notas",style='RoundedButton.TButton', command=salvar_notas)
        btn_salvar.grid(row=len(alunos) + 1, column=0, columnspan=3, pady=10)

    #Função para gerar notas aleatórias
    def gerar_notas_aleatorias():
        for aluno in alunos:
            nota_aleatoria = round(random.uniform(0.0, 10.0), 2)
            aluno.media = nota_aleatoria
            
        def verificar_aprovacao():
            aprovados = [aluno.nome for aluno in alunos if aluno.media >= 7.0] 
            media_ap = [aluno.media for aluno in alunos if aluno.media >= 7.0]
            reprovados = [aluno.nome for aluno in alunos if aluno.media < 7.0]
            media_rep = [aluno.media for aluno in alunos if aluno.media < 7.0]

            mensagem_aprovacao = f"\nAprovados: {aprovados} -> {media_ap}\n" if aprovados else "\nNenhum aluno aprovado."
            mensagem_reprovacao = f"\nReprovados: {', '.join(reprovados)}" if reprovados else "\nNenhum aluno reprovado."

            mensagem_final = f"Resultados:\n{mensagem_aprovacao}\n{mensagem_reprovacao}"

            messagebox.showinfo("Resultados", mensagem_final)
            
        mostrar_mensagem("Notas aleatórias geradas com sucesso!")
        verificar_aprovacao()
        
    def cmd1():
        janela.destroy()
        meni1()
    
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))

    btn_adicionar = ttk.Button( janela, text="Adicionar Notas",style='RoundedButton.TButton', command=adicionar_notas)
    btn_adicionar.pack(pady=10)
    
    btn_gerar_aleatorias = ttk.Button(janela, text="Gerar Notas Aleatórias", style='RoundedButton.TButton', command=gerar_notas_aleatorias)
    btn_gerar_aleatorias.pack(pady=10)

    btn_sair = ttk.Button( janela, text="Voltar",style='RoundedButton.TButton', command=cmd1)
    btn_sair.pack(pady=10)
    
    janela.mainloop()

if __name__ == "__main__":
    meni1()