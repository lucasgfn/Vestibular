from Vestibular import Vestibular
from Instances import Instances

if __name__ == "__main__":
    instance = Instances("salas/sala1.txt")

    g = Vestibular(instance.num_vertices)
    for u, v in instance.edges:
        g.addEdge(u, v)

    colors = g.greedy_color()
    num_types = g.get_num_colorUsed(colors)

    print("Tipos de prova atribuídos a cada mesa:", colors)
    print("Quantidade de tipos de prova usados:", num_types)


    if g.verificar_vizinhos_com_mesma_cor(colors):
       print("Todos os vizinhos têm cores diferentes.")
    else:
        print("Alguns vizinhos têm a mesma cor.")


