number=int(input())
alpha = str(input(''))
i = 0

beta = list(alpha)
z = len(beta)


while z > 0:
    if beta[i] == "a":
        beta[i] = 1

    if beta[i] == 'b':
        beta[i] = 2

    if beta[i] == 'c':
        beta[i] = 3

    if beta[i] == "d":
        beta[i] = 4

    if beta[i] == 'e':
        beta[i] = 5

    if beta [i] == 'f':
         beta[i] = 6 

    if beta[i] == 'g':
        beta[i] = 7

    if beta[i] == 'h':
        beta[i] = 8
    
    if beta[i] == 'i':
        beta[i] = 9

    if beta[i] == 'j':
        beta[i] = 10
    
    if beta[i] == 'k':
        beta[i] = 11
    
    if beta[i] == 'l':
        beta[i] = 12
    
    if beta[i] == 'm':
        beta[i] = 13

    if beta[i] == 'n':
        beta[i] = 14

    if beta[i] == 'o':
        beta[i] = 15

    if beta[i] == 'p':
        beta[i] = 16

    if beta[i] == 'q':
        beta[i] = 17

    if beta[i] == 'r':
        beta[i] = 18
    
    if beta[i] == 's':
        beta[i] = 19

    if beta[i] == 't':
        beta[i] = 20

    if beta[i] == 'u':
        beta[i] = 21
    
    if beta[i] == 'v':
        beta[i] = 22

    if beta[i] == 'w':
        beta[i] = 23
    
    if beta[i] == 'x':
        beta[i] = 24
    
    if beta[i] == 'y':
        beta[i] = 25
    
    if beta[i] == 'z':
        beta[i] = 26


    i= i + 1
    z = z - 1

print(sum(beta))