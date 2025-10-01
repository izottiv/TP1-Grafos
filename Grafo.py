import heapq 
class Grafo:

    def __init__ (self): #Inicia o dicionario que vai ser usado pra armazenar a estrutura do grafo
        self.lista = {}

    def adicionarVertice(self, v): #Adiciona no dicionario o vertice com as tuplas vazias
        if v not in self.lista:
            self.lista[v] = []

    def adicionarAresta(self, v, u, peso): #Adiciona os vertices e adiciona a tupla de conexão/peso
        self.adicionarVertice(v)
        self.adicionarVertice(u)
        self.lista[u].append((v,peso))
        self.lista[v].append((u,peso))

    def printDicionario(self): #Imprime o dicionario
        for v, vizinhos in self.lista.items(): #lista.items retorna tanto o indice do dicionario quanto as duplas, ent uma é armazenada em v(vertices) e os vizinhos e pesos são armazenados em vizinhos
            print(v, "->", vizinhos)

    def numeroDeCidades(self):
        vertices = []
        for v, _ in self.lista.items():
            vertices.append(v)
        return len(vertices)
    
    def estradas(self):
        estradasV = []
        vistas = set()
        for v, estradas in self.lista.items():
            for u, _ in estradas:
                if (u,v) not in vistas:
                    estradasV.append((v,u))
                    vistas.add((v,u))
        return estradasV
    
    def numeroEstradas(self):
        return (len(self.estradas()))

    def vizinhosDoVertice(self, vertice):
        vizinhosV = []
        for v, vizinhos in self.lista.items():
            if v == vertice:
                for vz, _ in vizinhos:
                    vizinhosV.append(vz)
        return vizinhosV

    def grauDoVertice(self, vertice):
        return len(self.vizinhosDoVertice(vertice))
    
    def dijkstra(self, v):
        dist = {v: float('inf') for v in self.lista}
        dist[v] = 0
        fila = [(0, v)]
        
        while fila:
            distancia_atual, v = heapq.heappop(fila)
            if distancia_atual > dist[v]:
                continue

            for vizinho, peso in self.lista[v]:
                nova_dist = distancia_atual + peso
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    heapq.heappush(fila, (nova_dist, vizinho))
        return dist
    
    def retornarMenorDistanciaEntreDuasCidades(self, v, u):
        menor = self.dijkstra(v)
        return (menor[u])
    
    def ehConexo(self):
        visitados  = set()
        print(self.lista)


