class TicTacToe:
    def __init__(self):
        self.board = [
            ['.','.','.'],
            ['.','.','.'],
            ['.','.','.']
        ]

        self.winner = None

    def print_board(self):
        for line in self.board:
            print(line)
        
        print('-'*15)

    def set_stone(self,turn):
        if turn == 0:
            return 'O'
        if turn == 1:
            return 'X'

    def get_user_input(self, turn):
        stone = self.set_stone(turn)

        while True:
            try:
                user_input = list(input().split())
                if len(user_input) != 2:
                    raise ValueError('Only Enter Two Intergers!')
                if not user_input[0].isnumeric() or not user_input[1].isnumeric():
                    raise ValueError('Only Integer Can Be Used!')
                elif int(user_input[0])<0 or int(user_input[1])<0 or int(user_input[0])>2 or int(user_input[1])>2:
                    raise ValueError('Location Out of Range!')
                elif self.board[int(user_input[1])][int(user_input[0])] != '.':
                    raise ValueError('Enter an Empty Space!')

            except ValueError as e:
                print (e)
            
            else:
                self.board[int(user_input[1])][int(user_input[0])] = stone
                break
    
    def is_player_win(self, turn):
        stone = self.set_stone(turn)
        for num in range(3):
            if self.board[num][0] == stone and self.board[num][1] == stone and self.board[num][2] == stone:
                self.winner = turn
                return True
            if self.board[0][num] == stone and self.board[1][num] == stone and self.board[2][num] == stone:
                self.winner = turn
                return True
        if self.board[0][0] == stone and self.board[1][1] == stone and self.board[2][2] == stone:
            self.winner = turn
            return True
        if self.board[0][2] == stone and self.board[1][1] == stone and self.board[2][0] == stone:
            self.winner = turn
            return True
        return False

game = TicTacToe()

for turn in range(9):
    game.print_board()
    game.get_user_input(turn%2)

    if game.is_player_win(turn%2):
        if game.winner == 0:
            player = 'Player1'
        elif game.winner == 1:
            player = 'Player2'
        game.print_board()
        print(player + " has won!")
        break
    
if game.winner is None:
    print('Tie!')
