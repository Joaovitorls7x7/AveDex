import unicodedata  # Biblioteca padrão usada para manipular e remover acentos de textos

# ==========================================
# FUNÇÕES UTILITÁRIAS E DE TRATAMENTO DE TEXTO
# ==========================================

def normalizar_texto(texto):
    """
    Remove acentos, converte para minúsculas e remove espaços extras das pontas.
    Isso garante que buscas por palavras com acento (ex: 'Canário') funcionem 
    mesmo que o usuário digite sem acento ('canario').
    """
    # Garante que o valor recebido seja convertido para string (texto)
    texto = str(texto)
    # Converte todas as letras para minúsculas e remove espaços desnecessários nas extremidades
    texto = texto.lower().strip()
    # Decompõe os caracteres acentuados em caractere base + acento separado (Normal Form D)
    texto = unicodedata.normalize("NFD", texto)
    # Filtra e reconstrói o texto mantendo apenas caracteres que NÃO sejam marcas de acentuação ('Mn')
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto


def pausar():
    """
    Pausa a execução do programa para que o usuário consiga ler o conteúdo retornado 
    antes que o menu principal seja exibido novamente.
    """
    input("\nPressione ENTER para voltar ao menu...")


def valor_ou_indisponivel(valor, unidade=""):
    """
    Verifica se um determinado dado numérico ou texto está preenchido.
    Se estiver vazio/ausente, retorna 'Não informado'.
    Se existir, formata o valor junto com sua unidade de medida (ex: '23 cm').
    """
    # Verifica se o valor é nulo (None) ou uma string vazia
    if valor is None or valor == "":
        return "Não informado"
        
    # Caso uma unidade tenha sido fornecida (ex: 'cm' ou 'g'), concatena ao valor
    if unidade != "":
        return f"{valor} {unidade}"
        
    # Retorna o próprio valor convertido para string caso não haja unidade especificada
    return str(valor)


# ==========================================
# FUNÇÕES DE INTERFACE E EXIBIÇÃO DE MENUS
# ==========================================

def exibir_menu():
    """
    Imprime na tela o cabeçalho estilizado e a lista numerada com todas as opções do sistema.
    """
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    """
    Percorre todo o catálogo fornecido e exibe apenas o ID numérico 
    e o Nome Popular de cada ave cadastrada.
    """
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)
    # Espera uma lista de dicionários e itera sobre cada ave
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


# ==========================================
# FUNÇÕES DE BUSCA E CONSULTA NO CATÁLOGO
# ==========================================

def buscar_ave_por_id(catalogo, id_procurado):
    """
    Procura uma ave específica no catálogo através de seu ID único.
    Retorna o dicionário completo da ave se encontrada, ou None caso não exista.
    """
    for ave in catalogo:
        # Converte o ID cadastrado para string para comparar com a entrada do usuário de forma segura
        if str(ave["id"]) == id_procurado:
            return ave  # Retorna o dicionário contendo todos os dados da ave
            
    # Caso percorra todo o catálogo e não encontre o ID solicitado
    return None


def buscar_aves(catalogo, termo_busca):
    """
    Busca por palavra-chave dentro do catálogo.
    Pesquisa no Nome Popular, Nome Científico, Família, Ordem e Dieta da ave,
    ignorando diferenças entre maiúsculas/minúsculas e acentuações.
    """
    resultados = []  # Inicializa a lista que armazenará as aves correspondentes
    termo = normalizar_texto(termo_busca)  # Limpa e normaliza o texto digitado pelo usuário
    
    for ave in catalogo:
        # Cria uma lista temporária contendo as informações chave da ave atual
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]
        
        # Junta todos os campos em um único texto para facilitar a busca
        texto_busca = " ".join(campos_busca)
        texto_busca = normalizar_texto(texto_busca)
        
        # Verifica se o termo digitado está contido dentro das informações da ave
        if termo in texto_busca:
            resultados.append(ave)  # Adiciona a ave à lista de resultados
            
    return resultados  # Retorna a lista completa com as aves encontradas


# ==========================================
# FUNÇÕES DE EXIBIÇÃO DE DETALHES E BUSCA
# ==========================================

