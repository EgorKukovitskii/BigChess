import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
LIGHT_SQUARE = (240, 217, 181)  # Светлая клетка
DARK_SQUARE = (181, 136, 99)   # Темная клетка

# Размеры окна
WIDTH, HEIGHT = 500, 500

# Размеры и количество клеток на игровой доске
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шахматная доска 10x10')

# Создание класса для фигур
class Piece:
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = image

# Загрузка изображений фигур и изменение их размера
rook_image = pygame.transform.scale(pygame.image.load('images/rook.png'), (CELL_SIZE, CELL_SIZE))
knight_image = pygame.transform.scale(pygame.image.load('images/knight.png'), (CELL_SIZE, CELL_SIZE))
bishop_image = pygame.transform.scale(pygame.image.load('images/bishop.png'), (CELL_SIZE, CELL_SIZE))
shaman_image = pygame.transform.scale(pygame.image.load('images/shaman.png'), (CELL_SIZE, CELL_SIZE))
queen_image = pygame.transform.scale(pygame.image.load('images/queen.png'), (CELL_SIZE, CELL_SIZE))
king_image = pygame.transform.scale(pygame.image.load('images/king.png'), (CELL_SIZE, CELL_SIZE))
pawn_image = pygame.transform.scale(pygame.image.load('images/pawn.png'), (CELL_SIZE, CELL_SIZE))

# Инициализация фигур

pawn1_white = Piece("white", "pawn", pawn_image)
pawn2_white = Piece("white", "pawn", pawn_image)
pawn3_white = Piece("white", "pawn", pawn_image)
pawn4_white = Piece("white", "pawn", pawn_image)
pawn5_white = Piece("white", "pawn", pawn_image)
pawn6_white = Piece("white", "pawn", pawn_image)
pawn7_white = Piece("white", "pawn", pawn_image)
pawn8_white = Piece("white", "pawn", pawn_image)
pawn9_white = Piece("white", "pawn", pawn_image)
pawn10_white = Piece("white", "pawn", pawn_image)

rook1_white = Piece("white", "rook", rook_image)
knight1_white = Piece("white", "knight", knight_image)
bishop1_white = Piece("white", "bishop", bishop_image)
shaman1_white = Piece("white", "shaman", shaman_image)
queen_white = Piece("white", "queen", queen_image)
king_white = Piece("white", "king", king_image)
shaman2_white = Piece("white", "shaman", shaman_image)
bishop2_white = Piece("white", "bishop", bishop_image)
knight2_white = Piece("white", "knight", knight_image)
rook2_white = Piece("white", "rook", rook_image)

pawn1_black = Piece("black", "pawn", pawn_image)
pawn2_black = Piece("black", "pawn", pawn_image)
pawn3_black = Piece("black", "pawn", pawn_image)
pawn4_black = Piece("black", "pawn", pawn_image)
pawn5_black = Piece("black", "pawn", pawn_image)
pawn6_black = Piece("black", "pawn", pawn_image)
pawn7_black = Piece("black", "pawn", pawn_image)
pawn8_black = Piece("black", "pawn", pawn_image)
pawn9_black = Piece("black", "pawn", pawn_image)
pawn10_black = Piece("black", "pawn", pawn_image)

rook1_black = Piece("black", "rook", rook_image)
knight1_black = Piece("black", "knight", knight_image)
bishop1_black = Piece("black", "bishop", bishop_image)
shaman1_black = Piece("black", "shaman", shaman_image)
queen_black = Piece("black", "queen", queen_image)
king_black = Piece("black", "king", king_image)
shaman2_black = Piece("black", "shaman", shaman_image)
bishop2_black = Piece("black", "bishop", bishop_image)
knight2_black = Piece("black", "knight", knight_image)
rook2_black = Piece("black", "rook", rook_image)


# Фигуры на доске
pieces = [
    [rook1_black, knight1_black, bishop1_black, shaman1_black, queen_black, king_black, shaman2_black, bishop2_black, knight2_black, rook2_black],
    [pawn1_black, pawn2_black, pawn3_black, pawn4_black, pawn5_black, pawn6_black, pawn7_black, pawn8_black, pawn9_black, pawn10_black],
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [pawn1_white, pawn2_white, pawn3_white, pawn4_white, pawn5_white, pawn6_white, pawn7_white, pawn8_white, pawn9_white, pawn10_white],
    [rook1_white, knight1_white, bishop1_white, shaman1_white, queen_white, king_white, shaman2_white, bishop2_white, knight2_white, rook2_white]
]


selected_piece = None  # Выбранная фигура

# Функция для проверки возможности хода для Ладьи
def valid_move_rook(row, col, new_row, new_col):
    return row == new_row or col == new_col

