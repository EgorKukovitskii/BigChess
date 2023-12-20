import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
LIGHT_SQUARE = (240, 217, 181)  # Светлая клетка
DARK_SQUARE = (181, 136, 99)   # Темная клетка

# Размеры окна
WIDTH, HEIGHT = 800, 800

# Размеры и количество клеток на игровой доске
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шахматная доска 10x10')

# Создание класса для фигур
class Piece:
    '''class for chess figure object
    :param color: color of figure
    :type color: str
    :param type: type of figure
    :type type: str
    :param image: image of figure
    :type image: png
    '''
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = image

# Загрузка изображений фигур и изменение их размера
white_rook_image = pygame.transform.scale(pygame.image.load('images/white_rook_image.png'), (CELL_SIZE, CELL_SIZE))
black_rook_image = pygame.transform.scale(pygame.image.load('images/black_rook_image.png'), (CELL_SIZE, CELL_SIZE))
white_knight_image = pygame.transform.scale(pygame.image.load('images/white_knight_image.png'), (CELL_SIZE, CELL_SIZE))
black_knight_image = pygame.transform.scale(pygame.image.load('images/black_knight_image.png'), (CELL_SIZE, CELL_SIZE))
white_bishop_image = pygame.transform.scale(pygame.image.load('images/white_bishop_image.png'), (CELL_SIZE, CELL_SIZE))
black_bishop_image = pygame.transform.scale(pygame.image.load('images/black_bishop_image.png'), (CELL_SIZE, CELL_SIZE))
white_shaman_image = pygame.transform.scale(pygame.image.load('images/white_shaman_image.png'), (CELL_SIZE, CELL_SIZE))
black_shaman_image = pygame.transform.scale(pygame.image.load('images/black_shaman_image.png'), (CELL_SIZE, CELL_SIZE))
white_queen_image = pygame.transform.scale(pygame.image.load('images/white_queen_image.png'), (CELL_SIZE, CELL_SIZE))
black_queen_image = pygame.transform.scale(pygame.image.load('images/black_queen_image.png'), (CELL_SIZE, CELL_SIZE))
white_king_image = pygame.transform.scale(pygame.image.load('images/white_king_image.png'), (CELL_SIZE, CELL_SIZE))
black_king_image = pygame.transform.scale(pygame.image.load('images/black_king_image.png'), (CELL_SIZE, CELL_SIZE))
white_pawn_image = pygame.transform.scale(pygame.image.load('images/white_pawn_image.png'), (CELL_SIZE, CELL_SIZE))
black_pawn_image = pygame.transform.scale(pygame.image.load('images/black_pawn_image.png'), (CELL_SIZE, CELL_SIZE))

# Инициализация фигур

pawn_white = Piece("white", "pawn", white_pawn_image)

rook_white = Piece("white", "rook", white_rook_image)
knight_white = Piece("white", "knight", white_knight_image)
bishop_white = Piece("white", "bishop", white_bishop_image)
shaman_white = Piece("white", "shaman", white_shaman_image)
queen_white = Piece("white", "queen", white_queen_image)
king_white = Piece("white", "king", white_king_image)

pawn_black = Piece("black", "pawn", black_pawn_image)

rook_black = Piece("black", "rook", black_rook_image)
knight_black = Piece("black", "knight", black_knight_image)
bishop_black = Piece("black", "bishop", black_bishop_image)
shaman_black = Piece("black", "shaman", black_shaman_image)
queen_black = Piece("black", "queen", black_queen_image)
king_black = Piece("black", "king", black_king_image)


# Фигуры на доске
pieces = [
    [rook_black, knight_black, bishop_black, shaman_black, queen_black, king_black, shaman_black, bishop_black, knight_black, rook_black],
    [pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black],
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [None] * 10,
    [pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white, pawn_white],
    [rook_white, knight_white, bishop_white, shaman_white, queen_white, king_white, shaman_white, bishop_white, knight_white, rook_white]
]

selected_piece = None  # Выбранная фигура

# Функция для проверки возможности хода для Ладьи
def valid_move_rook(row: int, col: int, new_row: int, new_col: int, pieces: list) -> bool:
    '''Returns is this move is valid for rook

    :param row: row of figure position
    :param col: col of figure position
    :param new_row: row of clicked position
    :param new_col: col of clicked position
    :param pieces: array of all chess table
    :returns: True or False that defines validity
    '''
    if not (0 <= col < 10 and 0 <= row < 10 and 0 <= new_col < 10 and 0 <= new_row < 10):
        return False
    if pieces[new_row][new_col] != None and pieces[new_row][new_col].color == pieces[row][col].color:
        return False
    if col == new_col:
        start_row = min(row, new_row)
        end_row = max(row, new_row)
        for r in range(start_row+1, end_row):
            if pieces[r][col] != None:
                return False
    else:
        start_col = min(col, new_col)
        end_col = max(col, new_col)
        for c in range(start_col+1, end_col):
            if pieces[row][c] != None:
                return False
    return True


