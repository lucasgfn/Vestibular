class Vestibular:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0]*num_vertices for _ in range(self.num_vertices)]

    def addEdge(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def greedy_color(self):
        color = [-1] * self.num_vertices
        available =  [True] *self.num_vertices

        color[0]= 0

        for u in range(1, self.num_vertices):
            for neighborhood in self.grafo[u]:
                if color[neighborhood]!=-1:
                    available[color[neighborhood]] = False

            for color_candidate in range(self.num_vertices):
                if available[color_candidate]:
                    color[u]= color_candidate
                    break

            available = [True] * self.num_vertices

        return color

    def get_num_colorUsed(self, color):
        return max(color) + 1

    def verificar_vizinhos_com_mesma_cor(self, colors):
        """ Verifica se dois vizinhos têm a mesma cor """
        for u in range(self.num_vertices):  # Use self.num_vertices para iterar corretamente
            for v in self.grafo[u]:
                if u != v and colors[u] == colors[v]:
                    print(f"Vértices {u} e {v} têm a mesma cor ({colors[u]})!")
        return True
