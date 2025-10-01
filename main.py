from Grafo import Grafo

g = Grafo()
nomeArquivo = input(("Escolha o arquivo com o conjunto de arestas: "))

with open(nomeArquivo) as arquivo:
    for linha in arquivo:
        linha = linha.strip() 
        v, u, peso = linha.split(",")
        g.adicionarAresta(v, u, int(peso))

menu = True
while(menu == True):
    escolha = int(input("Deseja realizar qual operação utilizando a bibliotceca ?\n" \
    "1 - Retornar o número de cidades no grafo\n" \
    "2 - Retornar a quantidade de estradas no grafo\n" \
    "3 - Retornar os vizinhos de uma cidade fornecida\n" \
    "4 - Determinar a quantidade de vizinhos de uma cidade fornecida\n" \
    "5 - Calcular o menor caminho entre duas cidades escolhidas\n" \
    "Escolha: "))
    if  escolha == 1:
        print(f"\nO número de cidades no grafo é: {g.numeroDeCidades()}")
    elif escolha == 2:
        print(f"\nA quantidade de estradas no grafo é:{g.numeroEstradas()}")
    elif escolha == 3:
        v = input("Digite a cidade no qual deseja determinar os vizinhos:").upper()
        print(f"\nA cidade {v} é vizinha das cidades: {', '.join(g.vizinhosDoVertice(v))}")
    elif escolha == 4:
        v = input("Digite a cidade no qual deseja determinar a quantidade de vizinhos: \n").upper()
        print(f"\nA cidade {v} possui {g.grauDoVertice(v)} vizinhos")
    elif escolha == 5:
        v, u = input("Digite as duas cidades que desenha descobrir a menor distancia (separadas por espaço): ").split()
        v = v.upper()
        u = u.upper()
        print(f"\nA menor distancia entre a cidade {v} e {u} é {g.retornarMenorDistanciaEntreDuasCidades(v, u)}");
    retornar= int(input("\nDeseja retornar ao menu para fazer outra operação:\n" \
    "1 - Sim\n" \
    "2 - Não, encerrar o programa\n"
    "Escolha: "))
    print("="*50)
    if retornar == 2:
        menu = False