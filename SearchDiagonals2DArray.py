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
    #Start with [r][c] and search [r-1][c] AND [r-2][c] -- > So IF r = 4 , search : FOR i in range (1,5) -- > [r-i][c]
    end = False
    is_zero = True
    r, c = 1, 2
    while not end:
        if c > (N-1):
            end = True
        else:
            for i in range(1,r+1):
                print(M[r-i][c])
                if M[r-i][c] != 0:
                    is_zero = False
            r += 1 ; c += 1
    return is_zero


def checkForZerosSub():
    #need to check all the values below sub diagonal to see if all zeros
    #Start with [r][c] and search [r+1][c] AND [r+2][c], etc -- > So IF r = 4 , search : FOR i in range (1,N-r) -- > [r+i][c]
    end = False
    is_zero = True
    r, c = 1, 0
    while not end:
        if c > (N-1):
            end = True
        else:
            for i in range(1,N-r):
                print(M[r+i][c])
                if M[r+i][c] != 0:
                    is_zero = False
            r += 1 ; c += 1
    return is_zero



               



create_matrix()
addingRandomValuesToMatrix()
print()
print(checkForZerosSup())
print(checkForZerosSub())