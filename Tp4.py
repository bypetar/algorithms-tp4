from graph import Graph

page_graph = Graph()

with open('web-Google.txt', 'r') as file:
    for l in file:
        if "# FromNodeId	ToNodeId" in l:
            break
    for l in file:
        if not l:
            break
        edge = tuple(int(v.replace("\n", "").replace("\t", "")) for v in l.split("\t"))
        for v in edge:
            if not page_graph.vertex_exists(v):
                page_graph.add_vertex(str(v))
        page_graph.add_edge(str(edge[0]), str(edge[1]))


def invertir_grafo(graph: Graph): 
    grafo_invertido = Graph()

    for v in graph._graph.keys():
        grafo_invertido.add_vertex(v)

        for vecino in graph.get_neighbors(v):
            grafo_invertido.add_vertex(vecino)
            grafo_invertido.add_edge(vecino, v)

    return grafo_invertido

def dfs(grafo, inicio, visitados, orden=None):
    pila = [(inicio, False)]
    while pila:
        nodo, procesado = pila.pop()
        if procesado:
            if orden is not None:
                orden.append(nodo)
            continue  

        if nodo in visitados:
            continue

        visitados.add(nodo)
        pila.append((nodo, True))

        for vecino in reversed(grafo.get_neighbors(nodo)):
            if vecino not in visitados:
                pila.append((vecino, False))

def dfs_guardar_sccs(grafo, inicio, visitados, componente):
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        if nodo in visitados:
            continue

        visitados.add(nodo)
        componente.append(nodo)

        for vecino in grafo.get_neighbors(nodo):
            if vecino not in visitados:
                pila.append(vecino)

def kosaraju(grafo):

    visitados = set()
    orden = []

    for nodo in grafo._graph.keys():
        if nodo not in visitados:
            dfs(grafo, nodo, visitados, orden)

    grafo_invertido = invertir_grafo(grafo)
    visitados = set()
    sccs = []

    while orden:
        nodo = orden.pop()
        if nodo not in visitados:
            componente = []
            dfs_guardar_sccs(grafo_invertido, nodo, visitados, componente)
            sccs.append(componente)
    return sccs

def punto_1(graph):
    sccs = kosaraju(graph)
    cantidad = len(sccs)
    tamaño_max = max(len(c) for c in sccs)
    print("Cantidad de componentes fuertemente conexas:", cantidad)
    print("Tamaño de la componente más grande:", tamaño_max)
punto_1(page_graph)