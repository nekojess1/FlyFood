import itertools

""" Retorna um dicionário com a posição de cada letra na matriz """
def get_data():
    positions = {}
    lineNumber, columnNumber =  map(int, file.readline().split(' '))      # Recebe o nº de linhas e colunas da matriz
    for line in range(lineNumber):
        lineList = file.readline().strip().split(' ')                     # Recebe a linha do arquivo e trata os espaços em branco
        try:
            for column in range(len(lineList)):
                if lineList[column] != '0' :                              # Verifica se o valor observado não é um "0"
                    positions[lineList[column]] = (line, column)          # Atribui a letra sua posição na matriz 
        except:
            print("Something else went wrong") 
    return(positions)


""" Retorna uma lista com todos os possíveis caminhos """
def permutation(positions):
    routesWithoutR = [item for item in positions if item != 'R']
    permutation = itertools.permutations(routesWithoutR)
    allPossiblesRoutes = ['R' + "".join(items) + 'R'  for items in list(permutation)]
    return allPossiblesRoutes

""" Retorna um dicionário com os custos de cada rota """
def calculate_cost(positions, allPossiblesRoutes):
    distances = {}
    for possibility in (allPossiblesRoutes):
        totalDistance = 0 
        for indice in range(len(possibility)):
            if (indice + 1 < len(possibility)):
                get_distance(indice,possibility)
        distances[possibility] = totalDistance          # Atribui a distância por tal rota
    return distances

""" Retorna a distância entre 2 pontos """ 
def get_distance(indice, possibility):
    atualLetter = positions.get(possibility[indice])
    nextLetter = positions.get(possibility[indice + 1])
    firstSubtraction = abs(atualLetter[0] - nextLetter[0])
    secondSubtraction = abs(atualLetter[1] - nextLetter[1])
    return firstSubtraction + secondSubtraction

""" Retorna o menor valor do dicionário """            
def min_cost(distances):
    return distances[min(distances, key=distances.get)]

""" Retorna o primeiro nome de chave a partir de um valor """
def get_route_name(dict, index):
    return list(dict.keys())[list(dict.values()).index(index)]

file = open('arquivo.txt', 'r')
positions = get_data()
allPossiblesRoutes = permutation(positions)
allCosts = calculate_cost(positions, allPossiblesRoutes)
minCostDic = min_cost(allCosts)
print(get_route_name(allCosts, minCostDic))
