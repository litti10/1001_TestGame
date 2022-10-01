from collections import deque

class BoardGame:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.board = [['.']*self.width for _ in range(self.height)]
        self.winner = None

    def set_stone(self):
        pass

    def print_board(self):
        for line in self.board:
            print(line)
        
        print('-'*self.width*5)
        
    def get_user_input(self, turn):
        stone = self.set_stone(turn)

        while True:
            try:
                self.user_input = list(input().split())
                if len(self.user_input) != 2:
                    raise ValueError('Only Enter Two Intergers!')
                if not self.user_input[0].isnumeric() or not self.user_input[1].isnumeric():
                    raise ValueError('Only Integer Can Be Used!')
                elif int(self.user_input[0])<0 or int(self.user_input[1])<0 or int(self.user_input[0])>self.height or int(self.user_input[1])>self.width:
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


class TicTacToe(BoardGame):
    def __init__(self):
        super().__init__(3,3)

    def set_stone(self,turn):
        if turn == 0:
            return 'O'
        if turn == 1:
            return 'X'
    
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

    def game_play(self):
        for turn in range(9):
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
    
        if self.winner is None:
            print('Tie!')

class Omok(BoardGame):
    def __init__(self):
        super().__init__(19,19)

    def set_stone(self,turn):
        if turn == 0:
            return '⚪'
        if turn == 1:
            return '⚫'
    
    def is_player_win(self, turn):
        stone = self.set_stone(turn)
        
        que = deque()
        y = int(self.user_input[0])
        x = int(self.user_input[1])
        que.append(self.board[y][x])

        # 가로줄 체크
        start_point = x
        left_point = start_point-1
        right_point = start_point+1

        # queue 안에 조건을 성립할 수 있는 돌들을 전부 삽입
        while len(que) != 9:
            # 9개의 돌이 전부 들어가는 경우 루프 종료
            if left_point > 0:
                que.appendleft(self.board[y][left_point])
                left_point -= 1
                # 왼쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if right_point < self.width:
                que.append(self.board[y][right_point])
                right_point += 1
                # 오른쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
        
        omok = []
        for idx in range (9):
            stone = 
        시작: 내가 마지막으로 input한 시점
        --> 우선 이 좌표를 가져와야 함, 여기서부터 시작
        경우의 수
        1. 확장했을 떄 range에 안 걸리는 경우
        2. 확장했을 떄 range에 걸리는 경우


    def game_play(self):
        for turn in range(9):
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
    
        if self.winner is None:
            print('Tie!')

# game = TicTacToe()
# game.game_play
# if game.winner is None:
#     print('Tie!')

game = Omok()
game.game_play()