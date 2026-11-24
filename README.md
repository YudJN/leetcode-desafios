# Desafios de Programação

Meu caderno de estudos de programação, feito a partir de problemas do [LeetCode](https://leetcode.com/). A ideia é retomar os fundamentos resolvendo um problema por vez e **documentando o raciocínio**, não só o código final.

![Linguagem](https://img.shields.io/badge/linguagem-Python-3776AB?logo=python&logoColor=white)
![Foco](https://img.shields.io/badge/foco-fundamentos-informational)

## Desafios resolvidos

| # | Problema | Dificuldade | Tema | Solução |
|---|---|---|---|---|
| 58 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Fácil | Strings | [ver pasta](58-length-of-last-word/) · [PDF](58-length-of-last-word/explicacao.pdf) |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Fácil | Árvores, recursão | [ver pasta](104-maximum-depth-of-binary-tree/) · [PDF](104-maximum-depth-of-binary-tree/explicacao.pdf) |

## Como cada pasta é organizada

```
NNN-nome-do-problema/
├── README.md       # o problema, a lógica e os aprendizados
├── img/            # diagramas usados no README e no PDF
├── solution.py     # a solução, no formato aceito pelo LeetCode
├── testes.py       # testes para rodar localmente
└── explicacao.pdf  # a explicação completa, passo a passo
```

## Como rodar os testes

Entre na pasta do desafio e rode:

```bash
python testes.py
```

Não precisa instalar nada além do Python 3.

## Método de estudo

1. Entender o enunciado com as próprias palavras (o que entra, o que sai).
2. Resolver os exemplos **à mão**, antes de escrever código.
3. Descobrir a regra geral e testá-la em casos pequenos.
4. Só então escrever o código, e depois registrar as armadilhas encontradas.
