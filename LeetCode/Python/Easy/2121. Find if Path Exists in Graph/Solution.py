
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = [source]
        visited = [False] * n
        visited[source] = True

        while len(q) > 0:
            a = q.pop(0)

            if a == destination:
                return True

            for neighbour in graph[a]:
                if visited[neighbour] == False:
                    q.append(neighbour)
                    visited[neighbour] = True

        return False
