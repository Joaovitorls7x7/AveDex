# 🐦 AveDex

> Catálogo interativo de aves desenvolvido para a disciplina de **Boas Práticas de Programação**.

O **AveDex** é um sistema desenvolvido em **Python** e executado via **linha de comando (CLI)**. O projeto foi desenvolvido com o objetivo de catalogar, pesquisar, visualizar detalhes e comparar informações biométricas, ecológicas e taxonômicas de diferentes espécies de aves.

---

## 📋 Funcionalidades do Sistema

* Menu de navegação contínuo utilizando laço `while`;
* Tratamento de opções inválidas;
* Encerramento seguro do programa;
* Listagem geral e simplificada das espécies cadastradas;
* Sistema de busca inteligente por palavra-chave;
* Busca em múltiplos campos:

  * Nome popular;
  * Nome científico;
  * Família;
  * Ordem;
  * Dieta;
* Normalização automática de texto, ignorando:

  * Diferenças entre letras maiúsculas e minúsculas;
  * Acentuação;
* Exibição de ficha técnica completa;
* Informações biométricas, como:

  * Comprimento;
  * Peso;
* Informações sobre:

  * Habitat;
  * Dieta;
  * Curiosidades;
  * Índice de conservação;
* Tratamento de dados ausentes para evitar erros durante a exibição;
* Tabela comparativa entre duas aves;
* Comparação de atributos taxonômicos, ecológicos e biométricos;
* Aviso ao selecionar a mesma ave para os dois lados da comparação;
* Validação de entradas do usuário;
* Tratamento de IDs inexistentes;
* Bloqueio de buscas em branco.

---

## 🏗️ Evolução e Arquitetura do Projeto

Nesta versão, a aplicação passou por um processo de **refatoração**, com foco em modularização, organização do código e estruturação dos dados.

O catálogo utiliza estruturas baseadas em **listas de dicionários chave-valor**, permitindo organizar e manipular as informações das espécies de forma limpa, segura e escalável.

A separação das funcionalidades em diferentes módulos facilita a manutenção do projeto e permite sua expansão futura.

---

# 🧪 Testes Manuais Realizados

## Módulo 1 — Navegação e Consulta Básica

* [x] Listagem geral de aves cadastradas
* [x] Consulta de detalhes por ID existente
* [x] Consulta por ID inexistente ou fora do catálogo
* [x] Tratamento de opção inválida no menu principal
* [x] Encerramento correto e seguro do programa

---

## Módulo 2 — Sistema de Busca e Normalização

* [x] Busca parcial por nome popular
* [x] Busca com tolerância à acentuação
* [x] Exemplo: `"canario"` encontra `"Canário-da-terra"`
* [x] Filtro de busca por família taxonômica
* [x] Filtro de busca por ordem
* [x] Filtro de busca por tipo de dieta
* [x] Retorno amigável para consultas sem resultados
* [x] Validação e bloqueio de entradas de busca em branco
* [x] Tentativa de navegação por ID fora do escopo de resultados filtrados

---

## Módulo 3 — Comparação de Espécies

* [x] Comparação estruturada entre duas aves distintas
* [x] Exibição alinhada de família, dieta e habitat na tabela comparativa
* [x] Comparação direta de dados biométricos
* [x] Comparação de peso em gramas
* [x] Comparação de comprimento em centímetros
* [x] Comparação de status e índice de conservação
* [x] Validação de ID inexistente durante o fluxo de seleção
* [x] Exibição de aviso ao comparar uma ave com ela mesma
* [x] Tratamento de opção inválida durante o fluxo do menu

---

# 🔄 Testes de Regressão

Os testes de regressão devem ser realizados após alterações no código para verificar se as funcionalidades existentes continuam funcionando corretamente.

* [X] Listar aves
* [X] Buscar por parte do nome
* [X] Buscar por família
* [X] Buscar por ordem
* [X] Buscar por dieta
* [X] Ver detalhes por ID
* [X] Comparar duas aves
* [X] Tratar ID inexistente
* [X] Tratar opção inválida no menu
* [X] Encerrar o programa

---

# 📚 Fontes dos Dados

As informações utilizadas no catálogo foram consultadas no **WikiAves**:

* [WikiAves — Carcará](https://www.wikiaves.com.br/wiki/carcara)
* [WikiAves — Ararinha-azul](https://www.wikiaves.com.br/wiki/ararinha-azul)
* [WikiAves — Tucano-toco](https://www.wikiaves.com.br/wiki/tucano-toco)
* [WikiAves — Uirapuru-verdadeiro](https://www.wikiaves.com.br/wiki/uirapuru-verdadeiro)

---

# ▶️ Como Executar

Para executar o AveDex, é necessário possuir o **Python** instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

O programa será iniciado através da interface de linha de comando (CLI).

---

# 👨‍💻 Autor

**João Vitor Lima Soares**

Projeto desenvolvido para a disciplina de **Boas Práticas de Programação**.
