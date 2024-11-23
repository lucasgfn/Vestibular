class Vestibular:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]
        self.cores = [-1] * num_vertices  # Inicializa a lista de cores

    def addEdge(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        return sum(self.grafo[v])

    def pontuacao(self, v):
        """
        Calcula a pontuação do vértice com base no grau (número de conexões).
        """
        return self.grau(v)

    def greedy_color_by_rank(self):
        # Conjunto V0 dos vértices não coloridos
        vertices_nao_coloridos = set(range(self.num_vertices))

        # Inicializa as cores
        cores = [-1] * self.num_vertices

        while vertices_nao_coloridos:
            # Recalcula a pontuação (grau) de cada vértice não colorido
            pontuacoes = [(v, self.pontuacao(v)) for v in vertices_nao_coloridos]

            # Ordena os vértices de acordo com a pontuação (maior grau primeiro)
            pontuacoes.sort(key=lambda x: x[1], reverse=True)

            # Seleciona o vértice com maior grau
            v = pontuacoes[0][0]

            # Encontra o primeiro tipo de prova não atribuído aos vizinhos
            vizinhos = [cores[u] for u in range(self.num_vertices) if self.grafo[v][u] == 1]
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
        """
        Calcula o número total de tipos de prova utilizados.
        """
        return max(cores) + 1 if cores else 0

    def verificar_vizinhos_com_mesma_cor(self, cores):
        """
        Verifica se existem vértices vizinhos com a mesma cor.
        """
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and cores[u] == cores[v] and cores[u] != -1:
                    print(f"Vértices {u} e {v} têm a mesma cor ({cores[u]})!")
        return True
