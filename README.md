# AveDex
Catálogo interativo de aves desenvolvido na disciplina de Boas Práticas de Programação.
## Funcionalidades
- listagem e paginação;
- busca textual sem diferenciar acentos ou maiúsculas;
- detalhes por ID;
- comparação entre duas aves;
- ave aleatória;
- Batalha AveDex;
- download e cache de imagens e sons;
- tentativa de exibição de imagens no terminal;
- reprodução de sons;
- validação defensiva do dataset;
- verificação do ambiente;
- créditos e fontes.
## Como executar
```bash
pip install -r requirements.txt
python main.py
```
Os recursos centrais funcionam sem as bibliotecas opcionais. Imagem, som e download dependem das bibliotecas de `requirements.txt`.
## Estrutura
- `main.py`: ponto de entrada;
- `src/avedex/app.py`: fluxo principal;
- `src/avedex/catalogo.py`: listagem, busca, detalhes e ave aleatória;
- `src/avedex/comparacao.py`: comparação;
- `src/avedex/batalha.py`: batalha por atributos;
- `src/avedex/multimidia.py`: download, cache, imagem e som;
- `src/avedex/interface.py`: abertura e menu;
- `src/avedex/dados.py`: carregamento e validação do JSON;
- `src/avedex/ambiente.py`: verificação das dependências;
- `src/avedex/creditos.py`: créditos e fontes;
- `src/avedex/utils.py`: funções auxiliares;
- `data/avedex_dataset_midias.json`: dados das aves;
- `cache_midias/`: mídias baixadas, criada automaticamente;
- `docs/testes_manuais.md`: roteiro de testes.