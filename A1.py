class A1:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]

    def addEdge(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        return sum(self.grafo[v])

    def pontuacao(self, v):
        return self.grau(v)

    def greedy_color_by_degree(self):
        vertices = sorted(range(self.num_vertices), key=self.pontuacao, reverse=True)
        color = [-1] * self.num_vertices

        for u in vertices:
            available = [True] * self.num_vertices

            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and color[v] != -1:
                    available[color[v]] = False

            for color_candidate in range(self.num_vertices):
                if available[color_candidate]:
                    color[u] = color_candidate
                    break

        return color

    def get_num_color_used(self, colors):
        return max(colors) + 1

    def verificar_vizinhos_com_mesma_cor(self, colors):
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and colors[u] == colors[v]:
                    print(f"Vértices {u} e {v} têm a mesma cor ({colors[u]})!")
        return True