class Vertex:
    def __init__(self, node_id, colors):
        self.id = node_id
        self.color = None # Only set once definite
        self.colors_remain = colors # All possible remaining colors
        self.adj = set() # Track nodes this one is adjacent to

    def add_neighbor(self, neighbor):
        self.adj.add(neighbor)

    def color(self, color):
        self.color = color

    def __str__(self):
        return str(self.id) + " : " + str(self.color)

    def print_edges(self):
        s = str(self) + "\n"
        for v in self.adj:
            s += "  -> " + str(v) + "\n"
        return s

class Graph:
    def __init__(self):
        self.nodes = {}
        self.colors = None # List of all possible colors

    def set_colors(self, colors):
        self.colors = colors

    def add_edge(self, src, dst):
        # Create vertex objects if they don't already exist
        if src not in self.nodes:
            self.nodes[src] = Vertex(src, self.colors)
        if dst not in self.nodes:
            self.nodes[dst] = Vertex(dst, self.colors)

        # Create edges
        self.nodes[src].add_neighbor(self.nodes[dst])
        self.nodes[dst].add_neighbor(self.nodes[src])

    def __str__(self):
        s = ""
        for v in self.nodes:
            s += str(self.nodes[v].print_edges())
            s += "\n"
        return s

