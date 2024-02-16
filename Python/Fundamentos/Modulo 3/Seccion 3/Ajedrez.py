# Definir constantes para representar las piezas
EMPTY = '-'
PAWN_W = '♙'
ROOK_W = '♖'
KNIGHT_W = '♘'
BISHOP_W = '♗'
QUEEN_W = '♕'
KING_W = '♔'
PAWN_B = '♟'
ROOK_B = '♜'
KNIGHT_B = '♞'
BISHOP_B = '♝'
QUEEN_B = '♛'
KING_B = '♚'

# Crear un tablero de ajedrez vacío
def crear_tablero():
    tablero = [[EMPTY] * 8 for _ in range(8)]
    # Colocar piezas blancas
    tablero[0] = [ROOK_W, KNIGHT_W, BISHOP_W, QUEEN_W, KING_W, BISHOP_W, KNIGHT_W, ROOK_W]
    tablero[1] = [PAWN_W] * 8
    # Colocar piezas negras
    tablero[6] = [PAWN_B] * 8
    tablero[7] = [ROOK_B, KNIGHT_B, BISHOP_B, QUEEN_B, KING_B, BISHOP_B, KNIGHT_B, ROOK_B]
    return tablero

# Imprimir el tablero de ajedrez
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

# Ejemplo de uso
tablero = crear_tablero()
imprimir_tablero(tablero)
