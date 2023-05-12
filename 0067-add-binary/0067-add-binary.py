class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >=0:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0
            # Calcula a soma dos 2 números atuais, juntamente com valor transportado da adição anterior.
            curr_sum = num1 + num2 + carry
            '''
            O resto da divisão de curr_sum por 2 é convertido em uma string usando a função str(). 
            Em seguida, o dígito binário atual é concatenado com a esquerda do result
            '''
            result = str(curr_sum % 2) + result
            # Realiza a divisão inteira de curr_sum por 2, arredondando o resultado para baixo para o número inteiro mais próximo.
            carry = curr_sum // 2
            '''
            Decrementa os índices 'i' e 'j', para pecorrer os próximos caracteres das strings 'a' e 'b', 
            até chegar ao inicio de ambas as strings
            '''
            i -= 1
            j -= 1
        #  Adiciona um dígito adicional ao resultado, caso haja um transporte (carry) restante após a soma dos dígitos binários.
        if carry:
            result = '1' + result

        return result
     

        