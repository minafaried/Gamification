import random
import copy
from _winapi import INFINITE

board=[
    [1,-1,0],
    [-1,0,1],
    [0,1,-1]]
def initialInput():
    x=int(input("num Of Steps :"))
    y= int(input("Goal :"))
    zx = int(input("current position x :"))
    zy = int(input("current position y :"))
    return (x,y,[zx,zy])
def printbord(board, c):
    for i in range (0,3):
        for j in range (0,3):
            if c[0]==i and c[1]==j:
                print(end="*")
                print(board[i][j], end="")
                print(end="* ")
            else:
                print(board[i][j], end=" ")
        print("\n")
    print("----------------")
def getposiblemoves(c):
    if c==[0,0]:
        return [[0,1],[1,0]]
    elif c==[0,1]:
        return [[0,0],[0,2],[1,1]]
    elif c==[0,2]:
        return [[0,1],[1,2]]
    elif c==[1,0]:
        return [[0,0],[2,0],[1,1]]
    elif c==[1,1]:
        return [[0,1],[1,0],[1,2],[2,1]]
    elif c==[1,2]:
        return [[2,2],[0,2],[1,1]]
    elif c==[2,0]:
        return [[1,0],[2,1]]
    elif c==[2,1]:
        return [[2,0],[1,1],[2,2]]
    elif c==[2,2]:
        return [[1,2],[2,1]]

def alphabetetree(alpha, beta, depth, board, previous, current, player):
    if depth==0 :
        return board[current[0]][current[1]]
    if player:
        posiblemoves=getposiblemoves(current)
        resvalue=-INFINITE
        for i in range (0,len(posiblemoves)):
            b = copy.deepcopy(board)
            b[posiblemoves[i][0]][posiblemoves[i][1]]+=board[current[0]][current[1]]
            value=alphabetetree(alpha, beta, depth - 1, b, current, posiblemoves[i], False)
            resvalue=max(value,resvalue)
            alpha = max(value,alpha)
            if beta <= alpha:
                break
        return resvalue
    else:
        resvalue=INFINITE
        for i in range (-1,2):
            b = copy.deepcopy(board)
            b[previous[0]][previous[1]]=i
            value= alphabetetree(alpha, beta, depth, b, previous, current, True)
            resvalue = min(value, resvalue)
            beta = min(value, beta)
            if beta <= alpha:
                break
        return resvalue

def player(board, current, alpha, beta, depth, goal):
    posiblemoves = getposiblemoves(current)
    pos = posiblemoves[0]
    resvalue = -INFINITE
    score=board[current[0]][current[1]]
    if goal-score<depth:
        for j in range (goal-score-1,depth):
            for i in range(len(posiblemoves)):
                b = copy.deepcopy(board)
                b[posiblemoves[i][0]][posiblemoves[i][1]] += board[current[0]][current[1]]
                value= alphabetetree(alpha, beta, j, b, current, posiblemoves[i], False)
                if value>resvalue:
                    pos=posiblemoves[i]
                    resvalue=value
                if value>alpha:
                    alpha=value
                if beta <= alpha:
                    break
                if value==goal-score:
                    return pos
    else:
        for i in range(len(posiblemoves)):
            b = copy.deepcopy(board)
            b[posiblemoves[i][0]][posiblemoves[i][1]] += board[current[0]][current[1]]
            value = alphabetetree(alpha, beta, depth - 1, b, current, posiblemoves[i], False)
            if value > resvalue:
                pos = posiblemoves[i]
                resvalue = value
            if value > alpha:
                alpha = value
            if beta <= alpha:
                break
    return pos

def computer(board, prevous, current, alpha, beta, depth):
     pos = -1
     resvalue = INFINITE
     for i in range(-1,2):
         b = copy.deepcopy(board)
         b[current[0]][current[1]] =i
         value= alphabetetree(alpha, beta, depth,b, prevous, current, True)
         if value<resvalue:
             pos=i
             resvalue=value
         if value<beta:
             beta=value
         if beta <= alpha:
             break
     return pos

def computer():
    return random.randint(-1,1)


#print(minimum(bord,[2,0] ,[2,1], -INFINITE, +INFINITE, 3, 3))


def play(board):
    n,g,c=initialInput()
    printbord(board, c)
    for i in range(n,0,-1):
        tempbord= copy.deepcopy(board)
        tempc=copy.deepcopy(c)
        tempg=copy.deepcopy(g)
        maxres=player(tempbord, tempc, -INFINITE, +INFINITE, i, tempg)
        board[maxres[0]][maxres[1]]+= board[c[0]][c[1]]
        print("user")
        print("next move:", maxres," score:", board[maxres[0]][maxres[1]])
        printbord(board, maxres)
        """
        tempbord= copy.deepcopy(board)
        tempc=copy.deepcopy(maxres)
        tempg=copy.deepcopy(g)
        tempmin=computer(tempbord,c,tempc, -INFINITE, +INFINITE,i)
        """
        tempmin=computer()
        board[c[0]][c[1]] = tempmin
        print("computer put :",tempmin)
        printbord(board, c)
        c=maxres
        if board[c[0]][c[1]] == g:
            print("the score is :", board[c[0]][c[1]])
            print("win")
            return True
    else:
        print("the score is :", board[c[0]][c[1]])
        print("lose")
        return False

play(board)