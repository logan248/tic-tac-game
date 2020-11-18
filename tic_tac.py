from inputs import menu_selector


class TicTac(object):
    def draw_board(self, board):
        template = f"""
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    """
        print(template)

    def move(self, board, player_input):
        not_occupied = True
        while not_occupied:
            prompt = 'Which move(1-9): '
            cell = menu_selector(prompt, min_value=1, max_value=9)
            cell -= 1
            if board[cell] == ' ':
                board[cell] = player_input
                not_occupied = False
            else:
                print('Cell occupied!\nSorry, choose another cell!')

    def check(self, board, item):
        if board[0] == board[1] == board[2] == item:
            return True
        if board[3] == board[4] == board[5] == item:
            return True
        if board[6] == board[7] == board[8] == item:
            return True
        if board[0] == board[3] == board[6] == item:
            return True
        if board[1] == board[4] == board[7] == item:
            return True
        if board[2] == board[5] == board[8] == item:
            return True
        if board[0] == board[4] == board[8] == item:
            return True
        if board[2] == board[4] == board[6] == item:
            return True
