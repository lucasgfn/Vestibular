import sys
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

    def grasp(self, max_iter=100):
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
        # Verifica se podemos recolorir v para nova_cor sem criar conflitos
        for u in range(self.num_vertices):
            if self.grafo[v][u] == 1 and colors[u] == nova_cor:
                return False
        return True

    def local_search(self, colors):
        melhorou = True
        while melhorou:
            melhorou = False
            cores_usadas_antes = len(set(colors))

            for v in range(self.num_vertices):
                for nova_cor in range(max(colors) + 1):
                    if nova_cor != colors[v] and self.pode_recolorir(v, nova_cor, colors):
                        colors[v] = nova_cor
                        melhorou = True
                        break

            # Reduzir número de cores usadas
            cores_usadas = sorted(set(colors))
            for antiga_cor in cores_usadas:
                if all(colors[v] != antiga_cor for v in range(self.num_vertices)):
                    colors = [c if c < antiga_cor else c - 1 for c in colors]
                    melhorou = True
                    break  # Ajuste uma cor por iteração

            # Verificar se houve melhoria real
            if len(set(colors)) == cores_usadas_antes:
                melhorou = False

        return colors

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
        colors = g.grasp(max_iter=100)
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

    filename = sys.argv[1]
    a2_instance = A4(0)
    a2_instance.main(filename)
