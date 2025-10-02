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

    def Cidades(self):
        vertices = []
        for v, _ in self.lista.items():
            vertices.append(v)
        return vertices
    
    def numeroDeCidades(self):
        return len(self.Cidades())
    
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
        vertices = self.Cidades()
        def dfs(v):
            if v in visitados: #se o v ja tiver nos visitados volta, se n adiciona
                return
            visitados.add(v)
            for vizinho, _ in self.lista[v]: #pega os vizinhos de x vertice e chama dfs pra ele para q possa continuar seguindo a busca
                dfs(vizinho)
        dfs(vertices[0]) #faz com o primeiro vertice pq ja q é conexo n faz diferença
            
        if len(visitados) == len(vertices):
            return True
        else:
            return False


    def cidadesCriticas(self):
        Criticas = set()
        vertices = self.Cidades()
        for a in vertices:  
            visitados = set()    
            def dfs(v):
                if v in visitados:
                    return
                visitados.add(v)
                for vizinho, _ in self.lista[v]:
                    if vizinho != a:   
                        dfs(vizinho)
            inicio = next((v for v in vertices if v != a), None)
            dfs(inicio)
            if len(visitados) != len(vertices) - 1:
                Criticas.add(a)
        return Criticas
