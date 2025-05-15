# Laberinto: 0 = camino libre, 1 = pared
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Punto de inicio (fila, columna)
inicio = (0, 0)

# Punto de destino
final = (4, 4)

# Función para resolver el laberinto con DFS recursiva
def dfs(x, y, camino, visitado): #x: fila, y: columna, camino: lista de pasos, visitado: matriz de visitados
    # Si estamos fuera del laberinto, no hacemos nada
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False

    # Si estamos en una pared o ya visitamos esta celda, no continuamos
    if laberinto[x][y] == 1 or visitado[x][y]:
        return False

    # Agregamos la posición actual al camino
    camino.append((x, y))

    # Marcamos la celda como visitada
    visitado[x][y] = True

    # Si llegamos al destino, terminamos
    if (x, y) == final:
        return True

    # Probamos moverse en las 4 direcciones: arriba, abajo, izquierda, derecha
    if (dfs(x - 1, y, camino, visitado) or
        dfs(x + 1, y, camino, visitado) or
        dfs(x, y - 1, camino, visitado) or
        dfs(x, y + 1, camino, visitado)):
        return True

    # Si no se pudo avanzar, retrocedemos (backtracking)
    camino.pop()
    return False

# Función principal que prepara la matriz de visitados e inicia el DFS
def resolver_laberinto():
    # Creamos la matriz de visitados: al inicio todo es False
    visitado = [[False for _ in range(5)] for _ in range(5)]

    # Lista para guardar el camino desde el inicio hasta el final
    camino = []

    # Llamamos a DFS desde el punto inicial
    if dfs(inicio[0], inicio[1], camino, visitado):
        print("Camino encontrado:")
        for paso in camino:
            print(paso)
    else:
        print("No hay camino disponible.")

# Ejecutamos la función
resolver_laberinto()
