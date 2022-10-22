from collections import deque

class BoardGame:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.maxPlayerTurn = self.width*self.height
        self.board = [['.']*self.width for _ in range(self.height)]
        self.winner = None

    def initialize_grid(self):
        dis_to_cen = self.width // self.height // 2

        # Initializing the array
        game_array = [[None]*self.width for _ in range(self.height)]
        
        for h in range(len(game_array)):
            for w in range(len(game_array[h])):
                x = dis_to_cen * (2 * w + 1)
                y = dis_to_cen * (2 * h + 1)

                # Adding centre coordinates
                game_array[h][w] = (x, y, "", True)

        return game_array

    def get_stone(self):
        pass

    def print_board(self):
        for line in self.board:
            print(line)
        
        print('-'*self.width*5)
        
    def get_user_input(self, turn):
        stone = self.get_stone(turn)

        while True:
            try:
                self.user_input = list(input().split())
                if len(self.user_input) != 2:
                    raise ValueError('Only Enter Two Intergers!')
                if not self.user_input[0].isnumeric() or not self.user_input[1].isnumeric():
                    raise ValueError('Only Integer Can Be Used!')
                elif int(self.user_input[0])<0 or int(self.user_input[1])<0 or int(self.user_input[0])>=self.height or int(self.user_input[1])>=self.width:
                    raise ValueError('Location Out of Range!')
                elif self.board[int(self.user_input[1])][int(self.user_input[0])] != '.':
                    raise ValueError('Enter an Empty Space!')

            except ValueError as e:
                print (e)
            
            else:
                self.board[int(self.user_input[1])][int(self.user_input[0])] = stone
                break

    def is_player_win(self, turn):
      pass

    def game_play(self):
        for turn in range(self.maxPlayerTurn):
            self.print_board()
            self.get_user_input(turn%2)

            if self.is_player_win(turn%2):
                if self.winner == 0:
                    player = 'Player1'
                elif self.winner == 1:
                    player = 'Player2'
                self.print_board()
                print(player + " has won!")
                break


# game = TicTacToe()
# game.game_play
# if game.winner is None:
#     print('Tie!')
