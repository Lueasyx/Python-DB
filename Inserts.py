import mysql.connector

#Cadastrar aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    telefone = input("Digite o nome do aluno: ")
    cpf_aluno = input("Digite o nome do aluno: ")

    cursor = conexao.cursor()

    sql = "INSERT INTO aluno (nome) VALUES (%s)"
    valores = (nome, email,telefone,cpf_aluno)
    cursor.execute(sql, valores)
    conexao.commit()
    print("aluno cadastrada com sucesso!")
    cursor.close()

#Listar aluno
def listar_aluno():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos ORDER BY id")
    alunos = cursor.fetchall()
    if not alunos:
        print("Não existem alunos cadastradas!")
    else:
        for aluno in alunos:
            print(f"cpf_aluno: {aluno[0]}, Nome: {aluno[1]}")

#Cadastrar curso
def cadastrar_curso():
    nome = input("Digite o nome do curso: ")

    print("Escolha qual aluno deseja vincular o curso: ")
    listar_aluno()

    cpf_aluno = input("ID da aluno escolhida: ")

    #verificar se o ID da aluno escolhida é válido
    cursor = conexao.cursor()
    sql = "SELECT id FROM alunos WHERE id = %s"
    valores = (cpf_aluno,)
    cursor.execute(sql, valores)
    aluno = cursor.fetchone()

    if aluno is None:
        print("ID de aluno inválido")
        return

    #Inserir um novo registro na tabela
    cursor = conexao.cursor()
    sql = "INSERT INTO cursos (nome, cpf_aluno) VALUES (%s, %s)"
    valores = (nome, cpf_aluno)
    cursor.execute(sql, valores)
    conexao.commit()
    print("curso cadastrado com sucesso!")

#Listar cursos
def listar_cursos():
    cursor = conexao.cursor()
    cursor.execute("SELECT cursos.id, cursos.nome, alunos.nome FROM cursos INNER JOIN alunos on cursos.cpf_aluno = alunos.id ORDER BY cursos.id")
    cursos = cursor.fetchall()

    if not cursos:
        print("Não há cursos cadastrados.")
    else:
        for curso in cursos:
            print(f"ID: {curso[0]}, Nome: {curso[1]}, aluno: {curso[2]}")

#Cadastrar professor
def cadastrar_professor():
    nome = input("Digite o nome do professor: ")
    email = input("Digite o email do professor: ")
    telefone = input("Digite o nome do professor: ")
    id_professor = input("Digite o nome do aluno: ")

    cursor = conexao.cursor()
    sql = "INSERT INTO professor (nome, email, telefone, id_professor) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, telefone, id_professor)
    cursor.execute(sql, valores)
    conexao.commit()
    print("professor cadastrada com sucesso!")

#Listar aluno
def listar_professor():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM professor ORDER BY id")
    alunos = cursor.fetchall()
    if not professor:
        print("Não existem alunos cadastradas!")
    else:
         for professor in professor:
            print(f"id_professor: {professor[0]}, Nome: {professor[1]}")

# Cria uma conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa"
    )
    cursor = conexao.cursor()
except:
    print("Erro ao conectar com o banco de dados")
    exit()

while True:
    print("\nEscolha uma opção: ")
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar curso")
    print("3 - Listar alunos")
    print("4 - Listar curso")
    print("0 - Sair")

    opcao = input("Opção escolhida: ")
    
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        cadastrar_curso()
    elif opcao == "3":
        cadastrar_professor()
    elif opcao == "4":
        listar_aluno()
    elif opcao == "5":
        listar_cursos()
    elif opcao == "6":
        listar_professor()
    elif opcao == "0":
        break