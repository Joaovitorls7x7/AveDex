# AveDex
Catálogo interativo de aves desenvolvido para a disciplina de Boas Práticas de Programação.

O AveDex é um sistema em Python executado via linha de comando (CLI), projetado para catalogar, pesquisar, exibir detalhes biométricos e comparar informações ecológicas e taxonômicas de diversas espécies de aves.

## Funcionalidades do Sistema
- Menu de navegação contínuo (laço while) com tratamento para opções inválidas e encerramento seguro;
- Listagem geral e simplificada de todas as espécies cadastradas no catálogo;
- Sistema de busca inteligente por palavra-chave em múltiplos campos (nome popular, nome científico, família, ordem e dieta);
- Normalização de texto automática que ignora diferenças entre letras maiúsculas/minúsculas e acentuação durante as pesquisas;
- Exibição de ficha técnica completa com dados biométricos (comprimento e peso), habitat, dieta, curiosidades e índice de conservação;
- Tratamento de dados ausentes para evitar erros de exibição quando alguma informação biométrica não estiver preenchida;
- Tabela comparativa lado a lado entre duas aves para análise direta de atributos taxonômicos e ecológicos;
- Aviso em tela ao selecionar a mesma ave para ambos os lados na comparação;
- Validação de entradas do usuário para evitar travamentos ao digitar IDs inexistentes ou buscas em branco.

## Evolução e Arquitetura do Projeto
Nesta versão, a aplicação passou por um processo de refatoração focado em modularização e organização de dados. O catálogo foi estruturado utilizando listas de dicionários chave-valor, permitindo manipular as informações ecológicas de forma limpa, segura e escalável.

## Testes Manuais Realizados

### Módulo 1 — Navegação e Consulta Básica
- [x] Listagem geral de aves cadastradas
- [x] Consulta de detalhes por ID existente
- [x] Consulta por ID inexistente ou fora do catálogo
- [x] Tratamento de opção inválida no menu principal
- [x] Encerramento correto e seguro do programa

### Módulo 2 — Sistema de Busca e Normalização
- [x] Busca parcial por nome popular
- [x] Busca com tolerância à acentuação (ex: "canario" encontra "Canário-da-terra")
- [x] Filtro de busca por família taxonômica
- [x] Filtro de busca por ordem
- [x] Filtro de busca por tipo de dieta
- [x] Retorno amigável para consultas sem resultados
- [x] Validação e bloqueio de entradas de busca em branco
- [x] Tentativa de navegação por ID fora do escopo de resultados filtrados

### Módulo 3 — Comparação de Espécies
- [x] Comparação estruturada entre duas aves distintas
- [x] Exibição alinhada de família, dieta e habitat na tabela comparativa
- [x] Comparação direta de dados biométricos (peso em gramas e comprimento em cm)
- [x] Comparação de status e índice de conservação
- [x] Validação de ID inexistente durante o fluxo de seleção para comparação
- [x] Exibição de aviso para comparação de uma mesma ave com ela mesma
- [x] Tratamento de opção inválida durante o fluxo do menu

## Fontes dos Dados
- WikiAves (Carcará): https://www.wikiaves.com.br/wiki/carcara
- WikiAves (Ararinha-azul): https://www.wikiaves.com.br/wiki/ararinha-azul

## Como Executar
```bash
python avedex.py