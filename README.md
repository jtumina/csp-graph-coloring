# CSCI 4511: Project 2
## Constraint Satisfaction Problem - Graph Coloring
### Author: Jack Umina

## Algorithm Description
The algorithm begins with a list of uncolored vertexes left in the graph (which begins as every vertex). Then, for each vertex in the uncolored list, the following is performed:
1. `mrv()` is called to find the vertex *v* with the minimum remaing possible colors
2. `lcv()` then finds the least constraining color for the vertex *v*
3. *v*'s color is set to the color found by `lcv()`
4. *v* is removed from uncolored
5. `ac3()` is called to remove inconsistent values from each vertex's remaining possible colors

## Usage
#### Running the script:
```
python3 src/main.py "<path/to/file/with/graph/data>"
```
*or* <br>
`./tester.sh` can be run to run the algorithm on every text file contained in `graph-files/`

#### Formatting the graph data files:
```
# Lines beginning with '#' are treated as comments
# First non comment line is of the form 'colors = n'
colors = 3
# Now the vertexes/edges
<vertex_id>, <vertex_id>
# Vertexes are implied through an edge description
