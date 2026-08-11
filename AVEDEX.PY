import unicodedata

# ==========================================
# 1. FUNÇÕES DE UTILITÁRIOS E NORMALIZAÇÃO
# ==========================================

def normalizar_texto(texto):
    """
    Remove acentos, converte o texto para minúsculas e remove espaços extras.
    Permite buscar 'canário' digitando 'canario', por exemplo.
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


def valor_ou_indisponivel(valor, unidade=""):
    """Formatador de valores numéricos para exibição com unidade de medida ou 'Não informado'."""
    if valor is None or valor == "":
        return "Não informado"
    
    if unidade != "":
        return f"{valor} {unidade}"
    
    return str(valor)


# ==========================================
# 2. FUNÇÕES DE BUSCA E LISTAGEM DE DADOS
# ==========================================

def buscar_aves(catalogo, termo_busca):
    """
    Percorre o catálogo e busca o termo digitado dentro de vários campos
    (nome popular, nome científico, família, ordem e tipo de dieta).
    """
    resultados = []
    termo = normalizar_texto(termo_busca)
    
    for ave in catalogo:
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]
        
        texto_busca = normalizar_texto(" ".join(campos_busca))
        
        if termo in texto_busca:
            resultados.append(ave)
            
    return resultados


def buscar_ave_por_codigo(catalogo, codigo_procurado):
    """Procura uma ave específica dentro do catálogo utilizando o seu ID/código."""
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


# ==========================================
# 3. FUNÇÕES DE EXIBIÇÃO E COMPARAÇÃO
# ==========================================

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


def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    """Imprime uma linha formatada para alinhar os dados lado a lado como em uma tabela."""
    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")


def exibir_comparacao_aves(ave_1, ave_2):
    """Gera uma tabela visual comparando todos os atributos de duas aves selecionadas."""
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)
    
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )
    print("-" * 78)
    
    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )
    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )
    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )
    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )
    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )
    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(ave_1.get("comprimento_cm"), "cm"),
        valor_ou_indisponivel(ave_2.get("comprimento_cm"), "cm")
    )
    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(ave_1.get("peso_g"), "g"),
        valor_ou_indisponivel(ave_2.get("peso_g"), "g")
    )
    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get("status_conservacao", "Não informado"),
        ave_2.get("status_conservacao", "Não informado")
    )
    imprimir_linha_comparacao(
        "Índice",
        ave_1.get("indice_conservacao", "Não informado"),
        ave_2.get("indice_conservacao", "Não informado")
    )


def escolher_ave(catalogo, mensagem):
    """Exibe o catálogo e solicita um ID ao usuário, retornando o dicionário da ave."""
    listar_aves(catalogo)
    id_escolhido = input(f"\n{mensagem}: ").strip()
    
    # Corrigido de buscar_ave_por_id para buscar_ave_por_codigo
    ave_encontrada = buscar_ave_por_codigo(catalogo, id_escolhido)
    
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None
        
    return ave_encontrada


def comparar_duas_aves(catalogo):
    """Orquestra a seleção de duas aves e invoca a tela de comparação."""
    print()
    print("Escolha a primeira ave")
    ave_1 = escolher_ave(catalogo, "Digite o ID da primeira ave")
    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")
    ave_2 = escolher_ave(catalogo, "Digite o ID da segunda ave")
    if ave_2 is None:
        return

    exibir_comparacao_aves(ave_1, ave_2)


# ==========================================
# 4. INTERFACE E NAVEGAÇÃO DE TELAS
# ==========================================

def exibir_menu():
    """Exibe o menu principal com todas as opções ativas."""
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


def selecionar_ave_por_id(catalogo):
    """Opção 3 do menu: Solicita um ID e exibe a ficha completa da ave."""
    listar_aves(catalogo)
    codigo_escolhido = input("\nDigite o ID/código da ave para ver detalhes: ").strip()
    ave_encontrada = buscar_ave_por_codigo(catalogo, codigo_escolhido)
    
    if ave_encontrada is not None:
        exibir_detalhes(ave_encontrada)
    else:
        print("Ave não encontrada. Confira o código informado.")


def tela_busca(catalogo):
    """Gerencia a busca por palavras-chave e navegação para detalhes."""
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()
    
    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return
        
    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)
    
    if len(resultados) > 0:
        escolha = input("\nDigite o ID para ver detalhes ou ENTER para voltar: ").strip()
        if escolha != "":
            ave_encontrada = buscar_ave_por_codigo(resultados, escolha)
            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes(ave_encontrada)


# ==========================================
# 5. BASE DE DADOS (CATÁLOGO EM MEMÓRIA)
# ==========================================

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
# 6. FLUXO PRINCIPAL DO PROGRAMA
# ==========================================

if __name__ == "__main__":
    exibir_linha()
    print("                    AVEDEX")
    exibir_linha()

    opcao_menu = ""

    while opcao_menu != "0":
        exibir_menu() 
        opcao_menu = input("Escolha uma opção: ").strip()
        print()
        
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
            print("Desenvolvido para consulta taxonômica e comparação de espécies.")
            
        elif opcao_menu == "0":
            print("Encerrando a AveDex. Até logo!")
            
        else:
            print("Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5.")
            
        if opcao_menu != "0":
            pausar()