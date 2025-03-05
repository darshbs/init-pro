# https://practice.geeksforgeeks.org/contest/job-a-thon-40-hiring-challenge/problems

def solveTheExpression(a, b, k):
    subSet = [0] * k

    largeOfA = max(a)
    sumofB = 0
    for i in b:
        sumofB += i
    
    print(sumofB)
    
    sumofB = sum(b)
    print(sumofB)





a = [3, 7, 6]
b = [9, 2, 4]
k = 2

print(solveTheExpression(a,b,k))