#6405203 Shothibutr Tansiri

def LCS(word1,word2):
    #create a 2D array to store the length of the longest common subsequence
    m=len(word1)+1 #row
    n=len(word2)+1 #col
    #first create 0 matrix with m*n dimension
    matrix = [([0]*n) for i in range(m)]
    for i in range(m):
        for j in range(n):  # noqa: F821
            if i==0 or j==0:
                matrix[i][j]=0
            else:
                if word1[i-1]==word2[j-1]:
                    matrix[i][j]=max(max(matrix[i-1]),max(matrix[i]))+1
                else:
                    matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    #trace of LCS
    for i in matrix:
        print(i) 
    return matrix[m-1][n-1]

print(LCS("abcdef", "acdfeg"))
print(LCS("suffix","simple"))
