import pytest

from client import valid_move_rook, valid_move_bishop
from client import rook_white, rook_black, pawn_white, bishop_black, bishop_white
from client import pawn_white

def test_valid_move_rook_horizontal():
    # Testing a valid horizontal move for the rook
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[4][3] = rook_white
    result = valid_move_rook(4, 3, 4, 7, pieces)
    assert result is True

def test_valid_move_rook_vertical():
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[6][5] = rook_black
    result = valid_move_rook(6, 5, 2, 5, pieces)
    assert result is True

def test_invalid_move_rook_blocked():
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[2][4] = rook_white
    pieces[4][4] = pawn_white
    result = valid_move_rook(2, 4, 5, 4, pieces)
    assert result is False

def test_invalid_move_rook_same_color_piece():
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[3][1] = rook_black
    pieces[3][5] = rook_black
    result = valid_move_rook(3, 1, 3, 5, pieces)
    assert result is False

def test_valid_move_bishop_diagonal():
    # Testing a valid diagonal move for the bishop
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[3][4] = bishop_white
    result = valid_move_bishop(3, 4, 7, 8, pieces)
    assert result is True

def test_invalid_move_bishop_blocked():
    # Testing an invalid move for the bishop because it's blocked by a piece
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[2][3] = bishop_black
    pieces[5][6] = pawn_white
    result = valid_move_bishop(2, 3, 6, 7, pieces)
    assert result is False

def test_invalid_move_bishop_same_color_piece():
    # Testing an invalid move for the bishop due to a piece of the same color
    pieces = [[None for _ in range(10)] for _ in range(10)]
    pieces[4][2] = bishop_black
    pieces[6][4] = bishop_black
    result = valid_move_bishop(4, 2, 7, 5, pieces)
    assert result is False
