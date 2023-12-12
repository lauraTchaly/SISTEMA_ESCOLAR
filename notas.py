import json
#screenlogger = programa detetive

#FUNÇÃO PRA CADASTRAR UM NOVO ALUNO 
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    #GERA MATRÍCULA DE FORMA AUTOMÁTICA
       #str = gera numeros legiveis para o usuario  / repr = gera informações criptografados
       # hash = serve para decodificar alguma coisa
       #[:5] = o limite de numeros a aparecer na tela
    matricula = str(abs(hash(cpf)))[:5]

    # VARIAVEL DICIONÁRIO
    aluno = {
        "nome" : nome,
        "CPF" : cpf,
        "Telefone" : telefone,
        "Endereço" : endereco
    } 
    # r = exibir  /  a = inserir e anexar informações no arquivo  / rw = alterar
    with open("alunos.json", "a") as file:
        # dumps = serve para converter um tipo especial(como dicionario) em string
        file.write(json.dumps({matricula : aluno}) + "\n")

    print(f"Aluno cadastrado com matricula: {matricula}.")

#FUNÇÃO PARA LISTAR TODOS OS ALUNOS CADASTRADOS
def listar_aluno():
    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            for matricula, aluno in dado.items():
                print(f"Matricula: {matricula}. Nome: {aluno['nome']}")

#FUNÇÃO PARA EDITAR UM ALUNO CADASTRADO
def editar_aluno():
    matricula = input("Digite a matricula do aluno a ser editado: ")
    with open ("alunos.json", "r") as file:
        #readlines = lê a quantidade de linhas
        linhas = file.readlines()
    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Nome telefone: ")
            novo_endereco = input("Novo endereço: ")

            #ATUALIZA AS INFORMAÇÕES DO ALUNO
            dado[matricula]["Nome"] = novo_nome
            dado[matricula]["Telefone"] = novo_telefone
            dado[matricula]["Endereco"] = novo_endereco

            linhas[i] = json.dumps(dado) + "\n"
            with open ("alunos.json", "w") as file:
                #WRITELINES = ESCREVE E EDITA HA LINHA
                file.writelines(linhas)
            print("Informações do aluno atualizadas.")
            return
    print("Matricula não encontrada.")

   
#FUNÇÃO PARA LANÇAR AS NOTAS DE UM ALUNO
def lancar_notas():
    # matricula = input("Digite a matricula do aluno a ser editado: ")
    # with open("alunos.json", "a") as file:
    #    prova1 = input("Nota da prova 1: ")
    #    prova2 = input("Nota da prova 2: ")
    #    trabalho = input("Nota do trabalho: ")
  
    #    notas = {
    #       "Prova 1" : prova1,
    #       "Prova 2" : prova2,
    #       "Trabalho" : trabalho
    #    }  
  
    #    file.write(json.dumps({matricula : notas }) + "\n")

    # print("Matricula não encontrada")

    matricula = input("Digite a matrícula do aluno para lançamento de nota: ")
    
    with open("alunos.json", "r") as file:
        linhas = file.readlines()

    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            prova1 = input("Nota da prova 1: ")
            prova2 = input("Nota da prova 2: ")
            trabalho = input("Nota do trabalho: ")

            dado[matricula]["Notas"] = {
                "Prova 1": prova1,
                "Prova 2": prova2,
                "Trabalho": trabalho
            }

            linhas[i] = json.dumps(dado) + "\n"
            with open("alunos.json", "w") as file:
                file.writelines(linhas)

            print("Notas do aluno atualizadas.")
            return

    print("Matrícula não encontrada.")
 
#FUNÇÃO PARA EXIBIR AS NOTAS DE UM ALUNO
def exibir_nota():
    matricula = input("Digite a matrícula do aluno a ser exibido: ")

    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            if matricula in dado:
                if "Notas" in dado[matricula]:
                    notas = dado[matricula]["Notas"]
                    print(f"Notas do aluno {dado[matricula]['nome']} : {notas}")
                    return

    print("Matrícula não encontrada.")

#FUNÇÃO PARA EDITAR AS NOTAS DE UM ALUNO
def editar_notas():
    matricula = input("Digite a matrícula do aluno para edição de nota: ")
    with open("alunos.json", "r") as file:
        linhas = file.readlines()
    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            if "Notas" in dado[matricula]:
                notas = dado[matricula]["Notas"]
                print(f"Notas atuais do aluno {dado[matricula]['nome']} : {notas}")

                nova_prova1 = input("Nova nota da prova 1: ")
                nova_prova2 = input("Nova nota da prova 2: ")
                novo_trabalho = input("Nova nota do trabalho: ")
                
                dado[matricula]["Notas"]["Prova 1"] = nova_prova1
                dado[matricula]["Notas"]["Prova 2"] = nova_prova2
                dado[matricula]["Notas"]["Trabalho"] = novo_trabalho

                linhas[i] = json.dumps(dado) + "\n"
                with open("alunos.json", "w") as file:
                    file.writelines(linhas)

                print("Notas do aluno atualizadas.")
                return

while True:

    print("1 - Cadastrar aluno")
    print("2 - Listar aluno")
    print("3 - Editar aluno")
    print("4 - Lançar notas")
    print("5 - Exibir nota")
    print("6 - Editar notas")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")


    if escolha == "1":
        cadastrar_aluno()
    elif escolha == "2":
        listar_aluno()
    elif escolha == "3":
        editar_aluno()
    elif escolha == "4":
        lancar_notas()
    elif escolha == "5":
        exibir_nota()
    elif escolha == "6":
        editar_notas()
    elif escolha == "0":
        break
    else:
        print("Opção inválida")

