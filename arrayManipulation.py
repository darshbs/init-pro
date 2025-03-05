# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true

def arrayManipulation(n, queries):
    newArray = []
    for i in range(n):
        newArray.append(0)
    

    for row in queries:
        for i in range( row[0]-1, row[1]):
            newArray[i] += row[2]
    return max(newArray)


n = 5
queries = [[1, 2, 100], 
           [2, 5, 100], 
           [3, 4, 100]]

print(arrayManipulation(n,queries))