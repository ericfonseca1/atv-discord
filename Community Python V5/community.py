'''
Logica da Programação - Projeto Unidade 3 

Membros da Equipe: Altair Junior 
                   Caique Vidal
                   Erick Fonseca
                   Gabriele Costa
                   Liliana Carmo
                   Luiz Santos
                   Marlon Santos
                   Matheus Oliveira
'''

# Importação de bibliotecas necessárias

import random # Fornece funções para geração de números aleatórios, usadas para gerar notas aleatórias.
import tkinter as tk # Biblioteca GUI para criação de janelas, botões e outros elementos de UI.importar tkinter como tk
from tkinter import ttk # Extensão do tkinter que fornece um conjunto de widgets temáticos.
from tkinter import messagebox # Usada para criar caixas de diálogo modais padrão, como mensagens de alerta.
from tkinter import * # Biblioteca principal do tkinter 
import webbrowser # Utilizado pra criar um hiperlink para o discord.

# Define uma classe 'Aluno' para representar o aluno com atributos nome, comunidade e média
class Aluno:
    def __init__(self, nome, comunidade, media):
        self.nome = nome
        self.comunidade = comunidade
        self.media = media
        

# Lista de objetos 'Aluno' representando os alunos com seus respectivos nomes, comunidades e médias iniciais
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

# Lista de URLs do Linkedin dos alunos.
links = [
        "http://www.linkedin.com/in/albert-duarte-dev",
        "https://www.linkedin.com/in/altairjunior-dev/",
        "https://www.linkedin.com/in/amanda-oliveira-da-silva-453040207/",
        "https://www.linkedin.com/in/ana-caroline-da-silva-muniz-52aba9291/",
        "https://www.linkedin.com/in/antonio-de-sousa-silva-b65381292/",
        "https://www.linkedin.com/in/%C3%A1tila-concei%C3%A7%C3%A3o-de-goes-001030154/",
        "https://www.linkedin.com/in/caique-vidal-gonzaga-de-freitas-764384292/",
        "https://www.linkedin.com/in/douglas-henrique-da-concei%C3%A7%C3%A3o-souza-b5108b243/",
        "https://www.linkedin.com/in/eduardo-santos-da-concei%C3%A7%C3%A3o-386a931ab/",
        "https://www.linkedin.com/in/eric-fonseca-a62080292/",
        "https://www.linkedin.com/in/erick-macedo-tech/",
        "https://www.linkedin.com/in/filipe-da-silva-santos-363b3b1b9/",
        "https://www.linkedin.com/in/filipe-sobreira-74a768175/",
        "https://www.linkedin.com/in/gabrielecosta77/",
        "https://www.linkedin.com/in/liliana-lima-do-carmo-42b5751b4/",
        "https://www.linkedin.com/in/luiz-meneses-470ba7291/",
        "https://www.linkedin.com/in/marlon-gabriel-araujo-dos-santos-1a0ab0266/",
        "https://www.linkedin.com/in/marta-cordolino-90868460/",
        "https://www.linkedin.com/in/mateus-ferreira-de-oliveira-6829a728b/",
        "https://www.linkedin.com/in/matheus-santa-rita-711183257/",
        "https://www.linkedin.com/in/pedro-c%C3%A9sar-da-silva-santos-j%C3%BAnior-a84b86289/",
        "https://www.linkedin.com/in/ramon-oliveira-336379292/",
        "https://www.linkedin.com/in/sedriky-logan-1863831b6/",
        "https://www.linkedin.com/in/tamires-dos-santos-de-jesus-1ab1521a5/",
        "https://www.linkedin.com/in/tawan-correia/",
        "https://www.linkedin.com/in/thalysmarcio/"
    ]

# Função para mostrar uma caixa de diálogo de mensagem
def mostrar_mensagem(mensagem):
    messagebox.showinfo("Mensagem", mensagem)

