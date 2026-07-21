import unicodedata

# ==========================================
# FUNÇÕES DE UTILITÁRIOS E NORMALIZAÇÃO
# ==========================================


def buscar_aves(catalogo, termo_busca):
    # Lista que receberá todas as aves encontradas.
    resultados = []
    
    # Normalizamos o termo digitado uma única vez.
    termo = normalizar_texto(termo_busca)
    
    # Percorremos todas as aves do catálogo.
    for ave in catalogo:
        # Separamos os campos em que a busca será feita.
        # Usamos get() para evitar erro caso alguma chave esteja ausente.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]
        
        # Juntamos todos os campos em um único texto.
        # Assim, a busca pode procurar em todos eles de uma vez.
        texto_busca = " ".join(campos_busca)
        
        # Normalizamos o texto completo da ave.
        texto_busca = normalizar_texto(texto_busca)
        
        # Se o termo digitado estiver no texto da ave,
        # adicionamos essa ave aos resultados.
        if termo in texto_busca:
            resultados.append(ave)
            
    return resultados


def normalizar_texto(texto):
    # Garante que o valor recebido será tratado como texto.
    texto = str(texto)
    # Converte para minúsculas e remove espaços no início e no final.
    texto = texto.lower().strip()
    # Separa as letras dos sinais de acentuação.
    # Exemplo: "á" passa a ser tratado como "a" + acento.
    texto = unicodedata.normalize("NFD", texto)
    # Monta um novo texto removendo os sinais de acentuação.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto


def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("                MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver detalhes de uma ave")
    print("4 - Buscar ave por nome")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def mostrar_curiosidade():
    print("Curiosidade:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# ==========================================
# FUNÇÕES DE BUSCA E LISTAGEM
# ==========================================

def buscar_aves_por_nome(catalogo, termo_busca):
    resultados = []
    # Normalizamos o termo digitado pelo usuário (remove acentos e deixa minúsculo).
    termo = normalizar_texto(termo_busca)
    
    for ave in catalogo:
        # Normalizamos também o nome cadastrado.
        nome = normalizar_texto(ave["nome_popular"])
        
        # O operador "in" verifica se o termo sem acento está dentro do nome sem acento.
        if termo in nome:
            resultados.append(ave)
            
    return resultados


def listar_aves(catalogo):
    print()
    exibir_linha()
    print("AVES CADASTRADAS")
    exibir_linha()
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_codigo(catalogo, codigo_procurado):
    for ave in catalogo:
        if str(ave["id"]) == str(codigo_procurado):
            return ave
    return None


def exibir_detalhes(ave):
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


# ==========================================
# BASE DE DADOS (CATÁLOGO)
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
# FLUXO PRINCIPAL DO PROGRAMA
# ==========================================

exibir_linha()
print("                    AVEDEX")
exibir_linha()

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu() 
    opcao_menu = input("Escolha uma opção: ").strip()
    print()
    
    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)
    
    elif opcao_menu == "2":
        listar_aves(catalogo_aves)
    
    elif opcao_menu == "3":
        listar_aves(catalogo_aves)
        codigo_escolhido = input("\nDigite o código da ave: ").strip()
        ave_encontrada = buscar_ave_por_codigo(
            catalogo_aves,
            codigo_escolhido
        )
        if ave_encontrada is not None:
            exibir_detalhes(ave_encontrada)
        else:
            print("Ave não encontrada. Confira o código informado.")

    elif opcao_menu == "4":
        termo = input("Digite o nome ou parte do nome da ave: ").strip()
        resultados = buscar_aves_por_nome(catalogo_aves, termo)
        
        if resultados:
            print(f"\n--- AVES ENCONTRADAS ({len(resultados)}) ---")
            for ave in resultados:
                print(f"ID {ave['id']} - {ave['nome_popular']} ({ave['nome_cientifico']})")
        else:
            print(f"\nNenhuma ave encontrada com o termo '{termo}'.")

    elif opcao_menu == "5":
        mostrar_sobre()
    
    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")
    
    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3, 4 ou 5.")
        
    if opcao_menu != "0":
        pausar()