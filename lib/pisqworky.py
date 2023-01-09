from typing import List, Tuple

class Desk:
    def __init__(self) -> None:
        self.desk = list(list([0 for _ in range(15)]) for _ in range(15))
        self.moves = list()

        self.status = 0

    def move(self, x: int, y: int) -> bool:
        '''
        Zapíše číslo hráča na políčko ktoré klikol
        ak na danom políčku ešte nieje znak
        '''
        if self.desk[x][y] == 0:
            self.desk[x][y] = len(self.moves) % 2 + 1
            self.moves.append((x, y))
            return True
        else:
            return False

    def get_desk(self) -> List[List[int]]:
        '''
        Vráti 2D pole s int hodnotami hracích políčok
        (0 - prázdne políčko, 1 - hráč č. 1, 2 - hráč č.2)
        '''
        return self.desk

    def check_win(self) -> int:
        '''
        Skontroluje, či sa na doske nachádza výhra
        Vráti 0 ak nikto nevyhral alebo číslo hráča ak ktorý vyhral
        alebo -1 v prípade remízy
        '''
        for i in range(15):
            horizontal_sign = 0
            horizontal_counter = 0
            vertical_sign = 0
            vertical_counter = 0

            for j in range(15):                
                #horizontal
                if self.desk[i][j] == horizontal_sign: 
                    horizontal_counter += 1
                else: 
                    horizontal_counter = 1
                    horizontal_sign = self.desk[i][j]
                #vertical
                if self.desk[j][i] == vertical_sign: 
                    vertical_counter += 1
                else:
                    vertical_counter = 1
                    vertical_sign = self.desk[j][i]

                #counter
                if horizontal_counter >= 5 and horizontal_sign != 0:
                    return horizontal_sign
                elif vertical_counter >= 5 and vertical_sign != 0:
                    return vertical_sign

        for i in range(4, 15):
            diagonal_counter_1 = 0
            diagonal_sign_1 = 0
            diagonal_counter_2 = 0
            diagonal_sign_2 = 0
            diagonal_counter_3 = 0
            diagonal_sign_3 = 0
            diagonal_counter_4 = 0
            diagonal_sign_4 = 0
            for j in range(i+1):
                #diagonal_1
                if self.desk[i-j][j] == diagonal_sign_1:
                    diagonal_counter_1 += 1
                else:
                    diagonal_counter_1 = 1
                    diagonal_sign_1 = self.desk[i-j][j]

                #diagonal_2
                if self.desk[14-i+j][j] == diagonal_sign_2:
                    diagonal_counter_2 += 1
                else:
                    diagonal_counter_2 = 1
                    diagonal_sign_2 = self.desk[14-i+j][j]
                
                #diagonal_3
                if self.desk[14-i+j][14-j] == diagonal_sign_3:
                    diagonal_counter_3 += 1
                else:
                    diagonal_counter_3 = 1
                    diagonal_sign_3 = self.desk[14-i+j][14-j]
                
                #diagonal_4
                if self.desk[i-j][14-j] == diagonal_sign_4:
                    diagonal_counter_4 += 1
                else:
                    diagonal_counter_4 = 1
                    diagonal_sign_4 = self.desk[i-j][14-j]


                #counter
                if diagonal_counter_1 >= 5 and diagonal_sign_1 != 0:
                    return diagonal_sign_1
                if diagonal_counter_2 >= 5 and diagonal_sign_2 != 0:
                    return diagonal_sign_2
                if diagonal_counter_3 >= 5 and diagonal_sign_3 != 0:
                    return diagonal_sign_3
                if diagonal_counter_4 >= 5 and diagonal_sign_4 != 0:
                    return diagonal_sign_4

    def undo(self) -> List[List[int]]:
        ''' Vráti jeden ťah späť '''
        if len(self.moves) >= 1:
            self.desk[self.moves[-1][0]][self.moves[-1][1]] = 0
            self.moves.pop(-1)
            return self.get_desk()

    def restart(self) -> None:
        ''' Reštartuje hru '''
        self.__init__()

    def turn(self, x, y) -> Tuple[List[List[int]], int]:
        '''
        Spraví celý jeden ťah vrátane kontroly výhry
        a vrátenia pola, potencionálnej výhry a počet ťahov
        '''
        if not self.move(x, y):
            return (self.get_desk(), 0)
        else:
            self.status = self.check_win()
            return (self.get_desk(), self.status)

    def get_num_of_moves(self) -> int:
        ''' Vráti počet ťahov '''
        return len(self.moves)
