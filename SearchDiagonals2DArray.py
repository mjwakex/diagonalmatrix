import random 
#randint()
def create_matrix(N):
    global M
    M = [[0] * N for i in range(N)]

def addingRandomValuesToMatrix():
    for i in range(len(M)):
        for j in range(len(M[i])):
          M[i][j] = random.randint(0,9)
    for row in M:
        print(row)

def declaringMainDiagonal():
    diagonal = [M[i][1] for i in range(len(M))]
    print(diagonal)
    
        
        
    

create_matrix(6)
addingRandomValuesToMatrix()
print()
declaringMainDiagonal()
