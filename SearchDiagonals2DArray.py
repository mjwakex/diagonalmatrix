import random 
#randint()
def create_matrix(N):
    global M
    M = [[0] * N for i in range(N)]
    for row in M:
        print(row)

def addingRandomValuesToMatrix():
    row, col = 0,0
    for row in M:
        for col in M:
            M[row][col] = random.randint(0,10)
        row += 1 ; col += 1
        print(row)
    

create_matrix(6)
addingRandomValuesToMatrix()