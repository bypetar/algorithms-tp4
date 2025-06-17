typedef struct nodo{
char* nombre;
int* adyacentes; //lista de indices de paginas a las que apunta
size_t cant_adyacentes; //cantidad de vecinos
size_t cap_adyacentes; //capacidad del array
}Nodo_t;

typedef struct grafo{
nodo_t* nodos; //array dinamico de nodos
size_t cant_nodos; //cantidad actual de nodos
size_t cap_nodos; //capacidad del array
}grafo_t;

