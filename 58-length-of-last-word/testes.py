"""Testes locais para as duas soluções do problema 58.

Como rodar (dentro desta pasta):
    python testes.py
"""
import solucao_alternativa
import solution

CASOS = [
    # (entrada, resposta esperada)
    ("Hello World", 5),
    ("fly me to the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("a", 1),
    ("a ", 1),
    ("   a   ", 1),
]


def main():
    falhas = 0
    for nome, modulo in (("split", solution), ("de trás para a frente", solucao_alternativa)):
        solucao = modulo.Solution()
        for entrada, esperado in CASOS:
            obtido = solucao.lengthOfLastWord(entrada)
            ok = obtido == esperado
            falhas += 0 if ok else 1
            marca = "OK    " if ok else "FALHOU"
            print("[{}] {:<22} entrada={!r} esperado={} obtido={}".format(
                marca, nome, entrada, esperado, obtido))

    print()
    if falhas:
        print("{} teste(s) falharam.".format(falhas))
        raise SystemExit(1)
    print("Todos os {} testes passaram.".format(2 * len(CASOS)))


if __name__ == "__main__":
    main()
