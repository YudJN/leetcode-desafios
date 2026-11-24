"""Testes locais para a solução do problema 104.

Como rodar (dentro desta pasta):
    python testes.py
"""
from collections import deque

from solution import Solution


class TreeNode(object):
    """Mesmo formato de nó que o LeetCode usa."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construir_arvore(valores):
    """Monta a árvore a partir da lista, nível por nível (formato do LeetCode).

    Exemplo: [3, 9, 20, None, None, 15, 7]
    Um None significa "aqui não existe nó" e não gera filhos.
    """
    if not valores or valores[0] is None:
        return None

    raiz = TreeNode(valores[0])
    fila = deque([raiz])
    i = 1
    while fila and i < len(valores):
        no = fila.popleft()

        if i < len(valores) and valores[i] is not None:
            no.left = TreeNode(valores[i])
            fila.append(no.left)
        i += 1

        if i < len(valores) and valores[i] is not None:
            no.right = TreeNode(valores[i])
            fila.append(no.right)
        i += 1

    return raiz


CASOS = [
    # (descrição, lista de entrada, resposta esperada)
    ("Exemplo 1 do enunciado", [3, 9, 20, None, None, 15, 7], 3),
    ("Exemplo 2 do enunciado", [1, None, 2], 2),
    ("Árvore vazia", [], 0),
    ("Só a raiz", [0], 1),
    ("Caminho só pela direita", [1, None, 2, None, 3, None, 4], 4),
    ("Lado esquerdo mais fundo", [1, 2, 3, 4, None, None, None, 5], 4),
]


def main():
    solucao = Solution()
    falhas = 0

    for descricao, entrada, esperado in CASOS:
        obtido = solucao.maxDepth(construir_arvore(entrada))
        ok = obtido == esperado
        falhas += 0 if ok else 1
        marca = "OK    " if ok else "FALHOU"
        print("[{}] {:<26} entrada={} esperado={} obtido={}".format(
            marca, descricao, entrada, esperado, obtido))

    print()
    if falhas:
        print("{} teste(s) falharam.".format(falhas))
        raise SystemExit(1)
    print("Todos os {} testes passaram.".format(len(CASOS)))


if __name__ == "__main__":
    main()
