# La matriz de visitados (visited) es una estructura de datos auxiliar que se usa para recordar qué celdas del 
# laberinto ya han sido exploradas por el algoritmo.


# Laberinto como una matriz
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

def dfs(maze, current, end, path, visited): #current: posición actual, end: posición final, path: camino recorrido, visited: matriz de visitados
    x, y = current
    if current == end:
        path.append(current)
        return True

    rows, cols = len(maze), len(maze[0]) # Obtener dimensiones del laberinto
    # Comprobar límites y si la celda es un obstáculo o ya visitada
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    if maze[x][y] == 1 or visited[x][y]:
        return False

    visited[x][y] = True
    path.append(current)

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # arriba, abajo, izq, der
    for dx, dy in directions:
        if dfs(maze, (x+dx, y+dy), end, path, visited):
            return True

    path.pop()  # Retroceder si no se encontró salida en esta rama
    return False

def solve_maze_dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []
    if dfs(maze, start, end, path, visited):
        return path
    else:
        return None

# Ejecutar y mostrar resultados
path = solve_maze_dfs(maze, start, end)

if path:
    print("Camino encontrado (DFS):")
    for step in path:
        print(step)
else:
    print("No hay camino disponible.")
