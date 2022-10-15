import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(N)] for j in range(N)]
        self.init()
    def init(self):
        N = self.N
        M = self.M
        tmp = [1] * M + [0] * (N ** 2 - M)
        random.shuffle(tmp)
        #print(tmp)
        tmp_pole = [[0] * (N + 2)]
        while tmp != []:
            tmp_pole.append([0] + tmp[:N] + [0])
            tmp = tmp[N:]
        tmp_pole.append([0] * (N + 2))
        #print(tmp_pole)
        pole = [[[0] for i in range(N)] for j in range(N)]
        # print(pole)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                k = sum([tmp_pole[i - 1][j - 1], tmp_pole[i - 1][j], tmp_pole[i - 1][j + 1], tmp_pole[i][j - 1], tmp_pole[i][j + 1], tmp_pole[i + 1][j - 1], tmp_pole[i + 1][j], tmp_pole[i + 1][j + 1]])
                tmp = Cell(k, tmp_pole[i][j])
                pole[i - 1][j - 1] = tmp
        #print(pole)
        self.pole = pole

    def show(self):
        N = len(self.pole)
        for i in range(N):
            for j in range(N):
                if self.pole[i][j].fl_open:
                    if self.pole[i][j].mine:
                        print('*', end=' ')
                    else:
                        print(self.pole[i][j].around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()
    def show_all(self):
        N = len(self.pole)
        for i in range(N):
            for j in range(N):
                if True:
                    if self.pole[i][j].mine:
                        print('*', end=' ')
                    else:
                        print(self.pole[i][j].around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()
        
        
pole_game = GamePole(10, 12)
#pole_game.show()
#pole_game.show_all()
