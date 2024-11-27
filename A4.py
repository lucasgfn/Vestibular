import sys
from Instances import Instances
import random

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

    def grasp(self, max_iter=100, alpha=0.5):
        best_colors = None
        best_num_colors = float('inf')

        for _ in range(max_iter):
            # Geração da solução inicial com a fase greedy randomizada
            colors = self.grasp_phase(alpha)
            # Busca local para melhorar a solução
            colors = self.local_search(colors)

            num_colors = self.get_num_color_used(colors)
            if num_colors < best_num_colors:
                best_colors = colors
                best_num_colors = num_colors

        return best_colors

    def grasp_phase(self, alpha):
        # Inicializa a coloração com -1 (sem cor)
        colors = [-1] * self.num_vertices
        available_colors = set(range(self.num_vertices))

        # Fase Greedy Randomizada
        for v in range(self.num_vertices):
            # Verifica quais cores estão disponíveis para o vértice
            used_colors = set()
            for u in range(self.num_vertices):
                if self.grafo[v][u] == 1 and colors[u] != -1:
                    used_colors.add(colors[u])

            available = available_colors - used_colors
            if available:
                # Seleciona uma cor aleatória dentro do conjunto de cores disponíveis
                restricted_set = list(available)
                num_choices = max(1, int(len(restricted_set) * alpha))
                random_choice = random.choice(restricted_set[:num_choices])
                colors[v] = random_choice

        return colors

    def local_search(self, colors):
        melhorou = True
        while melhorou:
            melhorou = False
            for v in range(self.num_vertices):
                # Tentar recolorir o vértice v para uma cor mais baixa, sem criar conflitos
                for nova_cor in range(colors[v]):
                    if self.pode_recolorir(v, nova_cor, colors):
                        colors[v] = nova_cor
                        melhorou = True
                        break
        return colors

    def pode_recolorir(self, v, nova_cor, colors):
        # Verifica se podemos recolorir v para nova_cor sem criar conflitos
        for u in range(self.num_vertices):
            if self.grafo[v][u] == 1 and colors[u] == nova_cor:
                return False
        return True

    def main(self, filename):
        print(f"Executando o algoritmo de coloração para o arquivo {filename}...")
        instance = Instances(filename)

        g = A4(instance.num_vertices)
        for u, v in instance.edges:
            g.addAresta(u, v)

        # Executando a coloração gulosa
        colors = g.greedy_color()
        print("Resultado inicial (guloso):", colors)
        num_types_initial = g.get_num_color_used(colors)
        print(f"Quantidade de tipos de prova usados (inicial): {num_types_initial}")

        # Aplica o GRASP para otimizar a quantidade de provas
        colors = g.grasp(max_iter=1000, alpha=0.5)
        num_types_after = g.get_num_color_used(colors)

        print("Resultado após GRASP:", colors)
        print(f"Quantidade de tipos de prova usados (após otimização): {num_types_after}")

        # Verificando se há vértices vizinhos com a mesma cor
        if g.verificar_conflitos(colors):
            print("Alguns vizinhos têm a mesma cor!")
        else:
            print("Todos os vizinhos têm cores diferentes.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorreto. Passe o arquivo de entrada como parâmetro.")
        sys.exit(1)

    filename = sys.argv[1]  # O primeiro argumento será o nome do arquivo
    a2_instance = A4(0)
    a2_instance.main(filename)
