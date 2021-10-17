import random 
#randint()
def create_matrix():
    global N
    global M
    N = int(input("Enter value of N: "))
    M = [[0] * N for i in range(N)]

def addingRandomValuesToMatrix():
    for i in range(len(M)):
        for j in range(len(M[i])):
          M[i][j] = random.randint(0,9)
    for row in M:
        print(row)

def declaringMainDiagonal():
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

def decalringSubDiagonal():
    global sub_diag
    end = False
    sub_diag = []
    r, c = 1, 0
    while not end:
        if r > (N-1):
            end = True
        else:
            sub_diag.append(M[r][c])
            r += 1 ; c += 1
    print(sub_diag)

def decalringSupDiagonal():
    global sub_diag
    end = False
    sup_diag = []
    r, c = 0, 1
    while not end:
        if r > (N-2):
            end = True
        else:
            sup_diag.append(M[r][c])
            r += 1 ; c += 1
    print(sup_diag)
        
def checkForZerosSup():
    #need to check all the values above sup diagonal to see if all zeros
    #start with [1][2] and check if [0][2] == 0, IF not, Reutrn False
    end = False
    is_zero = True
    r, c = 1, 2
    while not end:
        if c > (N-1):
            end = True
        else:
            if (M[r-1][c]) != 0:
                is_zero = False
                return False
                break
            else:
                is_zero = True
            r += 1 ; c += 1
    if is_zero == True:
        return True

def checkForZerosSup():
    #need to check all the values above sup diagonal to see if all zeros
    #start with [1][2] and check if [0][2] == 0, IF not, Reutrn False
    end = False
    is_zero = True
    r, c = 1, 2
    while not end:
        if c > (N-1):
            end = True
        else:
            if (M[r-1][c]) != 0:
                is_zero = False
                return False
                break
            else:
                is_zero = True
            r += 1 ; c += 1
    if is_zero == True:
        return True

"""""
def checkForZerosSub():
    end = False
    is_zero = True
    r, c = 1, 0
    while not end:
        if c > (N-1):
            end = True
        else:
            if (M[r-1][c]) != 0:
                is_zero = False
                return False
                break
            else:
                is_zero = True
            r += 1 ; c += 1
    if is_zero == True:
        return True
"""""

    

create_matrix()
addingRandomValuesToMatrix()
print()
declaringMainDiagonal()
decalringSubDiagonal()
decalringSupDiagonal()
print()
print(checkForZerosSup())