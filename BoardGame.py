from collections import deque
import pygame
import math
import gui
from gui import GUI

print('boardgame.py')

class BoardGame:
    def __init__(self, width, height, px_height):
        self.width = width
        self.height = height
        self.px_height = px_height
        
        self.maxPlayerTurn = self.width*self.height
        self.board = [['.']*self.width for _ in range(self.height)]
        self.winner = None
        self.turn = 0

    def initialize_grid(self):
        dis_to_cen =  self.px_height // self.height // 2

        # Initializing the array
        self.game_array = [[None]*self.width for _ in range(self.height)]
        
        for h in range(len(self.game_array)):
            for w in range(len(self.game_array[h])):
                x = dis_to_cen * (2 * w + 1)
                y = dis_to_cen * (2 * h + 1)

                # Adding centre coordinates
                self.game_array[h][w] = (x, y, "", True)

        return self.game_array

    def get_stone(self):
        pass

    # def print_board(self):
    #     for line in self.board:
    #         print(line)
        
    #     print('-'*self.width*5)
        
    # def get_user_input(self, turn):
    #     stone = self.get_stone(turn)

    #     while True:
    #         try:
    #             self.user_input = list(input().split())
    #             if len(self.user_input) != 2:
    #                 raise ValueError('Only Enter Two Intergers!')
    #             if not self.user_input[0].isnumeric() or not self.user_input[1].isnumeric():
    #                 raise ValueError('Only Integer Can Be Used!')
    #             elif int(self.user_input[0])<0 or int(self.user_input[1])<0 or int(self.user_input[0])>=self.height or int(self.user_input[1])>=self.width:
    #                 raise ValueError('Location Out of Range!')
    #             elif self.board[int(self.user_input[1])][int(self.user_input[0])] != '.':
    #                 raise ValueError('Enter an Empty Space!')
    #         except ValueError as e:
    #             print (e)
            
    #         else:
    #             self.board[int(self.user_input[1])][int(self.user_input[0])] = stone
    #             break

    def is_player_win(self):
      print("구현이 필요합니다")
      exit()

    def is_player_drawn(self):
        print("구현이 필요합니다")
        exit()

    def game_play(self):
        print("구현이 필요합니다")
        exit()
        
# if game.winner is None:
#     print('Tie!')
