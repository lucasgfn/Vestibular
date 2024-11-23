class Vestibular:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]

    def addEdge(self, u, v):
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1

    def grau(self, v):
        """
        Calcula o grau de um vértice, considerando todos os vizinhos.
        """
        return sum(self.grafo[v])

    def pontuacao(self, v, color):
        """
        Calcula a pontuação de um vértice considerando o número de vizinhos
        que já têm tipo de prova atribuído.

        Args:
        - v: O vértice cuja pontuação será calculada.
        - color: Lista que indica o tipo de prova atribuído a cada vértice (ou -1 se não atribuído).

        Returns:
        - Pontuação do vértice (número de vizinhos com tipo de prova atribuído).
        """
        return sum(1 for u in range(self.num_vertices) if self.grafo[v][u] == 1 and color[u] != -1)

    def greedy_color_by_rank2(self):
        """
        Aplica a coloração gulosa considerando os vértices em ordem de pontuação dinâmica,
        baseada no número de vizinhos com prova atribuída.
        """
        # Inicializa a lista de cores com -1 (não colorido)
        color = [-1] * self.num_vertices

        # Conjunto de vértices não coloridos (V0)
        uncolored = set(range(self.num_vertices))

        # Itera enquanto houver vértices não coloridos
        while uncolored:
            # Recalcula a pontuação de todos os vértices não coloridos
            pontuacoes = [(v, self.pontuacao(v, color)) for v in uncolored]

            # Ordena os vértices com base na pontuação (maior pontuação primeiro)
            best_vertex = max(pontuacoes, key=lambda x: x[1])[0]

            # Marca as cores dos vizinhos como indisponíveis
            available = [True] * self.num_vertices
            for v in range(self.num_vertices):
                if self.grafo[best_vertex][v] == 1 and color[v] != -1:
                    available[color[v]] = False

            # Atribui o primeiro tipo de prova não atribuído aos vizinhos
            for color_candidate in range(self.num_vertices):
                if available[color_candidate]:
                    color[best_vertex] = color_candidate
                    break

            # Remove o vértice da lista de não coloridos (V0)
            uncolored.remove(best_vertex)

        return color

    def get_num_color_used(self, colors):
        """
        Calcula o número total de cores utilizadas.
        """
        return max(colors) + 1 if colors else 0

    def verificar_vizinhos_com_mesma_cor(self, colors):
        """
        Verifica se existem vértices vizinhos com a mesma cor.
        """
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.grafo[u][v] == 1 and colors[u] == colors[v]:
                    print(f"Vértices {u} e {v} têm a mesma cor ({colors[u]})!")
        return True
