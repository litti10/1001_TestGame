from boardgame import BoardGame
from gui import GUI
# from main import display_message
import pygame

print('tictactoe.py')

class TicTacToe(BoardGame):
    def __init__(self):
        super().__init__(3,3, 300)
        self.board = self.initialize_grid()
        self.gui = GUI(self.game_array,300)
        self.turn = 0
        self.winner = None
        self.winner_dict = {'0':'player1', '1':'player2'}
        print('생성자 생성 완료')

    def get_stone(self):
        if self.turn%2 == 0:
            return 'x'
        if self.turn%2 == 1:
            return 'o'
    
    def is_player_win(self):
        stone = self.get_stone()
        for num in range(3):
            if self.board[num][0][2] == stone and self.board[num][1][2] == stone and self.board[num][2][2] == stone:
                self.winner = self.winner_dict[str(self.turn%2)]
                return True
            if self.board[0][num][2] == stone and self.board[1][num][2] == stone and self.board[2][num][2] == stone:
                self.winner = self.winner_dict[str(self.turn%2)]
                return True
        if self.board[0][0][2] == stone and self.board[1][1][2] == stone and self.board[2][2][2] == stone:
            self.winner = self.winner_dict[str(self.turn%2)]
            return True
        if self.board[0][2][2] == stone and self.board[1][1][2] == stone and self.board[2][0][2] == stone:
            self.winner = self.winner_dict[str(self.turn%2)]
            return True
        return False

    def game_play(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.gui.click():
                        if self.is_player_win():
                            run = False
                        elif self.turn == 8:
                            run = False
                        if run:
                            self.turn += 1
            self.gui.render()

        if self.winner != None:
            self.gui.display_message(self.winner+' has won!')
        elif self.turn == 8:
            self.gui.display_message('Draw!')

while True:
    game = TicTacToe()
    game.game_play()