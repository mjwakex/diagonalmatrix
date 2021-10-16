import random 
#randint()
def create_matrix(N):
    global M
    M = [[0] * N for i in range(N)]
    for row in M:
        print(row)

def addingRandomValuesToMatrix():
    for i in range(len(M)):
        for j in range(len(M[i])):
          M[i][j] = random.randint(0,10)
    
        
        
    

create_matrix(6)
addingRandomValuesToMatrix()
