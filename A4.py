import sys
import random
from Instances import Instances

class A4:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]

    def addAresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        return sum(self.grafo[v])

    def pontuacao(self, v, color):
        return self.grau(v)

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

    def verificar_conflitos(self, colors):
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and colors[u] == colors[v]:
                    return True
        return False

    def get_num_color_used(self, colors):
        return max(colors) + 1 if colors else 0

    def iterated_local_search(self, max_iter=100):
        best_colors = None
        best_num_colors = float('inf')

        for _ in range(max_iter):
            colors = self.greedy_color()

            # Busca local para melhorar a solução
            colors = self.local_search(colors)

            num_colors = self.get_num_color_used(colors)
            if num_colors < best_num_colors:
                best_colors = colors
                best_num_colors = num_colors

        return best_colors

    def pode_recolorir(self, v, nova_cor, colors):
        for u in range(self.num_vertices):
            if self.grafo[v][u] == 1 and colors[u] == nova_cor:
                return False
        return True

    def local_search(self, colors):
        melhorou = True
        while melhorou:
            melhorou = False
            cores_usadas_antes = len(set(colors))

            vertices_para_recolorir = random.sample(range(self.num_vertices), len(colors)//3)  # Recolorir 1/3 dos vértices
            for v in vertices_para_recolorir:
                for nova_cor in range(max(colors) + 1):
                    if nova_cor != colors[v] and self.pode_recolorir(v, nova_cor, colors):
                        colors[v] = nova_cor
                        melhorou = True
                        break

            cores_usadas = sorted(set(colors))
            for antiga_cor in cores_usadas:
                if all(colors[v] != antiga_cor for v in range(self.num_vertices)):
                    colors = [c if c < antiga_cor else c - 1 for c in colors]
                    melhorou = True
                    break

            if len(set(colors)) == cores_usadas_antes:
                melhorou = False

        return colors

    def main(self, filename):
        #print(f"Executando o algoritmo de coloração para o arquivo {filename}...")
        instance = Instances(filename)

        g = A4(instance.num_vertices)
        for u, v in instance.edges:
            g.addAresta(u, v)

        colors = g.greedy_color()
        #print("Resultado inicial (guloso):", colors)
        num_types_initial = g.get_num_color_used(colors)
        #print(f"Quantidade de tipos de prova usados (inicial): {num_types_initial}")

        colors = g.iterated_local_search(max_iter=200)
        num_types_after = g.get_num_color_used(colors)

        #print("Resultado após buscal:", colors)
        print(f" {num_types_after}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorreto. Passe o arquivo de entrada como parâmetro.")
        sys.exit(1)

    filename = sys.argv[1]
    a2_instance = A4(0)
    a2_instance.main(filename)