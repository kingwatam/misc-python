"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 30    # Number of trials to run
MCMATCH = 1  # Score for squares played by the machine player
MCOTHER = 1  # Score for squares played by the other player

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4
    
# Add your functions here.
def mc_trial(board, player):
    """
    Takes current board and let next player move, alternate between players, return nothing when game is over
    """
    board_dim = board.get_dim()
    while board.check_win() is None:
        board.move(random.randrange(board_dim), random.randrange(board_dim), player)
        player = provided.switch_player(player)
    
def mc_update_scores(scores, board, player): 
    """
    Updates score grid (same dimension as game board) directly, and returns nothing
    """
    board_dim = board.get_dim()
    for dummy_col in range(board_dim):
        for dummy_row in range(board_dim):
            if board.check_win() == PLAYERX:
                if board.square(dummy_row, dummy_col) == PLAYERX:
                    scores[dummy_row][dummy_col] += MCMATCH
                if board.square(dummy_row, dummy_col) == PLAYERO:
                    scores[dummy_row][dummy_col] -= MCOTHER
            elif board.check_win() == PLAYERO:
                if board.square(dummy_row, dummy_col) == PLAYERX:
                    scores[dummy_row][dummy_col] -= MCMATCH
                if board.square(dummy_row, dummy_col) == PLAYERO:
                    scores[dummy_row][dummy_col] += MCOTHER

def get_best_move(board, scores):
    """
    Find all empty squares with max score, then randomly returns one of them as (row, col) tuple
    """
    empty_list = board.get_empty_squares()
    best_score = float('-inf')
    best_move = []
    # check for max value in scores
    for item in empty_list:
        if scores[item[0]][item[1]] >= best_score:
            best_score = scores[item[0]][item[1]] 
    # add items with same best_score
    for item in empty_list:
        if scores[item[0]][item[1]] == best_score:
            best_move.append(item)
    return random.choice(best_move)

def mc_move(board, player, trials):
    """
    takes current board, return best move
    """
    board_dim = board.get_dim()    
    scores = [[0 for _ in range(board_dim)] for _ in range(board_dim)]
    for _ in range(trials):
        board_clone = board.clone()
        player_clone = player
        mc_trial(board_clone, player_clone)
        mc_update_scores(scores, board_clone, player_clone)

    # need the current board instead of cloned board
    return get_best_move(board, scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(5, provided.PLAYERX, mc_move, NTRIALS, False)
