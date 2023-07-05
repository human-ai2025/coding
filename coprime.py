import sys
from os import path

FILE = True # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()


############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def coprime(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
    return gcd

def logic(inpList):
    answer = -1
    for i in range(len(inpList)):
        for j in range(len(inpList)):
            if coprime(inpList[i], inpList[j]) == 1:
                answer = max(i + j + 2, answer)
    return answer
            

def main():
    # first line has the number of test cases 
    # even lines has the nmber of integres 
    # odd lines has the corresponding elements 
    test_cases = inp()
    final_result = []
    for _ in range(test_cases):
        notWorth = inp()
        final_result.append(logic(inlt()))
    for item in final_result:
        sys.stdout.write(str(item))
        sys.stdout.write('\n')


if __name__ == "__main__":
    main()
    