def exibir_detalhes_ave(ave):
    """
    Recebe um único dicionário de ave e imprime de forma organizada 
    todas as suas propriedades (biometria, taxonomia, curiosidades, etc).
    """
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    # O método .get() evita erros no programa caso alguma chave não esteja cadastrada
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    # Formata comprimento e peso utilizando a função auxiliar para tratar valores zerados ou nulos
    print(f"Comprimento: {valor_ou_indisponivel(ave.get('comprimento_cm'), 'cm')}")
    print(f"Peso: {valor_ou_indisponivel(ave.get('peso_g'), 'g')}")
    print(f"Conservação: {ave.get('status_conservacao', 'Não informada')}")
    print(f"Índice de conservação: {ave.get('indice_conservacao', 'Não informado')}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    """
    Opção 3 do Menu: Exibe a lista de aves, solicita ao usuário um ID
    e busca o registro para exibir a ficha de detalhes da ave escolhida.
    """
    listar_aves(catalogo)  # Mostra as aves disponíveis
    id_escolhido = input("\nDigite o ID da ave: ").strip()
    
    # Chama a função de busca utilizando o ID digitado
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)
    
    # Valida se a ave foi localizada ou não
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def exibir_resultados_busca(resultados):
    """
    Formata e exibe no console o resultado simplificado obtido pela pesquisa de termo.
    """
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)
    
    # Valida se a busca retornou uma lista vazia
    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        # Exibe cada ave correspondente no formato: ID - Nome (Família, Dieta)
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    """
    Opção 2 do Menu: Gerencia o fluxo de pesquisa, permitindo que o usuário digite 
    uma palavra-chave e, caso deseje, selecione um ID para abrir a ficha completa.
    """
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()
    
    # Impede pesquisas em branco
    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return
        
    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)
    
    # Caso a busca encontre aves, dá a opção do usuário abrir os detalhes de uma delas
    if len(resultados) > 0:
        escolha = input("\nDigite o ID para ver detalhes ou ENTER para voltar: ").strip()
        if escolha != "":
            # Busca a ave dentro apenas do subset retornado no resultado
            ave_encontrada = buscar_ave_por_id(resultados, escolha)
            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)


# ==========================================
# FUNÇÕES DE COMPARAÇÃO DE AVES
# ==========================================

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    """
    Auxiliar da tabela comparativa: Formata três colunas alinhadas 
    (Rótulo do campo | Valor da Ave 1 | Valor da Ave 2).
    """
    # Usa especificadores de largura de campo (<18, <25) para deixar a tabela reta e bonita
    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")


def exibir_comparacao_aves(ave_1, ave_2):
    """
    Monta e imprime uma tabela lado a lado comparando as características das duas aves selecionadas.
    """
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)
    # Cabeçalho da Tabela
    imprimir_linha_comparacao("Campo", ave_1["nome_popular"], ave_2["nome_popular"])
    print("-" * 78)
    # Linhas de Atributos
    imprimir_linha_comparacao("Nome científico", ave_1.get("nome_cientifico"), ave_2.get("nome_cientifico"))
    imprimir_linha_comparacao("Ordem", ave_1.get("ordem"), ave_2.get("ordem"))
    imprimir_linha_comparacao("Família", ave_1.get("familia"), ave_2.get("familia"))
    imprimir_linha_comparacao("Dieta", ave_1.get("dieta_tipo"), ave_2.get("dieta_tipo"))
    imprimir_linha_comparacao("Habitat", ave_1.get("habitat"), ave_2.get("habitat"))
    imprimir_linha_comparacao("Comprimento", valor_ou_indisponivel(ave_1.get("comprimento_cm"), "cm"), valor_ou_indisponivel(ave_2.get("comprimento_cm"), "cm"))
    imprimir_linha_comparacao("Peso", valor_ou_indisponivel(ave_1.get("peso_g"), "g"), valor_ou_indisponivel(ave_2.get("peso_g"), "g"))
    imprimir_linha_comparacao("Conservação", ave_1.get("status_conservacao", "Não informado"), ave_2.get("status_conservacao", "Não informado"))
    imprimir_linha_comparacao("Índice", ave_1.get("indice_conservacao", "Não informado"), ave_2.get("indice_conservacao", "Não informado"))


def escolher_ave(catalogo, mensagem):
    """
    Auxiliar do processo de comparação: Exibe o catálogo e pede ao usuário que digite 
    o ID de uma ave, retornando o objeto correspondente.
    """
    listar_aves(catalogo)
    id_escolhido = input(f"\n{mensagem}: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)
    
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None
        
    return ave_encontrada


def comparar_duas_aves(catalogo):
    """
    Opção 4 do Menu: Gerencia a escolha de duas aves distintas para compará-las.
    """
    # Seleciona e valida a primeira ave
    print()
    print("Escolha a primeira ave")
    ave_1 = escolher_ave(catalogo, "Digite o ID da primeira ave")
    if ave_1 is None:
        return  # Cancela a operação se a ave não for encontrada
        
    # Seleciona e valida a segunda ave
    print()
    print("Escolha a segunda ave")
    ave_2 = escolher_ave(catalogo, "Digite o ID da segunda ave")
    if ave_2 is None:
        return  # Cancela a operação se a ave não for encontrada
        
    # Imprime a tabela de comparação final
    exibir_comparacao_aves(ave_1, ave_2)


# ==========================================
# BASE DE DADOS (CATÁLOGO DE AVES EM MEMÓRIA)
# ==========================================

# Lista composta por dicionários. Cada dicionário representa os atributos de uma ave.
catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 56,
        "peso_g": 830,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 57,
        "peso_g": 300,
        "status_conservacao": "Extinta na natureza",
        "indice_conservacao": 5,
        "alimentacao": "Frutos e sementes.",
        "curiosidade": "Infelizmente devido a destruição da Caatinga, atualmente a espécie é considerada extinta da natureza."
    }
]


# ==========================================
# LAÇO PRINCIPAL DE EXECUÇÃO DO PROGRAMA
# ==========================================

opcao_menu = ""

# O laço continuará sendo executado repetidamente até que a opção '0' seja digitada pelo usuário
while opcao_menu != "0":
    exibir_menu()  # Mostra as opções disponíveis
    opcao_menu = input("Escolha uma opção: ").strip()  # Captura e limpa a entrada do usuário
    
    # Redireciona a execução com base na escolha do usuário
    if opcao_menu == "1":
        listar_aves(catalogo_aves)
    elif opcao_menu == "2":
        tela_busca(catalogo_aves)
    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)
    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)
    elif opcao_menu == "5":
        print("A AveDex é um catálogo interativo de aves.")
        print("Em breve, teremos batalha, imagens, sons e dados em arquivo JSON.")
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")
    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5.")
        
    # Pausa a tela caso a opção escolhida não seja o encerramento do sistema
    if opcao_menu != "0":
        pausar()