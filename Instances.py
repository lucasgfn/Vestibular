class Instances:

    def __init__(self, path):
        self.num_vertices = 0
        self.edges = []
        self.read_instance(path)


    def read_instance(self, path):
        with open(path, 'r') as file:
            for line in file:
                if line.startswith("p edge"):

                    parts = line.split()
                    self.num_vertices = int(parts[2])
                elif line.startswith("e"):

                    parts = line.split()
                    u = int(parts[1]) - 1
                    v = int(parts[2]) - 1
                    self.edges.append((u, v))