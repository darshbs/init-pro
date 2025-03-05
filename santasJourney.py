# https://practice.geeksforgeeks.org/contest/job-a-thon-40-hiring-challenge/problems


from collections import deque, defaultdict

class Solution:
    def calculatePresentsCount(self, n, m, trails, journeyPlan):
        # Step 1: Create adjacency list representation of graph
        graph = defaultdict(list)
        for u, v in trails:
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph
        print(graph)
        # Step 2: Initialize an array to count presents received at each city
        presents = [0] * (n + 1)  # 1-based indexing

        # Step 3: Find paths for each journey and update presents count
        def bfs(start, end):
            """Finds the shortest path between start and end using BFS"""
            queue = deque([(start, [start])])  # Store (node, path_taken)
            visited = set()

            while queue:
                node, path = queue.popleft()
                if node == end:
                    return path  # Return the path found

                if node in visited:
                    continue
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

            return []  # No path found (shouldn't happen)

        for start, end in journeyPlan:
            path = bfs(start, end)  # Get the path from start to end
            for city in path:
                presents[city] += 1

        return presents[1:]  # Remove the extra 0th index for 1-based indexing

# Example Test Case
n = 5
m = 3
trails = [[1, 2], [1, 3], [3, 4], [3, 5]]
journeyPlan = [[1, 3], [2, 5], [1, 4]]

obj = Solution()
res = obj.calculatePresentsCount(n, m, trails, journeyPlan)
print(res)  # Output expected: Number of presents received by each city
