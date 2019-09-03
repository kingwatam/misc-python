'''
An implementation of solitaire Mancala
'''

class SolitaireMancala:
    '''
    An implementation of solitaire Mancala
    '''
    def __init__(self):
        '''
        Create a SolitaireMancala object whose configuration consists of 
        a board with an empty store and no houses (i.e; the configuration [0]). 
        '''
        self._board = [0]
    def set_board(self, configuration):
        '''
        Set the board to be a copy of the supplied configuration (to avoiding referencing issues). 
        The configuration will be a list of integers in the form described above.  
        '''
        self._board = list(configuration)
    def __str__(self):
        '''
        Return a string corresponding to the current configuration of the Mancala board. 
        This string is formatted as a list with the store appearing in the rightmost (last) entry. 
        Consecutive entries should be separated by a comma and blank (as done by Python when converting a list to a string). 
        '''
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    def get_num_seeds(self, house_num):
        ''' Return the number of seeds in the house with index house_num. 
        Note that house 0 corresponds to the store. 
        '''
        return self._board[house_num]
    def is_legal_move(self, house_num):
        '''Return True if moving the seeds from house house_num is legal. Otherwise, return False. 
        If house_num is zero, is_legal_move should return False. 
        '''
        if house_num > 0 and house_num < len(self._board):
            if self.get_num_seeds(house_num) == house_num:
                return True
        return False
    def apply_move(self, house_num):
        ''' Apply a legal move for house house_num to the board.
        '''
        if self.is_legal_move(house_num):
            for index in range(house_num - 1, -1, -1):
                self._board[index] += 1
            self._board[house_num] = 0

    def choose_move(self):
        '''
        Return the index for the legal move whose house is closest to the store. 
        If no legal move is available, return 0. 
        '''
        for index in range(1,len(self._board)):
            if self.is_legal_move(index):
                return index
        return 0
    def is_game_won(self):
        '''
        Return True if all houses contain no seeds. Return False otherwise. 
        '''
        sum_of_seeds = 0
        for dummy_n in range(1,len(self._board)):
            sum_of_seeds += self._board[dummy_n]
        return sum_of_seeds == 0
    def plan_moves(self):
        '''
        Given a Mancala game, return a list of legal moves computed to win the game if possible. 
        In computing this sequence, the method repeatedly chooses the move whose house is closest to the store when given a choice of legal moves. 
        Note that this method should not update the current configuration of the game. 
        '''       
        move_list = []
        temp = list(self._board)
        while self.choose_move() != 0:
            move_list.append(self.choose_move())
            self.apply_move(self.choose_move())
        self.set_board(temp)
        return move_list
    
import poc_mancala_testsuite
poc_mancala_testsuite.run_test(SolitaireMancala)

# import GUI code
import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())
