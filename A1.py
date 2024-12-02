from Instances import Instances
import sys

class A1:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)] #MatrizAdj
        self.cores = [-1] * num_vertices

    def addAresta(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        return sum(self.grafo[v])

    def pontuacao(self, v):
        #Calcula a pontuação do vértice com base no grau (número de conexões).
        return self.grau(v)

    def greedy_color_by_rank(self):
        # Conjunto V0 dos vértices não coloridos
        vertices_nao_coloridos = set(range(self.num_vertices))

        # Inicializa as cores
        cores = [-1] * self.num_vertices

        # Lista de pontuações e ordenação inicial
        pontuacoes = [(v, self.pontuacao(v)) for v in vertices_nao_coloridos]
        pontuacoes.sort(key=lambda x: x[1], reverse=True)

        # Enquanto houver vértices não coloridos
        while vertices_nao_coloridos:
            # Seleciona o vértice com maior pontuação (primeiro da lista ordenada)
            v = pontuacoes.pop(0)[0]  # Pega o vértice com maior pontuação

            # Encontra os tipos de cores já atribuídos aos vizinhos
            vizinhos = [cores[u] for u in range(self.num_vertices) if self.grafo[v][u] == 1]

            # Atribui a menor cor disponível ao vértice v
            for tipo in range(self.num_vertices):
                if tipo not in vizinhos:
                    cores[v] = tipo
                    break

            # Remove o vértice v de V0 (não coloridos)
            vertices_nao_coloridos.remove(v)

            # Atualiza a lista de pontuações removendo o vértice v
            pontuacoes = [(u, self.pontuacao(u)) for u in vertices_nao_coloridos]
            pontuacoes.sort(key=lambda x: x[1], reverse=True)

        return cores

    def get_num_color_used(self, cores):
        # Cores são indexadas a partir de 0 por isso +1
        return max(cores) + 1 if cores else 0

    def verificar_vizinhos_com_mesma_cor(self, cores):
       #Verifica se existem vértices vizinhos com a mesma cor.

        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and cores[u] == cores[v] and cores[u] != -1:
                    print(f"Vértices {u} e {v} têm a mesma cor ({cores[u]})!")
        return True

    def main(self, filename):
        #print(f"Executando o algoritmo de coloração para o arquivo {filename}...")
        instance = Instances(filename)

        g = A1(instance.num_vertices)
        for u, v in instance.edges:
            g.addAresta(u, v)

        colors = g.greedy_color_by_rank()
        num_types = g.get_num_color_used(colors)

        #print("Tipos de prova atribuídos a cada mesa:", colors)
        print(num_types)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso incorreto. Passe o arquivo de entrada como parâmetro.")
        sys.exit(1)

    filename = sys.argv[1]
    a2_instance = A1(0)
    a2_instance.main(filename)