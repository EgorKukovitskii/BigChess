import asyncio, sys
import websockets
import pygame

# Инициализация Pygame
pygame.init()

# Определение цветов
LIGHT_SQUARE = (240, 217, 181)  # Светлая клетка
DARK_SQUARE = (181, 136, 99)   # Темная клетка
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (50, 150, 50)
BLUE = (50, 50, 150)

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Шрифты
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)

# Размеры и количество клеток на игровой доске
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шахматы 10x10')

def warn_message(message):
    global button_exit_rect, button_retry_rect
    screen.fill(GRAY)

    # Вывод сообщения о разрыве соединения
    text = font_medium.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text, text_rect)

    pygame.display.flip()
    
def draw_lobby():
    global button_rect
    screen.fill(GRAY)

    # Надпись "Шахматы 10 на 10"
    text = font_large.render("Шахматы 10 на 10", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text, text_rect)

    # Создание кнопки "Присоединиться к серверу"
    button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
    pygame.draw.rect(screen, GREEN, button_rect)
    text = font_medium.render("Присоединиться к серверу", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    pygame.display.flip()

def draw_board():
    global pieces
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

    pygame.display.flip()

# Инициализируем кнопки


    
draw_lobby()

async def play_chess():
    async with websockets.connect('ws://localhost:8765') as websocket:
        warn_message('Ожидаем соперника')
        while True:
            pygame.event.get()
            pieces = await websocket.recv()
            draw_board()
            
           

def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    try:
                        asyncio.run(play_chess())
                    except Exception as err:
                        print(err)
                        warn_message('Соединение разорвано. Возможно, сервер переполнен')
            

start()

pygame.quit()
