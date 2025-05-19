# Algoritmo_para_laberintos
# Descripcion del proyecto

Programa en Python que busca un camino desde un punto de inicio hasta un punto de destino dentro de un laberinto, usando el algoritmo de búsqueda en Profundidad Recursiva (DFS).

El laberinto es una matriz 5x5 donde (0) representa un camino libre y (1) una pared que no se puede atravesar.

El codigo busca una ruta desde la esquina superior izquierda (0,0) hasta la esquina inferior izquierda (4,4) usando DFS.

Guarda cada paso en una lista llamada camino.

Evita visitar celdas dos veces con la matriz "visitado" que es del mismo tamaño del laberinto.

Usa backtracking: si una ruta no funciona, vuelve atrás y prueba otra.

