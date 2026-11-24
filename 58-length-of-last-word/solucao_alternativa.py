# 58. Length of Last Word - solução alternativa, sem criar lista.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1

        # 1) pula os espaços do final
        while s[i] == ' ':
            i -= 1

        # 2) conta as letras da última palavra
        tamanho = 0
        while i >= 0 and s[i] != ' ':
            tamanho += 1
            i -= 1

        return tamanho
