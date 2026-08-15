# Testes manuais da AveDex

## Execução
- [x] O projeto executa com `python main.py`.
- [x] O menu principal aparece corretamente.
- [x] A opção 0 encerra o programa.

## Catálogo
- [x] A opção 1 lista as aves.
- [x] A opção 2 busca por parte do nome.
- [x] A opção 2 busca por família.
- [x] A opção 2 busca por ordem.
- [x] A opção 2 busca por dieta.
- [x] A opção 3 mostra detalhes por ID.
- [x] O programa trata ID inexistente.
- [x] O programa trata letras no lugar do ID.

## Comparação
- [x] A opção 4 compara duas aves existentes.
- [x] A comparação mostra família, dieta, peso e comprimento.
- [x] A comparação trata ID inexistente.

## Dados e ambiente
- [x] O JSON é carregado corretamente.
- [x] O programa identifica JSON ausente.
- [x] O programa identifica JSON mal formatado.
- [x] O programa identifica campo obrigatório ausente.
- [x] O programa identifica ID duplicado.
- [x] A opção 6 verifica o ambiente.

# Testes manuais da AveDex

## Funcionalidades principais
- [x] O programa abre com `python main.py`.
- [x] O dataset JSON é carregado e validado.
- [x] A listagem possui paginação e seleção por ID.
- [x] A busca ignora diferenças de maiúsculas e acentos.
- [x] Os detalhes mostram dados completos e mídias cadastradas.
- [x] A comparação mostra duas aves lado a lado.
- [x] A ave aleatória é sorteada e exibida.
- [x] A batalha permite escolher duas aves e um atributo.
- [x] A mesma ave não pode batalhar contra ela própria.

## Imagem, som e cache
- [x] Ave sem `imagem_url` mostra aviso e não encerra o programa.
- [x] Ave sem `som_url` mostra aviso e não encerra o programa.
- [x] A primeira execução baixa a mídia disponível.
- [x] A segunda execução reaproveita o arquivo em `cache_midias/`.
- [x] Sem `term-image`, o caminho da imagem salva é informado.
- [x] Sem `pygame`, o caminho do som salvo é informado.
- [x] Falha de conexão mostra mensagem clara.

## Interface e ambiente
- [x] O menu aparece em caixa visual.
- [x] Títulos, avisos, erros e sucessos estão padronizados.
- [x] A verificação do ambiente informa as dependências instaladas.
- [x] A opção de créditos continua disponível.
- [x] A opção `0` encerra corretamente.