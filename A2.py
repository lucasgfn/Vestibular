from Instances import Instances
import sys

class A2:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]

    def addAresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        return sum(self.grafo[v])

    def pontuacao(self, v, color):
        return sum(1 for u in range(self.num_vertices) if self.grafo[v][u] == 1 and color[u] != -1)

    def greedy_color(self):
        color = [-1] * self.num_vertices

        vertices_nao_coloridos = set(range(self.num_vertices))

        while vertices_nao_coloridos:
            pontuacoes = [(v, self.pontuacao(v, color)) for v in vertices_nao_coloridos]

            maxPontuacao = max(pontuacoes, key=lambda x: x[1])[0]

            available = [True] * self.num_vertices
            for v in range(self.num_vertices):
                if self.grafo[maxPontuacao][v] == 1 and color[v] != -1:
                    available[color[v]] = False

            for color_candidate in range(self.num_vertices):
                if available[color_candidate]:
                    color[maxPontuacao] = color_candidate
                    break

            vertices_nao_coloridos.remove(maxPontuacao)

        return color

    def get_num_color_used(self, colors):
        return max(colors) + 1 if colors else 0

    def verificar_vizinhos_com_mesma_cor(self, colors):
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and colors[u] == colors[v]:
                    print(f"Vértices {u} e {v} têm a mesma cor ({colors[u]})!")
        return True

    def main(self, filename):
        #print(f"Executando o algoritmo de coloração para o arquivo {filename}...")
        instance = Instances(filename)

        g = A2(instance.num_vertices)
        for u, v in instance.edges:
            g.addAresta(u, v)

        colors = g.greedy_color()
        num_types = g.get_num_color_used(colors)

        #print("Tipos de prova atribuídos a cada mesa:", colors)
        print(num_types)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorreto. Passe o arquivo de entrada como parâmetro.")
        sys.exit(1)

    filename = sys.argv[1]
    a2_instance = A2(0)
    a2_instance.main(filename)
