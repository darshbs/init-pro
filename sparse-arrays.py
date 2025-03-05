# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

def matchingStrings(stringList, queries):
    new_list = []
    for i in queries:
        if i in stringList:
            new_list.append(stringList.count(i))
        elif i not in stringList:
            new_list.append(stringList.count(i))
    return new_list




n_list = ['aba', 'baba', 'aba', 'xzxb']
q_list = ['aba', 'xzxb', 'ab']

print(matchingStrings(n_list, q_list))

