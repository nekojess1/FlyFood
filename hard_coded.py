import itertools

""" Retorna um dicionário com a posição de cada letra na matriz """
def get_data(file):
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
def get_min_route(positions, allPossiblesRoutes):
    distances = {}
    minDistance = 0
    minDistanceRoute = "" 
    for possibility in allPossiblesRoutes:                              # Calcula o custo de todas as rotas
        totalDistance = 0 
        for indice in range(len(possibility)):
            if (indice + 1 < len(possibility)):
                totalDistance += get_distance(indice,possibility)
        if (totalDistance < minDistance or minDistance == 0):
            minDistance = totalDistance
            minDistanceRoute = possibility
        distances[possibility] = totalDistance          # Atribui a distância por tal rota
    return minDistanceRoute

    

""" Retorna a distância entre 2 pontos """ 
def get_distance(indice, possibility):
    atualLetter = positions.get(possibility[indice])
    nextLetter = positions.get(possibility[indice + 1])
    firstSubtraction = abs(atualLetter[0] - nextLetter[0])
    secondSubtraction = abs(atualLetter[1] - nextLetter[1])
    return firstSubtraction + secondSubtraction


file = open('arquivo.txt', 'r')
positions = get_data(file)
allPossiblesRoutes = permutation(positions)
minRoute = get_min_route(positions, allPossiblesRoutes) 
print(minRoute)
