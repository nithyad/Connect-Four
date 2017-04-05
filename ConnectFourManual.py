class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        
        s += '\n'

        # and the numbers underneath here
        for i in range(W):
            s += ' ' + str(i)
        
        return s       # the board is complete, return it
        
    def addMove(self, col, ox):
        """makes the move by dropping a checker on the board"""
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, col):
        """True if col is in-bounds + open and else false"""
        H = self.height
        W = self.width
        D = self.data
        if col < 0 or col >= W:
            return False
        elif D[0][col] != ' ':
            return False
        else:
            return True
    
    def isFull(self):
        for x in range(self.width):
            if self.allowsMove(x) == True:
                return False
        return True

    def delMove(self, col):
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                break
    
    def winsFor(self, ox):
        """ returns True if four checkers of type ox are in a row 
            returns False otherwise
        """

        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row][col+1] == ox and \
                   D[row][col+2] == ox and \
                   D[row][col+3] == ox:
                    return True
        
        for row in range(0,H-3):
            for col in range(0,W):
                if D[row][col] == ox and \
                   D[row+1][col] == ox and \
                   D[row+2][col] == ox and \
                   D[row+3][col] == ox:
                    return True

        
        for row in range(0,H-3):
            for col in range(0,W-3):
                if D[row][col] == ox and \
                   D[row+1][col+1] == ox and \
                   D[row+2][col+2] == ox and \
                   D[row+2][col+3] == ox:
                    return True
            
        for row in range(0,H-3):
            for col in range(3,W):
                if D[row][col] == ox and \
                   D[row+1][col-1] == ox and \
                   D[row+2][col-2] == ox and \
                   D[row+3][col-3] == ox:
                    return True
        
        return False


    def hostGame(self):
        """ Play Game
        """
        print("Welcome to Connect Four!!!")
        while self.isFull() == False:
            
            print(self)
            users_col = int(input("Please choose a Column: "))
            while self.allowsMove( users_col ) == False:
                users_col = int(input("Please choose a column: "))
            self.addMove(users_col, 'X')
            if self.winsFor('X') == True: 
                print("X wins sorry O")
                break
           
            print(self)
            users_col = int(input("Please choose a Column: "))
            while self.allowsMove( users_col ) == False:
                users_col = int(input("Please choose a column: "))
            self.addMove(users_col, 'O')
            if self.winsFor('O') == True: 
                print("O wins Sorry O")
                break
        print("Game Over")
    




    # def inarow_Neast(self, ch, r_start, c_start, A, N):
    #     """check to see if there is a three in the row east from A[r_start][c_start]"""
    #     h = len(A)
    #     w = len(A[0])
    #     h = len(A)
    #     w = len(A[0])
    #     if r_start < 0:
    #         return False
    #     if r_start >= h:
    #         return False
    #     if c_start < 0:
    #         return False
    #     if c_start+ N-1 >= w:
    #         return False
        
    #     for i in range(N):
    #         if A[r_start][c_start+i] != ch:
    #             return False
    #     return True
    
    # def inarow_Nsouth( self, ch, r_start, c_start, A, N):
    #     """check to see if there is a three in the row east from A[r_start][c_start]"""
    #     h = len(A)
    #     w = len(A[0])
    #     h = len(A)
    #     w = len(A[0])
    #     if r_start < 0:
    #         return False
    #     if r_start >= h:
    #         return False
    #     if c_start < 0:
    #         return False
    #     if c_start+ N-1 >= w:
    #         return False
        
    #     for i in range(N):
    #         if A[r_start + i][c_start] != ch:
    #             return False
    #     return True
    
    # def inarow_Nsoutheast( self, ch, r_start, c_start, A, N):
    #     """check to see if there is a three in the row east from A[r_start][c_start]"""
    #     h = len(A)
    #     w = len(A[0])
    #     h = len(A)
    #     w = len(A[0])
    #     if r_start < 0:
    #         return False
    #     if r_start >= h:
    #         return False
    #     if c_start < 0:
    #         return False
    #     if c_start+ N-1 >= w:
    #         return False
        
    #     for i in range(N):
    #         if A[r_start + i][c_start + i] != ch:
    #             return False
    #     return True
    
    # def inarow_Nnortheast(self, ch, r_start, c_start, A, N):
    #     """check to see if there is a three in the row east from A[r_start][c_start]"""
    #     h = len(A)
    #     w = len(A[0])
    #     if r_start < 0:
    #         return False
    #     if r_start >= h:
    #         return False
    #     if c_start < 0:
    #         return False
    #     if c_start+ N-1 >= w:
    #         return False
        
    #     for i in range(N):
    #         if A[r_start - i][c_start + i] != ch:
    #             return False
    #     return True
    
    # def winsFor (self, ox) :
    #     for i in range(self.height):
    #         for j in range(self.width):
    #                 if self.inarow_Nnortheast(ox, i, j, self.data, 4) \
    #                 or self.inarow_Nsoutheast(ox, i, j, self.data, 4) \
    #                 or self.inarow_Neast(ox, i, j, self.data, 4) \
    #                 or self.inarow_Nsouth(ox, i, j, self.data, 4) :
    #             #     return True;
    #             # if self.inarow_Nnortheast(ox, i, j, self.data, 4) == True or self.inarow_Nsoutheast(ox, i, j, self.data, 4) == True or self.inarow_Neast(ox, i, j, self.data 4) == True or self.inarow_Nsouth(ox, i, j, self.data, 4) == True:
    #                     return True
    #     return False
    
    def hostGame (self) :
        print("Welcome to Connect Four")
        print(self)
        while True:
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("X: Please choose a column!: ")
            self.addMove(users_col, "X")
            print(self)
            if self.winsFor("X") :
                print("X wins!!!! Sorry O")
                return
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = input("O: Choose a column: ")
            self.addMove(users_col, "O")
            print(self)
            if self.winsFor("O") :
                print("O wins!!!! Sorry X")
                return
            elif self.isFull() :
                print("Tie (yay for both!!!)")
                return


# def winsFor(self, ox):
#     """does ox win?"""
#     H = self.height
#     W = self.width
#     D = self.data
#     for row in range(H):
#         for col in range(W):
#             if D[row][col] < 0:
#                 return False
#             if D[row][col] >= H:
#                 return False
#             if c_start < 0:
#                 return False
#             if c_start + 3 >= W:
#                 return False
            
#             for i in range(4):
#                 if D[r_start][c_start+i] != ox:
#                     return False

#             for i in range(4):
#                 if D[r_start + i][c_start] != ox:
#                     return False
            
#             for i in range(4):
#                 if D[r_start + i][c_start + i] != ox:
#                     return False

#             for i in range(4):
#                 if D[r_start - i][c_start + i] != ox:
#                     return False
    
#     return True