# Função do menu principal 
# Cria uma janela com botões para acessar o Discord, Comunidades, LinkedIn e Boletim
def menu():
    janela = tk.Tk() # Cria uma instância da classe Tk do módulo tkinter e atribui a variável janela
    janela.title("DISCORD") # Define o título da janela
    janela.geometry("400x390") # Define o tamanho da janela
    janela.configure(background="#ADD8E6") # Define a cor de fundo
    
    # Função para abrir link do Discord
    def link_discord():
        mostrar_mensagem('Abrindo link externo')
        webbrowser.open("https://discord.com/channels/1142723554476044338/1142723554941608006")
        
    # Função para acessar comunidades
    def acessar_comunidades():
        janela.destroy() #fecha a janela principal
        comunidades()
        
    # Função para acessar linkedin dos alunos
    def linkedin_alunos():
        janela.destroy()
        linkedin()
       
    # Função para acessar o boletim    
    def acessar_boletim():
        janela.destroy()
        boletim()

    # Configura estilo do botão
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))

    # Carrega e exibe a imagem   
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
    
    btn_linkedin = ttk.Button(janela, text="Acessar LinkedIn",style='RoundedButton.TButton', command=linkedin_alunos)
    btn_linkedin.pack(pady=10)
    
    btn_boletim = ttk.Button(janela, text="Acessar Boletim",style='RoundedButton.TButton', command=acessar_boletim)
    btn_boletim.pack(pady=10)
    
    btn_sair = ttk.Button(janela, text="Sair do sistema",style='RoundedButton.TButton', command=janela.destroy)
    btn_sair.pack(pady=10)
    
    janela.mainloop() # Inicia o loop principal da interface gráfica

