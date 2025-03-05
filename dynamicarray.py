def dynamicArray(n, queries):
    lastAnswer = 0
    result = []
    seq = [[] for _ in range(n)]
    for i in queries:
        t, x, y = i
        index = (x ^ lastAnswer) % n  

        if t == 1:
            seq[index].append(y)
        elif t == 2:
            lastAnswer = seq[index][y % len(seq[index])]
            result.append(lastAnswer)
    return result



queries = [[1,0,5], [1, 1 ,7], [1, 0, 3], [2, 1, 0], [2, 1 ,1]]
n = 2
result = dynamicArray(n,queries)
print(result)