import random
from custom_exceptions import CellOcupiedError


class TicTacGame:

    def __init__(self, n):
        self.n = n
        self.cells = [[j + i * n for j in range(1, n + 1)] for i in range(n)]

    def show_board(self):
        for row in self.cells:
            for string in row:
                print(string, end='\t')
            print()

    def validate_input(self, player_choice, curr_player):
        player_choice = int(player_choice)
        if player_choice > self.n * self.n:
            raise IndexError

        fl_put = False
        for i in range(self.n):
            if player_choice in self.cells[i]:
                indx = self.cells[i].index(player_choice)
                self.cells[i][indx] = curr_player
                fl_put = True

        if not fl_put:
            raise CellOcupiedError('Выбранная клетка занята!')

    def start_game(self, mode='1 vs 1'):
        self.show_board()
        curr_player = 'X'
        count_moves = 0

        while count_moves < self.n * self.n:
            print()
            print(f'В какую клетку поставить {curr_player} ')
            player_choice = input() if mode == '1 vs 1' else self.lst_moves.pop(
                self.lst_moves.index(random.choice(self.lst_moves)))

            try:
                self.validate_input(player_choice, curr_player)

            except ValueError:
                print('Номер клетки должен быть числом, введите его еще раз!')
                continue
            except IndexError:
                print(
                    f'Выбранный номер клетки больше, чем общее число клеток в поле {self.n} x {self.n},'
                    f' введите его еще раз!')
                continue
            except CellOcupiedError:
                print('Выбранная клетка занята, введите номер клетки еще раз!')
                continue
            
            else:
                self.show_board()
                count_moves = count_moves + 1
                if self.check_winner(count_moves, curr_player):
                    return True
                curr_player = '0' if curr_player == 'X' else 'X'

    def check_winner(self, count_moves, curr_player):
        diag_right = []
        diag_left = []
        k = 1
        for i in range(len(self.cells)):
            raws = []
            for j in range(len(self.cells)):
                raws.append(self.cells[j][i])
                if i == j:
                    diag_right.append(self.cells[i][j])
                if j == len(self.cells) - k:
                    diag_left.append(self.cells[i][j])
            k = k + 1
            if len(set(raws)) == 1 or len(set(self.cells[i])) == 1:
                print(f'Игрок c {curr_player} выиграл!')
                return True

        if len(set(diag_right)) == 1 or len(set(diag_left)) == 1:
            print(f'Игрок c {curr_player} выиграл!')
            return True
       
        if count_moves == self.n * self.n:
            print('Ничья')
            return None

    def mode_comp_vs_comp(self):
        self.lst_moves = [i for i in range(1, (self.n * self.n) + 1)]
        return self.start_game(mode='comp vs comp')


if __name__ == '__main__':
    try:
        game = TicTacGame(int(input('Введите размер поля: ')))

    except ValueError:
        print('Вы неправильно задали размер игрового поля, оно должно быть числом, введите еще раз!')

    else:
        game.start_game()