# Cria uma janela com botões para acessar diferentes comunidades
def comunidades():
    janela = tk.Tk() # Cria uma instância da classe Tk do módulo tkinter e atribui a variável janela
    janela.title("COMUNIDADES") # Define o título da janela
    janela.geometry("450x560") # Define o tamanho da janela
    janela.configure(background="#ADD8E6") # Define a cor de fundo
   
    # Carrega e exibe a imagem 
    imagem_comu = PhotoImage(file='comu.png')
    lbl_comu = Label(janela, image=imagem_comu, bg="#ADD8E6")
    lbl_comu.pack(pady=10)
    
    # Função para acessar uma comunidade específica
    def acessar_comunidade(comunidade):
        membros = obter_membros_comunidade(comunidade) # Obtém a lista de membros da comunidade
        mostrar_membros_comunidade(comunidade, membros) # Exibe os membros 
    
    # Função para obter membros de uma comunidade
    def obter_membros_comunidade(comunidade):
        membros = [aluno.nome for aluno in alunos if aluno.comunidade == comunidade]
        '''
        - for aluno in alunos: Itera sobre cada objeto aluno na lista alunos.
        - if aluno.comunidade == comunidade: Verifica se a propriedade comunidade do aluno é igual à comunidade que está sendo passada como argumento para a função.
        - aluno.nome: Seleciona o atributo nome do objeto aluno.
        - [aluno.nome for aluno in alunos if aluno.comunidade == comunidade]: Cria uma lista contendo os nomes dos alunos que satisfazem a condição especificada pelo if.
        '''
        return membros

    # Função para exibir membros de uma comunidade em uma nova janela
    def mostrar_membros_comunidade(comunidade, membros):
        janela = tk.Tk()
        janela.title(f"Comunidade - {comunidade}")
        janela.configure(background="#ADD8E6")

        label = tk.Label(janela, text=f"Comunidade - {comunidade}", font=("Helvetica", 16,'bold'),bg="#ADD8E6")
        label.pack(pady=10)
        label = tk.Label(janela, text=f"Descrição:", font=("Helvetica", 14,'bold'),bg="#ADD8E6")
        label.pack(pady=5)
        
        # Condições para a exibição de determinada descrição
        if comunidade == "Empregabilidade":
            label = tk.Label(janela, text="A comunidade é um ambiente online dedicado exclusivamente à facilitação da busca por oportunidades de emprego.\nOs membros compartilham informações sobre oportunidades de emprego, dicas de recrutamento e experiências pessoais relacionadas ao processo seletivo.\nAlém disso, a comunidade fornece recursos como modelos de currículo, orientações para entrevistas e notícias sobre o mercado de trabalho.\nCom uma abordagem colaborativa, a comunidade se torna um espaço valioso para networking, crescimento profissional e apoio mútuo durante a busca por emprego.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Notícias Tech":
            label = tk.Label(janela, text="Essa comunidade é um espaço virtual dedicado à disseminação e discussão de notícias sobre tecnologia. Seu propósito central é manter os membros informados sobre\n as últimas tendências, inovações e desenvolvimentos no campo da tecnologia. Os participantes compartilham e discutem notícias relacionadas a avanços em inteligência artificial,\n robótica, ciência da computação, dispositivos eletrônicos, software, startups e outros tópicos relevantes. Além de ser uma fonte de informações atualizadas,\n a comunidade proporciona um ambiente propício para a troca de ideias, insights e opiniões entre entusiastas, profissionais e curiosos sobre o mundo da tecnologia.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Trello":
            label = tk.Label(janela, text="Essa comunidade tem como objetivo principal explorar e aprimorar o uso do Trello, uma plataforma de gerenciamento de projetos.\nOs membros compartilham conhecimentos sobre as funcionalidades do Trello e oferecem dicas aos colegas.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Github":
            label = tk.Label(janela, text="Essa comunidade tem como propósito principal explorar e aprimorar o uso do GitHub, uma plataforma amplamente utilizada para controle de versão \ne colaboração em projetos de software. Os membros compartilham conhecimentos sobre os recursos do GitHub, oferecem assistência e \norientação aos colegas em relação a práticas de desenvolvimento,controle de versão, criação de pull requests, resolução de conflitos e \noutros aspectos essenciais da plataforma.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Monitoria":
            label = tk.Label(janela, text="Essa comunidade tem como propósito principal oferecer suporte educacional a uma turma específica por meio de monitorias.\nOs monitores são responsáveis por criar e compartilhar exercícios relacionados aos assuntos abordados nas aulas, proporcionando uma prática adicional aos participantes.\nAlém disso, a comunidade serve como um espaço interativo para tirar dúvidas, onde os alunos podem fazer perguntas sobre os exercícios,\nconceitos ou qualquer conteúdo relacionado ao curso. Os monitores desempenham um papel ativo ao fornecer explicações claras,\n oferecer orientações personalizadas e realizar revisões periódicas para consolidar o aprendizado.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Lideres":
            label = tk.Label(janela, text="Essa comunidade busca fortalecer os laços entre os membros da turma, promover um ambiente positivo de aprendizado e facilitar a comunicação efetiva entre alunos e professores.\nOs líderes atuam como intermediários, ajudando a resolver dúvidas, incentivando a participação ativa em sala de aula \ne contribuindo para a criação de um ambiente de aprendizado inclusivo.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Softskills":
            label = tk.Label(janela, text="Essa comunidade tem como objetivo promover o aprendizado e o desenvolvimento das soft skills entre os alunos.Soft skills, que englobam habilidades interpessoais,\nde comunicação e comportamentais, são essenciais em diversos contextos, tanto pessoais quanto profissionais.A comunidade oferece recursos educacionais,\ncomo workshops, palestras e materiais informativos, para abordar temas relacionados a comunicação eficaz,\nempatia, trabalho em equipe, resiliência e outras competências fundamentais.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        elif comunidade == "Discord":
            label = tk.Label(janela, text="Essa comunidade opera como um ambiente virtual de estudo no Discord, visando facilitar a colaboração e o aprendizado em grupo.\nA função principal é criar e gerenciar um grupo de estudos, organizando salas específicas para cada tema abordado.\n O Discord é utilizado como plataforma central para comunicação e interação entre os membros. Os administradores da comunidade têm a responsabilidade de\n criar canais dedicados a diferentes assuntos, fornecendo um espaço estruturado para discussões, compartilhamento de materiais e\n realização de atividades relacionadas aos estudos. Eles atribuem cargos específicos aos membros,\ncomo moderadores para manter a ordem nas salas e coordenadores para liderar discussões.", font=("Helvetica", 12,'italic'),bg="#ADD8E6")
            label.pack(pady=10)
        
        label = tk.Label(janela, text=f"Membros:", font=("Helvetica", 14,'bold'),bg="#ADD8E6")
        label.pack(pady=5)

        if membros:
            for membro in membros:
                label_membro = tk.Label(janela, text=membro,bg="#ADD8E6",font=("Helvetica", 11))
                label_membro.pack()
        '''
        if membros: Verifica se a lista membros não está vazia. Se a lista não estiver vazia (ou seja, se houver membros na comunidade), o bloco de código dentro do if será executado.
        for membro in membros: Inicia um loop for que percorre cada elemento na lista membros. Em cada iteração, membro recebe o valor do próximo elemento da lista.
        '''          
        style = ttk.Style()
        style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))      
        btn_ok = ttk.Button(janela, text="OK",style='RoundedButton.TButton', command=janela.destroy)
        btn_ok.pack(pady=10)

        janela.mainloop()
          
    # Função para voltar ao primeiro menu 
    def cmd1():
        janela.destroy() # Fecha a janela
        menu() # invoca a funcão menu
        
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

        canvas = tk.Canvas(top_window) # Cria um widget de canvas e o associa à janela top_window
        canvas.grid(row=1, column=0, columnspan=3) # Utiliza o gerenciador de geometria grid para colocar o canvas na grade da janela top_window

        scrollbar = tk.Scrollbar(top_window, orient="vertical", command=canvas.yview, bg="#ADD8E6") # Cria um widget de barra de rolagem vertical associado ao canvas
        scrollbar.grid(row=1, column=3, sticky="ns") # Coloca a barra de rolagem na grade da janela top_window

        frame = tk.Frame(canvas, bg="#ADD8E6") # Cria um widget de frame (Frame) associado ao canvas
        canvas.create_window((0, 0), window=frame, anchor="nw") # Cria uma janela no canvas e associa o widget de frame a essa janela

        entry_notas = {} # Inicializa um dicionário vazio chamado entry_notas para mapear cada aluno para seu respectivo campo de entrada de nota
        for i, aluno in enumerate(alunos, start=1): # Itera sobre a lista de alunos usando a função enumerate, começando o índice em 1. 
            label_aluno = tk.Label(frame, text=f"{aluno.nome}: ", bg="#ADD8E6", font=("Helvetica", 10))
            label_aluno.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            entry_nota = tk.Entry(frame)
            entry_nota.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entry_notas[aluno] = entry_nota

            canvas.update_idletasks() # Atualiza as tarefas pendentes do canvas.

            canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set, bg="#ADD8E6") # Configura o canvas para ser rolável verticalmente. 

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
            '''
            - for aluno in alunos:: Itera sobre a lista de alunos.
            - try:: Inicia um bloco try-except para capturar possíveis erros durante a execução do código dentro do bloco.
            - nota = float(entry_notas[aluno].get()): Obtém o valor inserido no campo de entrada de nota associado ao aluno atual. Converte esse valor para um número de ponto flutuante.
            - if 0.0 <= nota <= 10.0:: Verifica se a nota está dentro do intervalo permitido (entre 0.0 e 10.0).
            - aluno.media = nota: Atribui a nota convertida à propriedade media do objeto aluno.
            - else:: Se a nota não estiver dentro do intervalo permitido, exibe uma mensagem de erro usando a função mostrar_mensagem e retorna da função.
            - except ValueError:: Captura exceções do tipo ValueError, que ocorrem se a conversão para ponto flutuante falhar (por exemplo, se o usuário inserir um texto em vez de um número).
            - mostrar_mensagem("Nota inválida! Deve ser um número."): Exibe uma mensagem de erro indicando que a nota inserida não é um número válido.
            - return: Encerra a execução da função se ocorrer um erro.
            - O bloco (for) continua iterando pelos alunos até que todas as notas sejam processadas.
            - mostrar_mensagem("Notas salvas com sucesso!"): Se todas as notas estiverem corretas, exibe uma mensagem indicando que as notas foram salvas com sucesso. 
            '''
            verificar_aprovacao() # Chama função de verificar os aprovados e reprovados
            top_window.destroy() # Fecha a janela

        # Verifica e exibe quais alunos foram aprovados ou reprovados.
        def verificar_aprovacao():
            aprovados = [(aluno.nome,aluno.media) for aluno in alunos if aluno.media >= 7.0] 
            reprovados = [(aluno.nome,aluno.media) for aluno in alunos if aluno.media < 7.0]
            
            mensagem_aprovacao = "\n\t---------- Aprovados --------- \n\n" + "\n".join([f'{nome} - Media: {media}' for nome, media in aprovados]) if aprovados else "\nNenhum aluno aprovado."
            mensagem_reprovacao = "\n\t---------- Reprovados --------- \n\n" + "\n".join([f'{nome} - Media: {media}' for nome, media in reprovados]) if reprovados else "\nNenhum aluno reprovado."

            mensagem_final = f"Resultados:\n{mensagem_aprovacao}\n{mensagem_reprovacao}"

            messagebox.showinfo("Resultados", mensagem_final)
            '''
            - aprovados = [(aluno.nome, aluno.media) for aluno in alunos if aluno.media >= 7.0]: Cria uma lista de tuplas contendo o nome e a média de alunos que têm uma média maior ou igual a 7.0.
            - reprovados = [(aluno.nome, aluno.media) for aluno in alunos if aluno.media < 7.0]: Cria uma lista de tuplas contendo o nome e a média de alunos que têm uma média menor que 7.0.
            - mensagem_aprovacao = ...: Cria uma string formatada que contém os nomes e médias dos alunos aprovados. A string inclui um título e usa a função join para formatar a lista de aprovados de uma maneira mais legível. 
                Se não houver alunos aprovados, a mensagem indicará "Nenhum aluno aprovado.".
            - mensagem_reprovacao = ...: Cria uma string formatada que contém os nomes e médias dos alunos reprovados. A string inclui um título e usa a função join para formatar a lista de reprovados de uma maneira mais legível. 
                Se não houver alunos reprovados, a mensagem indicará "Nenhum aluno reprovado.".
            - mensagem_final = f"Resultados:{mensagem_aprovacao}{mensagem_reprovacao}": Combina as mensagens de aprovação e reprovação em uma mensagem final.
            - messagebox.showinfo("Resultados", mensagem_final): Exibe uma caixa de diálogo informativa com o título "Resultados" e a mensagem final.
            '''
                      
        btn_salvar = ttk.Button(top_window, text="Salvar Notas",style='RoundedButton.TButton', command=salvar_notas)
        btn_salvar.grid(row=len(alunos) + 1, column=0, columnspan=3, pady=10)

    # Função para gerar notas aleatórias
    def gerar_notas_aleatorias():
        for aluno in alunos:
            nota_aleatoria = round(random.uniform(5.0, 10.0), 2)
            aluno.media = nota_aleatoria
            '''
            - for aluno in alunos: itera sobre cada aluno na lista alunos.
            - nota_aleatoria = round(random.uniform(5.0, 10.0), 2): Gera uma nota aleatória para o aluno utilizando a função random.uniform(5.0, 10.0), 
                que retorna um número decimal aleatório no intervalo de 5.0 a 10.0. O resultado é arredondado para duas casas decimais.
            - aluno.media = nota_aleatoria: Atribui a nota aleatória gerada à propriedade media do objeto aluno.
            '''
        
        def verificar_aprovacao():
            aprovados = [(aluno.nome,aluno.media) for aluno in alunos if aluno.media >= 7.0] 
            reprovados = [(aluno.nome,aluno.media) for aluno in alunos if aluno.media < 7.0]

            mensagem_aprovacao = "\n\t---------- Aprovados --------- \n\n" + "\n".join([f'{nome} - Media: {media}' for nome, media in aprovados]) if aprovados else "\nNenhum aluno aprovado."
            mensagem_reprovacao = "\n\t---------- Reprovados --------- \n\n" + "\n".join([f'{nome} - Media: {media}' for nome, media in reprovados]) if reprovados else "\nNenhum aluno reprovado."

            mensagem_final = f"Resultados:\n{mensagem_aprovacao}\n{mensagem_reprovacao}"

            messagebox.showinfo("Resultados", mensagem_final)
            
        mostrar_mensagem("Notas aleatórias geradas com sucesso!")
        verificar_aprovacao()
        
    def cmd1():
        janela.destroy()
        menu()
    
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))

    btn_adicionar = ttk.Button( janela, text="Adicionar Notas",style='RoundedButton.TButton', command=adicionar_notas)
    btn_adicionar.pack(pady=10)
    
    btn_gerar_aleatorias = ttk.Button(janela, text="Gerar Notas Aleatórias", style='RoundedButton.TButton', command=gerar_notas_aleatorias)
    btn_gerar_aleatorias.pack(pady=10)

    btn_sair = ttk.Button( janela, text="Voltar",style='RoundedButton.TButton', command=cmd1)
    btn_sair.pack(pady=10)
    
    janela.mainloop()
    
# Função para acessar o LinkedIn   
def linkedin():
    janela = tk.Tk()
    janela.title("LINKEDIN")
    janela.configure(background="#ADD8E6")
    
    proporcao = 6
    imagem_menor = PhotoImage(file='in.png')
    imagem_reduzida = imagem_menor.subsample(proporcao, proporcao)
    lbl = tk.Label(janela, image=imagem_reduzida, bg="#ADD8E6")
    lbl.pack(pady=10)
    
    # Cria um frame para conter a barra de rolagem e o conteúdo
    frame = ttk.Frame(janela, style='Frame.TFrame')  
    frame.pack(expand=True, fill="both", padx=50, pady=50)

    # Cria um canvas para permitir a rolagem
    canvas = tk.Canvas(frame, bg="#ADD8E6", highlightthickness=0)  
    canvas.pack(side="left", fill="both", expand=True)

    # Adiciona uma barra de rolagem à direita do canvas
    scrollbar = ttk.Scrollbar(frame, command=canvas.yview) 
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Cria um frame interno para armazenar o conteúdo
    inner_frame = ttk.Frame(canvas, style='Frame.TFrame')
    inner_frame_window = canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    
    # Função para mostra mensagem e abrir o link no navegador
    def open_link(link):
        mostrar_mensagem('Abrindo link externo')
        webbrowser.open(link)
    
    # Configuração de estilo para os botões e o frame
    style = ttk.Style()
    style.configure('RoundedButton.TButton', borderwidth=20, relief="flat", foreground="blue", background="#0000FF", font=('Helvetica', 10, 'bold'))
    style.configure('Frame.TFrame', background="#ADD8E6")

    def cmd1():
        janela.destroy()
        menu()

    # Popula o frame interno com botões para cada aluno e um botão para voltar
    def populate_inner_frame():
        for aluno, link in zip(alunos, links): # Loop que cria botões para cada aluno, associando a função open_link ao link correspondente. 
            btn = ttk.Button(inner_frame, text=aluno.nome, style='RoundedButton.TButton', command=lambda l=link: open_link(l))
            btn.pack(pady=5)

        btn_sair = ttk.Button(inner_frame, text="Voltar", style='RoundedButton.TButton', command=cmd1)
        btn_sair.pack(pady=10)

    populate_inner_frame() # Chama a função para preencher o frame interno com botões

     # Funções para ajustar a configuração do frame e do canvas quando a janela é redimensionada
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    def on_canvas_configure(event):
        canvas.itemconfig(inner_frame_window, width=canvas.winfo_width())

    # Associa os eventos de configuração às funções correspondentes
    inner_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    janela.mainloop()

if __name__ == "__main__": # Garante que o código dentro dele seja executado apenas quando o script é executado diretamente 
    menu() # Chama função principal