# Функция для проверки возможности хода для Слона
def valid_move_bishop(row: int, col: int, new_row: int, new_col: int, pieces: list) -> bool:
    '''Returns is this move is valid for bishop

    :param row: row of figure position
    :param col: col of figure position
    :param new_row: row of clicked position
    :param new_col: col of clicked position
    :param pieces: array of all chess table
    :returns: True or False that defines validity
    '''
    if not (0 <= col < 10 and 0 <= row < 10 and 0 <= new_col < 10 and 0 <= new_row < 10):
        return False
    if pieces[new_row][new_col] != None and pieces[new_row][new_col].color == pieces[row][col].color:
        return False
    if abs(new_col - col) != abs(new_row - row):
        return False
    diff_row = new_row - row
    diff_col = new_col - col
    step_row = 1 if diff_row > 0 else -1
    step_col = 1 if diff_col > 0 else -1
    check_row = row + step_row
    check_col = col + step_col
    while check_row != new_row and check_col != new_col:
        if pieces[check_row][check_col] != None:
            return False
        check_row += step_row
        check_col += step_col
    return True


# Функция для получения возможных ходов для выбранной фигуры
def get_possible_moves(row: int, col: int) -> list:
    '''Returns all possible moves for figure in <row> row and <col> col

    :param row: figure row
    :param col: figure col
    '''

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
        if (player_turn == "white" and row == 8) or (player_turn == "black" and row == 1):
            new_row = row + 2 * direction
            new_col = col
            if new_row >= 0 and new_row < 10 and new_col >= 0 and new_col < 10 and pieces[new_row][new_col] is None and pieces[row + direction][new_col] is None:
                possible_moves.append((new_row, new_col))
                
        # Проверка возможности взятия фигуры по диагонали
        for i in [-1, 1]:
            new_row = row + direction
            new_col = col + i
            if new_row >= 0 and new_row < 10 and new_col >= 0 and new_col < 10 and pieces[new_row][new_col] is not None and pieces[row][col].color != pieces[new_row][new_col].color:
                possible_moves.append((new_row, new_col))
    if selected_piece.type == 'king':
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < 10 and 0 <= new_col < 10:
                    if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                        possible_moves.append((new_row, new_col))
    if selected_piece.type == 'knight':
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    possible_moves.append((new_row, new_col))
    if selected_piece.type == 'rook':
        rook_moves = [(i, 0) for i in range(-9, 10)] + [(0, i) for i in range(-9, 10)]
        for move in rook_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_rook(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
    if selected_piece.type == 'shaman':
        bishop_moves = [(i, i) for i in range(-9, 10)] + [(i, -i) for i in range(-9, 10)]
        for move in bishop_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_bishop(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
        rook_moves = [(i, 0) for i in range(-9, 10)] + [(0, i) for i in range(-9, 10)]
        for move in rook_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_rook(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    possible_moves.append((new_row, new_col))
                        
    if selected_piece.type == 'bishop':
        bishop_moves = [(i, i) for i in range(-9, 10)] + [(i, -i) for i in range(-9, 10)]
        for move in bishop_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_bishop(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
    if selected_piece.type == 'queen':
        bishop_moves = [(i, i) for i in range(-9, 10)] + [(i, -i) for i in range(-9, 10)]
        for move in bishop_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_bishop(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
        rook_moves = [(i, 0) for i in range(-9, 10)] + [(0, i) for i in range(-9, 10)]
        for move in rook_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 10 and 0 <= new_col < 10:
                if pieces[new_row][new_col] is None or pieces[new_row][new_col].color != pieces[row][col].color:
                    if valid_move_rook(row, col, new_row, new_col, pieces) == True:
                        possible_moves.append((new_row, new_col))
    return possible_moves


# Функция для отображения доски и фигур
def draw_board():
    '''Draw the board with chess figures'''
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
                        # Отобразить подсветку для возможных ходов
                        move_row, move_col = move
                        circles.append((screen, (0, 128, 0), ((move_col + 0.5) * CELL_SIZE, (move_row + 0.5) * CELL_SIZE), CELL_SIZE//8))
                else:
                    selected_piece = None
            else:
                new_row, new_col = clicked_row, clicked_col
                if (new_row, new_col) in possible_moves:
                    pieces[new_row][new_col] = selected_piece
                    pieces[position[0]][position[1]] = None
                    player_turn = "black" if player_turn == "white" else "white"
                else:
                    print(possible_moves, 'он не наступил, потому что нельзя')
                for i in range(10):
                    if pieces[0][i]!=None and pieces[0][i].type=='pawn':
                        if pieces[0][i].color=='white':
                            pieces[0][i] = queen_white
                        else:
                            pieces[0][i] = queen_black
                    if pieces[-1][i]!=None and pieces[-1][i].type=='pawn':
                        if pieces[-1][i].color=='white':
                            pieces[-1][i] = queen_white
                        else:
                            pieces[-1][i] = queen_black   
                circles=[]
                selected_piece = None

    # Отображение доски и фигур
    draw_board()
    pygame.display.flip()

pygame.quit()
