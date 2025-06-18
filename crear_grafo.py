class Grafo:
    def __init__(self):                     #crea el diccionario del grafo.
        self.adyacentes = {}

    def agregar_nodo(self, nombre):         #agrega un nuevo nodo como clave si no esta
        if nombre not in self.adyacentes:
            self.adyacentes[nombre] = []
    def agregar_arista(self, origen, destino):      #verifica que el nodo origen y destino esten y luego los pone como key: value
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        if destino not in self.adyacentes[origen]:
            self.adyacentes[origen].append(destino)
    def nodos(self):                                #devuelve lista de todos los nodos
        return list(self.adyacentes.keys())
    def vecinos(self, nodo):                        #devuelve los vecinos de un nodo
        return list(self.adyacentes.get(nodo, []))
    def diccionario(self):                           #devuelve el grafo completo
        return self.adyacentes
    
def invertir_grafo(grafo):            #invierte el grafo. si A -> B, B -> A
    nuevo_grafo = Grafo()
    for i in grafo.nodos():
        for j in grafo.vecinos(i):
            nuevo_grafo.agregar_arista(j,i)
    return nuevo_grafo

def dfs(grafo, nodo, visitados, pila):  #recorre por cada nodo su primer vecino, luego el primer vecino de ese y asi.
    if nodo in visitados:
        return
    visitados.add(nodo)
    for i in grafo.vecinos(nodo):
        dfs(grafo, i, visitados, pila)  #llama recursivamente para que recorra el primer vecino del nodo hasta terminar.
    pila.append(nodo)                 #agrego a pila el ultimo nodo recorrido, que no tiene vecinos



graf = Grafo()
graf.agregar_arista("B","C")
graf.agregar_arista("B","D")
graf.agregar_arista("A","B")

new_graph = invertir_grafo(graf)
print(graf.diccionario())

print(new_graph.diccionario())
