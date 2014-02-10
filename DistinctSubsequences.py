class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        array = [[0 for i in range(len(S)+1)] for j in range(len(T)+1)]
        for j in range(len(T),-1,-1):
            array[j][-1] = 0
        for i in range(len(S),-1,-1):
            array[-1][i] = 1

        for i in range(len(S)-1,-1,-1):
            for j in range(len(T)-1,-1,-1):
                if i+1 <= len(S):
                    array[j][i] = array[j][i+1]
                if S[i] == T[j] and i+1 <= len(S) and j+1 <= len(T):
                    array[j][i] += array[j+1][i+1]
        return array[0][0]
