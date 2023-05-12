class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Cria um dicionário vazio p/ mapear valores aos seus números na lista "nums"."
        dict = {}

        # Inicia um loop for que itera sobre os índices na posição 0 até o tam. da lista "nums"
        for i in range(len(nums)):
            # Verifica se a diferença entre o valor alvo e o valor atual não está presente em "dict""
            if target - nums[i] not in dict:
                # Add uma entrada em dict, onde a chave é o valor atual e o índice é o índice atual
                dict[nums[i]] = i
            else:
                """
                Retorna uma lista contendo os índices e o valor mapeado no dicionário "dict".
                Em que a diferença é usada como chave 'target-nums[i]'
                """
                return([i, dict[target-nums[i]]])


