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
        for v, vizinhos in self.lista.items(): #lista.items retorna tanto o indice do dicionario quanto as tuplas, ent uma é armazenada em v(vertices) e os vizinhos e pesos são armazenados em vizinhos
            print(v, "->", vizinhos)

    def Cidades(self):
        vertices = []  
        for v, _ in self.lista.items(): #pega apenas os vertices do dicionario e armazena eles na lista de vertices
            vertices.append(v)
        return vertices
    
    def numeroDeCidades(self):
        return len(self.Cidades()) #so um len pra pegar o tamanho da lista de vertice q é retornada na função cidade
    
    def estradas(self):
        estradasV = []
        vistas = set() #cria um set pra n repetir aresta tipo (1-2) e (2-1)
        for v, estradas in self.lista.items(): # pega as estrada e vertice
            for u, _ in estradas: #ignora os pesos
                if (u,v) not in vistas: #se a aresta n tiver sido adicionada ainda
                    estradasV.append((v,u))
                    vistas.add((v,u))
        return estradasV
    
    def numeroEstradas(self):
        return (len(self.estradas())) #len pra retornar o numero de cidades

    def vizinhosDoVertice(self, vertice):
        vizinhosV = []
        for v, vizinhos in self.lista.items(): #pega os vertices e vizinhos
            if v == vertice: #se encontrar o vertice pega a lista de ajacencia dele e armaenza no vetor
                for vz, _ in vizinhos:
                    vizinhosV.append(vz)
        return vizinhosV

    def grauDoVertice(self, vertice):
        return len(self.vizinhosDoVertice(vertice)) #len pra encontrar grau do vertice
    
    def dijkstra(self, v):
        dist = {v: float('inf') for v in self.lista} # cria um dicionario com o vertice e define a distancia como infinito 
        dist[v] = 0 # a distancia do vertice pra ele msm é 0
        fila = [(0, v)]
        
        while fila:
            distancia_atual, v = heapq.heappop(fila)
            if distancia_atual > dist[v]:
                continue

            for vizinho, peso in self.lista[v]:
                nova_dist = distancia_atual + peso     #calcula distancia e substitui se for menor (é o algoritmo dijkstra ent n tem pq explicar mt)
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    heapq.heappush(fila, (nova_dist, vizinho))
        return dist
    
    def retornarMenorDistanciaEntreDuasCidades(self, v, u):
        menor = self.dijkstra(v) # pega o vetor
        return (menor[u])
    
    def ehConexo(self):
        visitados  = set()
        vertices = self.Cidades()
        def dfs(v):
            if v in visitados: #se o v ja tiver nos visitados volta, se n adiciona
                return
            visitados.add(v)
            for vizinho, _ in self.lista[v]: #pega os vizinhos de x vertice e chama dfs(busca em profundidade) pra ele para q possa continuar seguindo a busca
                dfs(vizinho)
        dfs(vertices[0]) #faz com o primeiro vertice pq ja q é conexo n faz diferença
            
        if len(visitados) == len(vertices):
            return True
        else:
            return False


    def cidadesCriticas(self):
        Criticas = set()
        vertices = self.Cidades() #usa a mesma logica da busca em profundidade, mas segue a seguinte logica:
        for a in vertices:        #Pega o vetor de vertices e cria uma lista tbm de visitados, remove um vertice temporariamente e executa a busca em profundidade(ta explicada ali em cima) pra ver se é conexo se for não adiciona nada
            visitados = set()     #Se não for adiciona no set de Vertices criticos, apos isso remove o proximo vertice(o antigo retorna) e faz o msm teste
            def dfs(v):           #remove no caso = desconsiderar o vertice não realmente remove
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
    
    def validacaoPasseioTuristico(self):
        vertices = self.Cidades()
        for inicio in vertices:
            n_vertices_necessarios = 4
            pilha = [inicio]
            na_pilha = {inicio}
            melhor_ciclo = []
            # busca em profundidade para encontrar ciclos fechados (voltam ao 'inicio')
            # guarda o melhor ciclo encontrado em `melhor_ciclo`.
            
            # algoritmo de busca em profundidade - menor caminho
            def dfs(v):
                nonlocal melhor_ciclo
                for vizinho, _ in self.lista[v]:
                    if vizinho == inicio:
                        vertices_diferentes = len(set(pilha))
                        if vertices_diferentes >= 3:
                            ciclo = pilha[:] + [inicio]
                            melhor_diferente = len(set(melhor_ciclo[:-1])) if melhor_ciclo else 0
                            if vertices_diferentes > melhor_diferente:
                                melhor_ciclo = ciclo
                            if vertices_diferentes >= n_vertices_necessarios:
                                return True
                    elif vizinho not in na_pilha:
                        na_pilha.add(vizinho)
                        pilha.append(vizinho)
                        parada = dfs(vizinho)
                        pilha.pop()
                        na_pilha.remove(vizinho)
                        if parada:
                            return True
                return False
            dfs(inicio)
            if melhor_ciclo:
                return melhor_ciclo
            else:
                return []
        
    def imprimePasseioTuristico(self):
        caminho = self.validacaoPasseioTuristico()
        if caminho:
            # imprime o ciclo encontrado como sequência de cidades
            print(f"O passeio turístico encontrado é: {' -> '.join(caminho)}")
        else:
            # aviso caso nenhum ciclo adequado seja encontrado
            print("O passeio turístico não foi encontrado.")