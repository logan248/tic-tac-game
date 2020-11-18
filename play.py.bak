from inputs import read_text, menu_selector
from tic_tac import *
from random import randint

game_board = [' ' for i in range(9)]

menu = """
Tic Tac Toe (XO)
1.Single player
2.Multiplayer
Choose: """

option = menu_selector(menu, min_value=1, max_value=2)
if option == 1:
    pass
elif option == 2:
    game = TicTac()
    player1 = read_text('Player1 name: ')
    player2 = read_text('Player2 name: ')
    player_turn = player1
    player_input = 'X'
    game.draw_board(game_board)
    for i in range(9):
        print(f"{player_turn}'s turn")
        game.move(game_board, player_input)
        game.draw_board(game_board)
        if i == 8:
            print('Tie Game')
            break
        elif i >= 4:
            win = game.check(game_board, player_input)
            if win:
                print(f'{player_turn} has won the game')
                break
        if player_input == 'X':
            player_turn = player2
            player_input = 'O'
        else:
            player_input = 'X'
            player_turn = player1
