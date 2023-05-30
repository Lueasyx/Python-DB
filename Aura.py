import mysql.connector

def cria_estrutura(sql, conexao, tabela):
    try:
        conexao.execute(sql)
        print("Tabela", tabela, "criada com sucesso")
    except mysql.connector.Error as err:
        print("Erro ao criar tabela:", tabela)
        print("Mensagem de erro:", err)
        exit()

# Cria uma conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa"
    )
except mysql.connector.Error as err:
    print("Erro ao conectar com o banco de dados")
    print("Mensagem de erro:", err)
    exit()

cursor = conexao.cursor()

def cria_estrutura(sql, conexao, tabela):
    try:
        conexao.execute(sql)
        print("Tabela", tabela, "criada com sucesso")
    except mysql.connector.Error as err:
        print("Erro ao criar tabela:", tabela)
        print("Mensagem de erro:", err)
        exit()

# Cria uma conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa"
    )
except mysql.connector.Error as err:
    print("Erro ao conectar com o banco de dados")
    print("Mensagem de erro:", err)
    exit()

cursor = conexao.cursor()

# Cria a tabela Aluno
cria_estrutura("CREATE TABLE aluno (cpf_aluno INT(11) NOT NULL UNIQUE, nome VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, telefone INT(20) NOT NULL, id_pagamento INT NOT NULL, PRIMARY KEY (cpf_aluno), FOREIGN KEY (id_pagamento) REFERENCES pagamento(id_pagamento))", cursor,"ALUNO")

cria_estrutura("CREATE TABLE cursos (id_curso INT NOT NULL UNIQUE AUTO_INCREMENT,nome VARCHAR(50) NOT NULL,id_professor INT NOT NULL, PRIMARY KEY (id_curso),FOREIGN KEY (id_professor) REFERENCES professor(id_professor))", cursor, "CURSOS")

cria_estrutura("CREATE TABLE cursos_has_alunos (id_curso INT NOT NULL UNIQUE AUTO_INCREMENT, cpf_aluno INT(11) NOT NULL UNIQUE, empresa_id INT NOT NULL, PRIMARY KEY (id_curso), PRIMARY KEY (cpf_aluno))", cursor, "CURSO_HAS_CURSOS")

cria_estrutura("CREATE TABLE professor (id_professor INT NOT NULL AUTO_INCREMENT,nome VARCHAR(50) NOT NULL, email VARCHAR(50),telefone VARCHAR(19)PRIMARY KEY (id_professor))", cursor, "PROFESSOR")

cria_estrutura("CREATE TABLE pagamento (id_pagamento INT NOT NULL AUTO_INCREMENT, forma_pagamento VARCHAR(50) NOT NULL, valor_assinatura FLOAT NOT NULL, PRIMARY KEY (id_pagamento))", cursor, "PAGAMENTO")