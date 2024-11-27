from Instances import Instances
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

        while vertices_nao_coloridos:
            # Recalcula a o grau de cada vértice não colorido --> Lista de compreensão que armazena vertice e pontuacao
            pontuacoes = [(v, self.pontuacao(v)) for v in vertices_nao_coloridos]

            # Ordenação com Timsort --> Pior Caso O(n log n)
            pontuacoes.sort(key=lambda x: x[1], reverse=True)

            # Seleciona o vértice com maior grau porque esta sorted
            v = pontuacoes[0][0]

            # Encontra o primeiro tipo de prova não atribuído aos vizinhos --> vertices u vizinhos de v
            vizinhos = [cores[u] for u in range(self.num_vertices) if self.grafo[v][u] == 1]    #indica a existencia de um vertice na MatrizAdj
            for tipo in range(self.num_vertices):
                if tipo not in vizinhos:
                    cores[v] = tipo
                    break

            # Remove o vértice v de V0 (não coloridos)
            vertices_nao_coloridos.remove(v)

            # Recalcula novamente as pontuações dos vértices restantes
            pontuacoes = [(v, self.pontuacao(v)) for v in vertices_nao_coloridos]

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
        print(f"Executando o algoritmo de coloração para o arquivo {filename}...")
        instance = Instances(filename)

        g = A1(instance.num_vertices)
        for u, v in instance.edges:
            g.addAresta(u, v)

        colors = g.greedy_color_by_rank()
        num_types = g.get_num_color_used(colors)

        print("Tipos de prova atribuídos a cada mesa:", colors)
        print("Quantidade de tipos de prova usados:", num_types)

        if g.verificar_vizinhos_com_mesma_cor(colors):
           print("Todos os vizinhos têm cores diferentes.")
        else:
           print("Alguns vizinhos têm a mesma cor.")

if __name__ == "__main__":
    a1_instance = A1(0)
    a1_instance.main("salas/sala1.txt")