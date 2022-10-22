from boardgame import BoardGame


class Omok(BoardGame):
    def __init__(self):
        super().__init__(19,19)
        self.stone = {
            0:'⚪',
            1:'⚫'
            }

    def get_stone(self,turn):
        return self.stone[turn]
    
    def is_player_win(self, turn):
        stone = self.get_stone(turn)
        que = []
        y = int(self.user_input[0])
        x = int(self.user_input[1])
        que.append(self.board[y][x])

        #----------- 가로줄 체크 -----------
        start_point = x
        left_point = start_point-1
        right_point = start_point+1

        # queue 안에 조건을 성립할 수 있는 돌들을 전부 삽입
        while len(que) != 9:
            CHANGE = False
            # 9개의 돌이 전부 들어가는 경우 루프 종료
            if left_point >= 0:
                que = list(self.board[y][left_point]) + que
                left_point -= 1
                CHANGE = True
                # 왼쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if right_point < self.width:
                que = que + list(self.board[y][right_point])
                right_point += 1
                CHANGE = True
                # 오른쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if not CHANGE:
                break
                # 돌을 아예 추가할 수 없는 상황이면 강제로 종료
        print(que)
        if self.is_omok(que, stone):
            self.winner = turn
            return True
        
        #----------- 세로줄 체크 -----------
        que = []
        que.append(self.board[y][x])
        
        up_point = y-1
        down_point = y+1

        # queue 안에 조건을 성립할 수 있는 돌들을 전부 삽입
        while len(que) != 9:
            CHANGE = False
            # 9개의 돌이 전부 들어가는 경우 루프 종료
            if up_point >= 0:
                que = list(self.board[up_point][x]) + que
                up_point -= 1
                CHANGE = True
                # 위의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if down_point < self.width:
                que = que + list(self.board[down_point][x])
                down_point += 1
                CHANGE = True
                # 아래의 범위에 벗어나지 않는 경우 queue의 오른쪽에 돌을 추가
            if not CHANGE:
                break
                # 돌을 아예 추가할 수 없는 상황이면 강제로 종료
        print(que)
        if self.is_omok(que, stone):
            self.winner = turn
            return True
        #----------- 왼쪽 아래부터 오른쪽 위 대각선 체크줄 체크 -----------
        que = []
        que.append(self.board[y][x])

        start_point_up_y = y+1
        start_point_up_x = x+1
        start_point_down_y = y-1
        start_point_down_x = x-1

        # queue 안에 조건을 성립할 수 있는 돌들을 전부 삽입
        while len(que) != 9:
            CHANGE = False
            # 9개의 돌이 전부 들어가는 경우 루프 종료
            if start_point_down_y >= 0 and start_point_down_x >= 0:
                que = list(self.board[start_point_down_y][start_point_down_x]) + que
                start_point_down_y -= 1
                start_point_down_x -= 1
                CHANGE = True
                # 왼쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if start_point_up_y < self.width and start_point_up_x < self.width:
                que = que + list(self.board[start_point_up_y][start_point_up_x])
                start_point_up_y += 1
                start_point_up_x += 1
                CHANGE = True
                # 오른쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가

            if not CHANGE:
                break
                # 돌을 아예 추가할 수 없는 상황이면 강제로 종료
        print(que)
        if self.is_omok(que, stone):
            self.winner = turn
            return True
        #----------- 오른쪽 아래부터 왼쪽 위 대각선줄 체크 -----------
        que = []
        que.append(self.board[y][x])
        
        start_point_up_y = y+1
        start_point_up_x = x-1
        start_point_down_y = y-1
        start_point_down_x = x+1
        # queue 안에 조건을 성립할 수 있는 돌들을 전부 삽입
        while len(que) != 9:
            CHANGE = False
            # 9개의 돌이 전부 들어가는 경우 루프 종료
            if start_point_down_y >= 0 and start_point_down_x < self.width:
                que = list(self.board[start_point_down_y][start_point_down_x]) + que
                start_point_down_y -= 1
                start_point_down_x += 1
                CHANGE = True
                # 왼쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if start_point_up_y < self.height and start_point_up_x >= 0:
                que = que + list(self.board[start_point_up_y][start_point_up_x])
                start_point_up_y += 1
                start_point_up_x -= 1
                CHANGE = True
                # 오른쪽의 범위에 벗어나지 않는 경우 queue의 왼쪽에 돌을 추가
            if not CHANGE:
                break
                # 돌을 아예 추가할 수 없는 상황이면 강제로 종료
        print(que)
        
        if self.is_omok(que, stone):
            self.winner = turn
            return True

        return False

    def is_omok(self, que, stone):
        row = 0
        max_row = -1
        for idx in range(len(que)):
            if que[idx] == stone:
                row += 1
                max_row = max(max_row, row)
            else:
                row = 0
        if max_row == 5:
            return True
        else:
            return False
        
game = Omok()
game.game_play()