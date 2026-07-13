import heapq

with open("problem0081_data.txt", "r", encoding="utf-8") as file:
    matrix = file.read()

a = [[int(x) for x in y.split(",")] for y in matrix.split("\n")]

M = len(a)

# class Graph:
#     def __init__(self):
#         self.adj_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list:
#             self.adj_list[vertex] = {}
        
#     def add_edge(self, src, dest, weight):
#         self.add_vertex(src)
#         self.add_vertex(dest)

#         src_list = self.adj_list[src]
#         src_list[dest] = weight

# def dijkstra(graph, start):

#     distances = {node: float('inf') for node in graph}
#     distances[start] = start

#     pred = {node: None for node in graph}

#     priority_queue = [(0, start)]

#     while priority_queue:
#         dist, curr = heapq.heappop(priority_queue)

#         if dist > distances[curr]:
#             continue

#         for neighbor, weight in graph[curr].items():
#             distance = dist + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 pred[neighbor] = curr
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances, pred

# # def shortest_path(pred, target):
# #     path = []
# #     curr = target
# #     while curr:
# #         path.append(curr)
# #         curr = pred[curr]
# #     return path[::-1]

# graph = Graph()

# for row in range(M):
#     for col in range(M):
#         if row > 0:
#             graph.add_edge(a[row][col], a[row - 1][col], a[row - 1][col])
#         if row < M - 1:
#             graph.add_edge(a[row][col], a[row + 1][col], a[row + 1][col])
#         if col < M - 1:
#             graph.add_edge(a[row][col], a[row][col + 1], a[row][col + 1])

# end_nodes = []


# smallest_dist = float('inf')

# for row in range(M):
#     start = a[row][0]
#     distances, pred = dijkstra(start, graph)
#     for 

dp = [[0 for _ in range(M)] for _ in range(M)]

for row in range(M):
    dp[row][0] = a[row][0]

for col in range(1, M):
    dp[0][col] = dp[0][col - 1] + a[0][col]

    for row in range(1, M):
        prev = dp[row][col - 1]
        weight = a[row][col]
        curr = prev + weight
        above = dp[row - 1][col]
        above_weight = a[row - 1][col]
        
        if curr + above_weight < above:
            dp[row - 1][col] = curr + above_weight
        if above + weight < curr:
            dp[row][col] = above + weight
        else:
            dp[row][col] = curr

    for row in range(M - 2, -1, -1):
        weight = a[row][col]
        curr = dp[row][col]
        below = dp[row + 1][col]
        below_weight = a[row + 1][col]
        if below + weight < curr:
            dp[row][col] = below + weight
        elif curr + below_weight < below:
            dp[row + 1][col] = curr + below_weight
        
min = dp[0][M - 1]
for row in range(M):
    if dp[row][M - 1] < min:
        min = dp[row][M - 1]

print(min)