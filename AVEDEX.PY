import unicodedata

# ==========================================
# 1. FUNÇÕES DE UTILITÁRIOS E NORMALIZAÇÃO
# ==========================================

def normalizar_texto(texto):
    """
    Remove acentos, converte o texto para minúsculas e remove espaços extras.
    Isso permite buscar 'canário' digitando 'canario', por exemplo.
    """
    texto = str(texto)
    texto = texto.lower().strip()
    # Decompõe os caracteres acentuados (NFD separa a letra do acento)
    texto = unicodedata.normalize("NFD", texto)
    # Filtra mantendo apenas os caracteres que não são marcas de acentuação ('Mn')
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto


def exibir_linha():
    """Imprime uma linha divisória visual para organização da interface."""
    print("=" * 50)


def pausar():
    """Pausa a execução até o usuário pressionar ENTER, evitando que a tela limpe rapidamente."""
    input("\nPressione ENTER para voltar ao menu...")


# ==========================================
# 2. FUNÇÕES DE BUSCA E EXIBIÇÃO DE DADOS
# ==========================================

def buscar_aves(catalogo, termo_busca):
    """
    Percorre o catálogo e busca o termo digitado dentro de vários campos
    (nome popular, nome científico, família, ordem e tipo de dieta).
    """
    resultados = []
    termo = normalizar_texto(termo_busca)
    
    for ave in catalogo:
        # Reúne os campos selecionados para a busca
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]
        
        # Junta todos os campos em uma única string e normaliza
        texto_busca = normalizar_texto(" ".join(campos_busca))
        
        # Se o termo procurado estiver dentro do texto da ave, adiciona aos resultados
        if termo in texto_busca:
            resultados.append(ave)
            
    return resultados


def buscar_ave_por_codigo(catalogo, codigo_procurado):
    """Procura uma ave específica dentro de uma lista utilizando o seu ID/código."""
    for ave in catalogo:
        if str(ave["id"]) == str(codigo_procurado):
            return ave
    return None


def listar_aves(catalogo):
    """Exibe uma lista simplificada com o ID e o Nome Popular de todas as aves do catálogo."""
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def exibir_detalhes(ave):
    """Exibe na tela todas as informações detalhadas de uma única ave."""
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave['ordem']}")
    print(f"Família: {ave['familia']}")
    print(f"Dieta: {ave['dieta_tipo']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")


def exibir_resultados_busca(resultados):
    """Formata e imprime a lista de aves encontradas após realizar uma pesquisa."""
    print()
    exibir_linha()
    print("RESULTADOS DA BUSCA")
    exibir_linha()
    
    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


# ==========================================
# 3. INTERFACE E NAVEGAÇÃO DE TELAS
# ==========================================

def exibir_menu():
    """Exibe o menu principal com o cabeçalho e as opções atualizadas."""
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


def selecionar_ave_por_id(catalogo):
    """
    Função auxiliar para a Opção 3 do menu:
    Lista as aves disponíveis, pede o ID ao usuário e exibe os detalhes.
    """
    listar_aves(catalogo)
    codigo_escolhido = input("\nDigite o ID/código da ave para ver detalhes: ").strip()
    ave_encontrada = buscar_ave_por_codigo(catalogo, codigo_escolhido)
    
    if ave_encontrada is not None:
        exibir_detalhes(ave_encontrada)
    else:
        print("Ave não encontrada. Confira o código informado.")


def tela_busca(catalogo):
    """
    Gerencia a tela de pesquisa: pede o termo, faz a busca,
    exibe os resultados e permite abrir o detalhamento direto pelo ID.
    """
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()
    
    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return
        
    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)
    
    # Se houver resultados, oferece a opção de abrir os detalhes diretamente
    if len(resultados) > 0:
        escolha = input("\nDigite o ID para ver detalhes ou ENTER para voltar: ").strip()
        if escolha != "":
            ave_encontrada = buscar_ave_por_codigo(resultados, escolha)
            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes(ave_encontrada)


# ==========================================
# 4. BASE DE DADOS (CATÁLOGO EM MEMÓRIA)
# ==========================================

# Estrutura de dados contendo o banco de informações das aves (Lista de Dicionários)
catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "id": 4,
        "nome_popular": "Carcará",
        "nome_cientifico": "Caracara plancus",
        "ordem": "Falconiformes",
        "familia": "Falconidae",
        "dieta_tipo": "Onívora / Necrófaga",
        "habitat": "Campos, cerrados, caatinga e áreas rurais.",
        "alimentacao": "Animais vivos, carcaça, restos de lixo humano, insetos e frutos.",
        "curiosidade": "Alguns indivíduos da espécie podem nascer com plumagem leucística."
    },
    {
        "id": 5,
        "nome_popular": "Ararinha-azul",
        "nome_cientifico": "Cyanopsitta spixii",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Granívora",
        "habitat": "Caatinga seca, florestas ciliares abertas.",
        "alimentacao": "Frutos e sementes.",
        "curiosidade": "Infelizmente devido a destruição da Caatinga, atualmente a espécie é considerada extinta da natureza."
    }
]


# ==========================================
# 5. FLUXO PRINCIPAL DO PROGRAMA
# ==========================================

# Mensagem inicial ao abrir o programa
exibir_linha()
print("                    AVEDEX")
exibir_linha()

opcao_menu = ""

# Laço principal que mantém o menu ativo até que a opção "0" seja digitada
while opcao_menu != "0":
    exibir_menu() 
    opcao_menu = input("Escolha uma opção: ").strip()
    print()
    
    # Processa a opção informada pelo usuário
    if opcao_menu == "1":
        listar_aves(catalogo_aves)
        
    elif opcao_menu == "2":
        tela_busca(catalogo_aves)
        
    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)
        
    elif opcao_menu == "4":
        print("A AveDex é um catálogo interativo de aves.")
        print("Em breve, teremos comparação, imagens, sons e dados em arquivo JSON.")
        
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")
        
    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")
        
    # Se o usuário não escolheu sair, faz uma pausa antes de redesenhar o menu
    if opcao_menu != "0":
        pausar()