# Функция для проверки возможности хода для Коня
def valid_move_knight(row, col, new_row, new_col):
    return (abs(new_row - row) == 2 and abs(new_col - col) == 1) or (abs(new_row - row) == 1 and abs(new_col - col) == 2)

# Функция для проверки возможности хода для Слона
def valid_move_bishop(row, col, new_row, new_col):
    return abs(new_row - row) == abs(new_col - col)

# Функция для проверки возможности хода для Ферзя
def valid_move_queen(row, col, new_row, new_col):
    return (row == new_row or col == new_col) or (abs(new_row - row) == abs(new_col - col))

# Функция для проверки возможности хода для Короля
def valid_move_king(row, col, new_row, new_col):
    return abs(new_row - row) <= 1 and abs(new_col - col) <= 1

# Функция для проверки возможности хода для Шамана
def valid_move_shaman(row, col, new_row, new_col):
    return abs(new_row - row) <= 1 and abs(new_col - col) <= 1

# Функция для проверки возможности хода для Пешки
def valid_move_pawn(row, col, new_row, new_col, player_color):
    if player_color == "white":
        direction = -1
        starting_row = 6
    else:
        direction = 1
        starting_row = 1
    
    # Передвижение на одну клетку вперед
    if col == new_col and row + direction == new_row and pieces[new_row][new_col] is None:
        return True
    
    # Передвижение на две клетки вперед из начальной позиции
    if col == new_col and row + 2 * direction == new_row and row == starting_row and pieces[row + direction][col] is None and pieces[new_row][new_col] is None:
        return True
    
    # Взятие фигуры по диагонали
    if abs(new_col - col) == 1 and row + direction == new_row and pieces[new_row][new_col] is not None:
        return True
    
    return False

# Функция для получения возможных ходов для выбранной фигуры
def get_possible_moves(row, col):
    possible_moves = []
    # Возможные ходы для пешки
    if selected_piece.type == "pawn":
        if player_turn == "white":
            direction = -1
        else:
            direction = 1

        # Проверка возможности хода на одну клетку вперед
        new_row = row + direction
        new_col = col
        if new_row >= 0 and new_row < 10 and new_col >= 0 and new_col < 10 and pieces[new_row][new_col] is None:
            possible_moves.append((new_row, new_col))

        # Проверка возможности хода на две клетки вперед из начальной позиции
        if (player_turn == "white" and row == 6) or (player_turn == "black" and row == 1):
            new_row = row + 2 * direction
            new_col = col
            if new_row >= 0 and new_row < 10 and new_col >= 0 and new_col < 10 and pieces[new_row][new_col] is None:
                possible_moves.append((new_row, new_col))

        # Проверка возможности взятия фигуры по диагонали
        for i in [-1, 1]:
            new_row = row + direction
            new_col = col + i
            if new_row >= 0 and new_row < 10 and new_col >= 0 and new_col < 10 and pieces[new_row][new_col] is not None:
                possible_moves.append((new_row, new_col))
    
    return possible_moves

# Функция для отображения доски и фигур
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # Отображение изображений фигур на доске
            piece = pieces[row][col]
            if piece:
                screen.blit(piece.image, (col * CELL_SIZE, row * CELL_SIZE))
    for cir in circles:
        pygame.draw.circle(*cir)

# Основной игровой цикл
running = True
selected_piece = None
player_turn = "white"  # Начинает белый игрок
circles =[]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // CELL_SIZE
            clicked_col = mouse_x // CELL_SIZE
            
            if selected_piece is None:
                selected_piece = pieces[clicked_row][clicked_col]
                # Проверка наличия выбранной фигуры и соответствие цвета ходящего игрока
                if selected_piece is not None and selected_piece.color == player_turn:
                    possible_moves = get_possible_moves(clicked_row, clicked_col)
                    position = (clicked_row, clicked_col)
                    print(possible_moves, 'отсюда можно попасть в эти позиции')
                    for move in possible_moves:
                        # Отобразить маркеры или подсветку для возможных ходов
                        move_row, move_col = move
                        circles.append((screen, (0, 255, 0), ((move_col + 0.5) * CELL_SIZE, (move_row + 0.5) * CELL_SIZE), CELL_SIZE//8))
            else:
                new_row, new_col = clicked_row, clicked_col
                if (new_row, new_col) in possible_moves:
                    pieces[new_row][new_col] = selected_piece
                    pieces[position[0]][position[1]] = None
                    player_turn = "black" if player_turn == "white" else "white"
                else:
                    print(possible_moves, 'он не наступил, потому что нельзя')
                circles=[]
                selected_piece = None

    # Отображение доски и фигур
    draw_board()
    pygame.display.flip()

pygame.quit()
