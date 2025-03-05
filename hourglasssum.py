def hourglassSum(arr):
    hourglasses = []
    sum = 0

    for i in range(4):
        for j in range(4):
            
            sum = sum + arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum = sum + arr[i+1][j+1]
            sum = sum + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            hourglasses.append(sum)
            sum = 0
    
    return max(hourglasses)
        







matrix = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print (hourglassSum(matrix))