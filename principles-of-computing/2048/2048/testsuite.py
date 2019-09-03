"""
A simple testing suite for 2048
"""

import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def run_test(game_class, function):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test merge() method    
    suite.run_test(function([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1a: merge")
    suite.run_test(function([0, 0, 2, 2] ), [4, 0, 0, 0], "Test #1b: merge")
    suite.run_test(function([2, 2, 0, 0] ), [4, 0, 0, 0], "Test #1c: merge")
    suite.run_test(function([2, 2, 2, 2] ), [4, 4, 0, 0], "Test #1d: merge")
    suite.run_test(function([8, 16, 16, 8]), [8, 32, 8, 0], "Test #1e: merge")
        
    # test __str__ method
    game = game_class(3,3)
    suite.run_test(game.__str__(), "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]", "Test #2: __str__")

    # test set_tile method
    game.set_tile(0,0,1)
    game.set_tile(0,1,2)
    game.set_tile(0,2,3)
    game.set_tile(1,0,4)
    game.set_tile(1,1,5)
    game.set_tile(1,2,6)
    game.set_tile(2,0,7)
    game.set_tile(2,1,8)
    game.set_tile(2,2,9)
    suite.run_test(game.__str__(), "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]", "Test #3: set_tile")

    # test get_tile method
    suite.run_test(game.get_tile(0,0), 1, "Test #4a: get_tile")
    suite.run_test(game.get_tile(1,2), 6, "Test #4b: get_tile")
    suite.run_test(game.get_tile(2,1), 8, "Test #4c: get_tile")

    # test new_tile method
    game.reset()
    game.new_tile()
    print game.__str__()

    # test move method
    game.set_tile(0,0,4)
    game.set_tile(0,1,2)
    game.set_tile(0,2,2)
    game.set_tile(1,0,0)
    game.set_tile(1,1,0)
    game.set_tile(1,2,2)
    game.set_tile(2,0,4)
    game.set_tile(2,1,2)
    game.set_tile(2,2,2)
    print game.__str__()
    game.move(UP)
    print game.__str__(), "up"
    game.move(DOWN)
    print game.__str__()
    game.move(LEFT)
    print game.__str__()
    game.move(RIGHT)
    print game.__str__()

    # report number of tests and failures
    suite.report_results()
