class Solution:
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        # https://leetcode.com/problems/is-graph-bipartite/discuss/491010/python-dfs-solution
        # dfs to mark the color
        colored = {}

        def dfs(i, color):
            if i in colored:
                return colored[i] == color
            colored[i] = color
            for nxt in graph[i]:
                if not dfs(nxt, color * (-1)):
                    return False
            return True

        # check every edge in graph if the node has not been visited previously
        for ii, g in enumerate(graph):
            if g and ii not in colored:
                if not dfs(ii, 1):
                    return False

        return True


# 2 BFS ans 2 DFS:
# https://leetcode.com/problems/is-graph-bipartite/discuss/480343/Python-2-DFS-%2B-2-BFS
