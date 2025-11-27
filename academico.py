import datetime # Apenas para pegar a data atual no certificado

# --- BANCO DE DADOS NA MEMÓRIA
cursos = []
disciplinas = []
professores = []
alunos = []
notas = [] 

# aqui é a area referente a função de cadastro

def cadastrar_curso():
    print("\n--- Cadastro de Curso ---")
    codigo = input("Código do curso: ")
    nome = input("Nome do curso: ")
    # Salva como um dicionário dentro da lista
    cursos.append({'codigo': codigo, 'nome': nome})
    print("Curso cadastrado com sucesso!")

def cadastrar_disciplina():
    print("\n--- Cadastro de Disciplina ---")
    codigo = input("Código da disciplina: ")
    nome = input("Nome da disciplina: ")
    disciplinas.append({'codigo': codigo, 'nome': nome})
    print("Disciplina cadastrada com sucesso!")

def cadastrar_professor():
    print("\n--- Cadastro de Professor ---")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    disciplina = input("Disciplina que leciona: ")
    curso = input("Curso vinculado: ")
    professores.append({
        'matricula': matricula, 
        'nome': nome, 
        'disciplina': disciplina, 
        'curso': curso
    })
    print("Professor cadastrado!")

def cadastrar_aluno():
    print("\n--- Cadastro de Aluno ---")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    curso = input("Código do Curso do aluno: ")
    alunos.append({'matricula': matricula, 'nome': nome, 'curso': curso})
    print("Aluno cadastrado!")

def cadastrar_nota():
    print("\n--- Lançamento de Notas ---")
    mat_aluno = input("Matrícula do aluno: ")
    cod_disc = input("Código da disciplina: ")
    valor = float(input("Nota (0 a 10): "))
    
    # aqui é onde verifica se ja tem uma nota existente no sistema e se ja existir, ele atualiza ela
    nota_existente = False
    for n in notas:
        if n['matricula_aluno'] == mat_aluno and n['cod_disciplina'] == cod_disc:
            n['valor'] = valor
            nota_existente = True
            break
            
    if not nota_existente:
        notas.append({'matricula_aluno': mat_aluno, 'cod_disciplina': cod_disc, 'valor': valor})
        
    print("Nota registrada!")

# area de calculo

def calcular_media_aluno(matricula):
    soma = 0
    contador = 0
    for n in notas:
        if n['matricula_aluno'] == matricula:
            soma += n['valor']
            contador += 1
    
    if contador == 0:
        return 0
    return soma / contador

def verificar_situacao_aluno():
    print("\n--- Verificar Situação do Aluno ---") 
    matricula = input("Digite a matrícula do aluno: ")
    
    # Achar o nome do aluno apenas para exibir bonitinho
    nome_aluno = ""
    for a in alunos:
        if a['matricula'] == matricula:
            nome_aluno = a['nome']
            break
            
    if nome_aluno == "":
        print("Aluno não encontrado.")
        return

    media = calcular_media_aluno(matricula)
    print(f"Aluno: {nome_aluno} | Média Geral: {media:.2f}")

    # Verificar situação conforme a média
    if media >= 7:
        print("SITUAÇÃO: APROVADO (Média >= 7)")
        verificar_certificado(matricula, nome_aluno)
        
    elif media < 4:
        print("SITUAÇÃO: REPROVADO NO CURSO (Média < 4)")
        
    else: 
        print("SITUAÇÃO: RECUPERAÇÃO (4 <= Média < 7)")
        print("O aluno precisa alterar notas baixas.")
        
        # Listar disciplinas com nota baixa
        for n in notas:
            if n['matricula_aluno'] == matricula and n['valor'] < 7:
                print(f"Disciplina {n['cod_disciplina']} com nota {n['valor']}")
                opcao = input("Deseja alterar esta nota? (s/n): ")
                if opcao.lower() == 's':
                    nova_nota = float(input("Nova nota: "))
                    n['valor'] = nova_nota
                    print("Nota alterada.")
                    # Recalcula a média para ver se agora passou
                    nova_media = calcular_media_aluno(matricula)
                    print(f"Nova média: {nova_media:.2f}")
                    if nova_media >= 7:
                        print("O aluno agora está APROVADO!")
                        break

