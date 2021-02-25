import sys
from graph import *

# Return of successive ints representing colors in range 0 to num_colors
def create_colors(num_colors):
    colors = []
    for i in range(1, int(num_colors+1)):
        colors.append(i)
    return colors

def populate_graph(graph, filename):
    f = open(filename, "r")
    lines = f.readlines()

    num_colors = 0

    for line in lines:
        # Skip comment lines
        if line[0] == "#":
            continue

        # This is the "Colors = n" line
        if num_colors == 0 and len(line) >= 8 and line[0:6] == "Colors":
            line = line[6:].lstrip().rstrip() 
            
            if line[0] != "=":
                return False 

            try: num_colors = int(line[1:])
            except: return False 

            graph.set_colors(create_colors(num_colors))

        # Once num_colors has been initialized, read vertexes and edges
        elif num_colors > 0: 
            vals = line.lstrip().rstrip().split(",")
            if len(vals) != 2:
                return False 

            graph.add_edge(vals[0], vals[1])

    return bool(num_colors) 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Incorrect arguments. Must provide filename of graph data.")

    graph = Graph()
    
    if not populate_graph(graph, sys.argv[1]):
        sys.exit("Unable to parse " + str(sys.argv[1]))

    graph.color_graph()  
    print(graph) 
