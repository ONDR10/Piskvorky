def undo(self) -> List[List[int]]:
        ''' Vráti jeden ťah späť '''
        if len(self.moves) >= 1:
            self.desk[self.moves[-1][0]][self.moves[-1][1]] = 0
            self.moves.pop(-1)
            return self.get_desk()