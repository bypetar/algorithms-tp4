from graph import Graph
from collections import deque
import random
import time

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

    for i in graph._graph.keys():
        grafo_invertido.add_vertex(i)

        for j in graph.get_neighbors(i):
            grafo_invertido.add_vertex(j)
            grafo_invertido.add_edge(j, i)

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

        for i in reversed(grafo.get_neighbors(nodo)):
            if i not in visitados:
                pila.append((i, False))

def dfs_guardar_sccs(grafo, inicio, visitados, componente):
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        if nodo in visitados:
            continue

        visitados.add(nodo)
        componente.append(nodo)

        for i in grafo.get_neighbors(nodo):
            if i not in visitados:
                pila.append(i)

def kosaraju(grafo):

    visitados = set()
    orden = []

    for i in grafo._graph.keys():
        if i not in visitados:
            dfs(grafo, i, visitados, orden)

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

def bfs(grafo, origen):
    distancias = {origen: 0}
    cola = deque([origen])

    while cola:
        actual = cola.popleft()
        for i in grafo.get_neighbors(actual):
            if i not in distancias:
                distancias[i] = distancias[actual] + 1
                cola.append(i)

    return distancias

def contar_triangulos(grafo):
    total = 0
    for i in grafo._graph:
        for j in grafo.get_neighbors(i):
            for k in grafo.get_neighbors(j):
                if grafo.edge_exists(k, i):
                    total += 1
    return total // 3

def maximo_en_distancias(diccionario):
    if not diccionario:
        return 0
    return max(diccionario.values())


def diametro_grafo(grafo, cantidad_muestras):
    nodos = list(grafo._graph.keys())
    muestra = random.sample(nodos, cantidad_muestras)

    diametro_estimado = 0

    for i in muestra:
        distancias = bfs(grafo, i)
        max_distancia = maximo_en_distancias(distancias)
        if max_distancia > diametro_estimado:
            diametro_estimado = max_distancia

    return diametro_estimado

import random

def calcular_pagerank(grafo, caminos, longitud):
    visitas = {}
    nodos = list(grafo._graph.keys())

    for _ in range(caminos):
        actual = random.choice(nodos)

        for _ in range(longitud):
            if actual in visitas:
                visitas[actual] += 1
            else:
                visitas[actual] = 1

            vecinos = grafo.get_neighbors(actual)
            if vecinos:
                actual = random.choice(vecinos)
            else:
                break

    return visitas



def punto_1(graph):
    print("")
    print("Primer punto")
    print("")
    sccs = kosaraju(graph)
    cantidad = len(sccs)
    tamaño_max = max(len(c) for c in sccs)
    print("Cantidad de componentes fuertemente conexas:", cantidad)
    print("Tamaño de la componente más grande:", tamaño_max)

#punto_1(page_graph)

def punto_2(grafo):
    print("")
    print("Segundo punto")
    print("")
    nodos = list(grafo._graph.keys())
    muestra = random.sample(nodos, 100)

    inicio = time.time()

    for nodo in muestra:
        bfs(grafo, nodo)

    fin = time.time()

    tiempo_total = fin - inicio
    tiempo_promedio = tiempo_total / len(muestra)
    estimado_todos = tiempo_promedio * len(nodos)

    print("Se procesaron", len(muestra), "nodos.")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print(f"Tiempo promedio por nodo: {tiempo_promedio:.4f} segundos")
    print(f"Tiempo estimado para todos los nodos: {estimado_todos / 3600:.2f} horas")
    print("Orden del algoritmo BFS desde cada nodo: O(V + E)")
    print("Orden total estimado (todos con todos): O(V*(V + E))")

#punto_2(page_graph)

def punto_3(grafo):
    print("")
    print("Tercer punto")
    print("")
    cantidad = contar_triangulos(grafo)
    print("Cantidad de triángulos:", cantidad)

#punto_3(page_graph)

def punto_4(grafo):
    print("")
    print("Cuarto punto")
    print("")
    diametro = diametro_grafo(grafo, cantidad_muestras=500)
    print("Diámetro estimado del grafo:", diametro)

#punto_4(page_graph)

def punto_5(grafo):
    print("")
    print("Quinto punto")
    print("")
    visitas = calcular_pagerank(grafo, caminos=100000, longitud=20)

    top_10 = sorted(visitas.items(), key=lambda x: x[1], reverse=True)[:10]

    print("Top 10 páginas con mayor PageRank:")
    for nodo, cantidad in top_10:
        print(f"Nodo {nodo}: {cantidad} visitas")

#punto_5(page_graph)



