class Vertex:
    def __init__(self, node_id, colors):
        self.id = node_id
        self.color = None # Only set once definite
        self.colors_remain = colors # All possible remaining colors
        self.adj = set() # Track nodes this one is adjacent to

    def color(self, color):
        self.color = color

    def add_neighbor(self, neighbor):
        self.adj.add(neighbor)

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

    def lcv(self, v):
        return None

    def mrv(self, uncolored):
        max_constrn_node = None

        for v in uncolored:
            # Get vertex obj of v
            v = self.nodes[v]

            # If this vertex has already been colored, continue
            if v.color != None:
                continue

            if max_constrn_node == None:
                max_constrn_node = v
            elif len(v.colors_remain) < len(max_constrn_node.colors_remain):
                max_constrn_node = v
            elif len(v.colors_remain) == len(max_constrn_node.colors_remain):
                if len(v.adj) > len(max_constrn_node.adj):
                    max_constrn_node = v

        return max_constrn_node

    
    #def rm_inconsistent_vals(self, v, u):
    #def ac3(self):

    def color_graph(self):
        while v := self.mrv():
            lcv = self.lcv(v)
            v.color(lcv)
            self.ac3()

        for v in self.nodes:
            print(self.nodes[v]) 