def verificar_certificado(matricula, nome_aluno): # lembrando que so sera emitido o certificado se o aluno tiver sido aprovado em pelo menos 10 disciplinas
    
    disciplinas_aprovadas = 0
    
    # é necessario ter registrado pelo menos 10 disciplinas para emitir o certificado (e ter passado nelas ne)
    count_disciplinas = 0
    for n in notas:
        if n['matricula_aluno'] == matricula:
            count_disciplinas += 1
            
    if count_disciplinas >= 10:
        curso_aluno = ""
        for a in alunos:
            if a['matricula'] == matricula:
                curso_aluno = a['curso']
        
        data_hoje = datetime.date.today()
        print("\n" + "="*40)
        print("       CERTIFICADO DE CONCLUSÃO")
        print("="*40)
        print(f"Certificamos que {nome_aluno}")
        print(f"Concluiu o curso de {curso_aluno}")
        print(f"Data de emissão: {data_hoje}")
        print("="*40 + "\n")
    else:
        print(f"Aviso: Aluno aprovado por média, mas cursou apenas {count_disciplinas} disciplinas (Mínimo 10 para certificado).")

# area dos relatiorios

def relatorio_geral():
    print("\n--- Relatório Geral ---")
    print(f"Total Alunos: {len(alunos)}")
    print(f"Total Professores: {len(professores)}")
    print(f"Total Cursos: {len(cursos)}")
    print(f"Total Disciplinas: {len(disciplinas)}")
    
    print("\nLista de Alunos:")
    for a in alunos: print(f"- {a['nome']} ({a['matricula']})")

def relatorio_por_curso_disciplina():
    print("\n--- Alunos por Curso ---")
    for c in cursos:
        print(f"Curso: {c['nome']}") # para o professor: ficar so declarando "i", não iria acabar bem (eu acho)
        for a in alunos:
            if a['curso'] == c['codigo']:
                print(f"   -> Aluno: {a['nome']}")

def boletim_detalhado():
    print("\n--- Boletim Detalhado ---")
    for a in alunos:
        print(f"\nALUNO: {a['nome']} | CURSO: {a['curso']}")
        print("Notas:")
        for n in notas:
            if n['matricula_aluno'] == a['matricula']:
                # Tenta achar nome da disciplina pelo código
                nome_disc = n['cod_disciplina']
                for d in disciplinas:
                    if d['codigo'] == n['cod_disciplina']:
                        nome_disc = d['nome']
                print(f"   - {nome_disc}: {n['valor']}")

# Me desculpe, mas eu não manjo de fazer interfaces graficas com python ainda não

def menu():
    while True:
        print("\n=== SISTEMA ACADÊMICO ===")
        print("1. Cadastrar Curso")
        print("2. Cadastrar Disciplina")
        print("3. Cadastrar Professor")
        print("4. Cadastrar Aluno")
        print("5. Lançar/Alterar Notas")
        print("6. Verificar Situação do Aluno (Aprovação/Recuperação)")
        print("7. Relatório Geral")
        print("8. Relatório Alunos por Curso")
        print("9. Boletim de Notas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar_curso()
        elif opcao == '2': cadastrar_disciplina()
        elif opcao == '3': cadastrar_professor()
        elif opcao == '4': cadastrar_aluno()
        elif opcao == '5': cadastrar_nota()
        elif opcao == '6': verificar_situacao_aluno()
        elif opcao == '7': relatorio_geral()
        elif opcao == '8': relatorio_por_curso_disciplina()
        elif opcao == '9': boletim_detalhado()
        elif opcao == '0': 
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# O inicio e tambem o fim (meio ironico ne)
menu()