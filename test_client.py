import pytest, pygame
from unittest.mock import patch, Mock

from client import valid_move_rook, valid_move_bishop, warn_message
from client import rook_white, rook_black, pawn_white, bishop_black, bishop_white
from client import pawn_white, get_possible_moves, NotInPiecesError

def test_valid_move_rook_horizontal():
    '''Проверяем ход ладьи по горизонтали'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[4][3] = rook_white
    result = valid_move_rook(4, 3, 4, 7, pieces)
    assert result is True

def test_valid_move_rook_vertical():
    '''Проверяем ход ладьи по вертикали'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[6][5] = rook_black
    result = valid_move_rook(6, 5, 2, 5, pieces)
    assert result is True

def test_invalid_move_rook_blocked():
    '''Проверяем ход ладьи, если нельзя перескочить через свою фигуру'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[2][4] = rook_white
    pieces[4][4] = pawn_white
    result = valid_move_rook(2, 4, 5, 4, pieces)
    assert result is False

def test_invalid_move_rook_same_color_piece():
    '''Проверяем ход ладьи, если там своя фигура'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[3][1] = rook_black
    pieces[3][5] = rook_black
    result = valid_move_rook(3, 1, 3, 5, pieces)
    assert result is False

def test_valid_move_bishop_diagonal():
    '''Проверяем ход слона по диагонали'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[3][4] = bishop_white
    result = valid_move_bishop(3, 4, 7, 8, pieces)
    assert result is True

def test_invalid_move_bishop_blocked():
    '''Проверяем ход слона, если он невозможен'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[2][3] = bishop_black
    pieces[5][6] = pawn_white
    result = valid_move_bishop(2, 3, 6, 7, pieces)
    assert result is False

def test_invalid_move_bishop_same_color_piece():
    '''Проверяем ход слона, если он невозможен из-за своей фигуры'''
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[4][2] = bishop_black
    pieces[6][4] = bishop_black
    result = valid_move_bishop(4, 2, 7, 5, pieces)
    assert result is False


def test_function_raises_error():
    '''Проверка функции get_possible_moves на вызов ошибки'''
    with pytest.raises(NotInPiecesError):
        get_possible_moves(11,8)

"""
def test_warn_message_fill():
    screen_mock = Mock()
    font_medium_mock = Mock()
    pygame_mock = Mock()
    WIDTH = 800
    HEIGHT = 600

    with patch('pygame.font.Font.render') as mock_font_render:
        warn_message(screen_mock, font_medium_mock, WIDTH, HEIGHT, pygame_mock)
        
        # Проверяем, что метод fill был вызван с правильными параметрами
        screen_mock.fill.assert_called_once_with((200, 200, 200))
"""
