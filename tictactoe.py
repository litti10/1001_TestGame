from boardgame import BoardGame
from gui import GUI
import pygame

class TicTacToe(BoardGame):
    def __init__(self):
        super().__init__(3,3)
        self.gui = GUI()
        self.board = self.initialize_grid()

    def get_stone(self,turn):
        if turn == 0:
            return 'O'
        if turn == 1:
            return 'X'
    
    def is_player_win(self, turn):
        stone = self.get_stone(turn)
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
    
    def game_play(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click(self.board)

                    
game = TicTacToe()
game.game_play()