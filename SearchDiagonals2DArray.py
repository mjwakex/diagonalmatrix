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

def declaringMainDiagonal(N):
    #need to initilize while loop and array
    #start at [0][0] and append to new array
    #then go [1][1], [2][2], etc...
    #until [N-1][N-1] is reached
    
    end = False
    main_diag = []
    r, c = 0, 0
    while not end:
        if r > (N-1):
            end = True
        else:
            main_diag.append(M[r][c])
            r += 1 ; c += 1
    print(main_diag)

    
        
        
    

create_matrix(6)
addingRandomValuesToMatrix()
print()
declaringMainDiagonal(6)
