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
    matricula = str(hash(cpf))

    aluno = {
        "nome" : nome,
        "CPF" : cpf,
        "Telefone" : telefone,
        "Endereço" : endereco
    } 
    # r = exibir e alterar  /  a = inserir e anexar informações no arquivo
    with open("alunos.json", "a") as file:
        file.write(json.dumps({matricula : aluno}) + "\n")

    print(f"Aluno cadastrado com matricula: {matricula}.")

#FUNÇÃO PARA LISTAR TODOS OS ALUNOS CADASTRADOS
def listar_aluno():
    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            for matricula, aluno in dado.items():
                print(f"Matricula: {matricula}. Nome: {aluno[nome]}")

#FUNÇÃO PARA EDITAR UM ALUNO CADASTRADO
def editar_aluno():
    matricula = input("Digite a matricula do aluno a ser editado: ")
    with open ("aluno.json", "r") as file:
        #readlines = lê a quantidade de linhas
        linhas = file.readlines()
   
#FUNÇÃO PARA LANÇAR AS NOTAS DE UM ALUNO
def lancar_notas():

#FUNÇÃO PARA EXIBIR AS NOTAS DE UM ALUNO
def exibir_aluno():

#FUNÇÃO PARA EDITAR AS NOTAS DE UM ALUNO
def editar_notas():

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar aluno")
    print("3 - Editar aluno")
    print("4 - Lançar notas")
    print("5 - Exibir aluno")
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
        exibir_aluno()
    elif escolha == "6":
        editar_notas()
    elif escolha == "0":
        break
    else:
        print("Opção inválida")
