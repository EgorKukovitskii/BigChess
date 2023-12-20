import asyncio
import websockets
import pygame

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Размеры и количество клеток на игровой доске
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Создание класса для фигур
class Piece:
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = image
    def to_json(self):
        return {
            "color": self.color,
            "type": self.type,
            "image": self.image
        }

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

connected_clients = set()

# Функция для обработки ходов игроков и игровой логики
async def handle_game(websocket, path):
    global connected_clients
    # Подключение нового игрока
    connected_clients.add(websocket)
    print(connected_clients)
    print('+ клиент, всего ', len(connected_clients))
    if len(connected_clients) > 2:
            await websocket.close()
    try:
        while len(connected_clients)<2:
            await asyncio.sleep(1)
        await websocket.send('start')
        await start_game(websocket, path)
    finally:
        connected_clients.remove(websocket)
        print('- клиент, всего ', len(connected_clients))
        
async def start_game(websocket, path):
    print('Игра началась!')
    await websocket.send(pieces)
    move = await websocket.recv()

# Запуск сервера WebSocket
async def main():
    server = await websockets.serve(handle_game, "localhost", 8765)
    await server.wait_closed()

player_count = 0  # Счетчик игроков
asyncio.run(main())
