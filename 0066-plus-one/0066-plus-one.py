class Solution:
    """
    Define um método chamado 'plusOne', dentro da classe 'Solution'.
    O método possui 2 parâmetros.
    O parâmetro 'self' faz referência ao objeto da classe.
    O parâmetro 'digits' do tipo 'List[int]' (uma lista de inteiros),   
    retorna uma lista de inteiros.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry

            if sum < 10:
                digits[i] = sum
                carry = 0
                break
            else:
                digits[i] = 0

        if carry == 1:
            digits.insert(0, 1)
    
        return digits


        