# 58. Length of Last Word (Comprimento da Última Palavra)
# https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split() sem argumentos separa por qualquer quantidade de espaços
        # e ignora os espaços do começo e do fim.
        lista = s.split()

        # lista[-1] é a última palavra; devolvo (return) o tamanho dela.
        return len(lista[-1])
