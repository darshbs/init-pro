# https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true

def rotateLeft(d, arr):
    new_arr = []
    temp = arr[d:]
    print(temp)
    new_arr = temp + arr[:d]
    return new_arr


res1 = rotateLeft(4,[1,2,3,4,5])
result = rotateLeft(10,[41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51])
print(res1)
print(result)