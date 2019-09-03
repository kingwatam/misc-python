"""
Cookie Clicker Simulator
"""
try:
    import codeskulptor
    import simpleplot

    import user27_5LlszPPJxQHFMbk as codeskulptor_lib
    import user34_4ecfMGjlR5PTBqO as simplegui_lib
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import SimpleGUICS2Pygame.simpleplot as simpleplot

    import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib
    import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib

# Used to increase the timeout, if necessary
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
import math
import random
# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_num_cookies = 0.0
        self._current_num_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0 #cookies per second
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return str(["Time:", self._current_time, "Current Cookies:", self._current_num_cookies, "CPS:",  self._current_cps, "Total Cookies:", self._total_num_cookies])
         
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_num_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        waiting_time = math.ceil((cookies-self._current_num_cookies)/self._current_cps) # how many seconds to reach given number of cookies
        if self._current_num_cookies >= cookies:
            return 0.0
        else:
            return waiting_time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time <= 0:
            pass
        else:
            self._current_time += time
            self._current_num_cookies += time * self._current_cps
            self._total_num_cookies += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_num_cookies:
            pass
        elif item_name == None:
            pass
        else:
            self._current_num_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_num_cookies))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    #cloned_build_info = build_info.clone()
    clicker_state = ClickerState()    
    while clicker_state.get_time() <= duration:
        strategy_with_param = strategy(clicker_state.get_cookies(), 
                                       clicker_state.get_cps(), duration - clicker_state.get_time(), build_info)       
        if strategy_with_param == None:
            clicker_state.wait(duration - clicker_state.get_time())
            break
        else:
            if clicker_state.time_until(
                build_info.get_cost(strategy_with_param)) > duration - clicker_state.get_time():
                break
            elif clicker_state.time_until(
                build_info.get_cost(strategy_with_param)) <= duration - clicker_state.get_time():
                clicker_state.wait(clicker_state.time_until(build_info.get_cost(strategy_with_param)))
                clicker_state.buy_item(strategy_with_param, build_info.get_cost(strategy_with_param), 
                                       build_info.get_cps(strategy_with_param))
                build_info.update_item(strategy_with_param)
    if clicker_state.get_time() <= duration:
        clicker_state.wait(duration - clicker_state.get_time())
        strategy_with_param = strategy(clicker_state.get_cookies(), 
                                       clicker_state.get_cps(), duration - clicker_state.get_time(), build_info)       
        if strategy_with_param != None:
            clicker_state.buy_item(strategy_with_param, build_info.get_cost(strategy_with_param), 
                                   build_info.get_cps(strategy_with_param))
            build_info.update_item(strategy_with_param)
    return clicker_state


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """    
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    this strategy should always select the cheapest item that you can afford in the time left. 
    """  
    items = build_info.build_items()
    cheapest_cost = float("inf")
    for item in items: 
        if build_info.get_cost(item) < cheapest_cost:
            cheapest_cost = build_info.get_cost(item) 
            cheapest_item = item
    if cheapest_cost-cookies <= cps*time_left:
        return cheapest_item
    else:
        return None

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    this strategy should always select the most expensive item you can afford in the time left. 
    """
    items = build_info.build_items()
    priciest_cost = float("-inf")
    priciest_item = None
    for item in items: 
        if build_info.get_cost(item) > priciest_cost:
            # if we have enough cookies to buy item or if we have enough time left to get enough cookies to buy item
            if cookies >= build_info.get_cost(item) or priciest_cost-cookies <= cps*time_left:
                   priciest_cost = build_info.get_cost(item)
                   priciest_item = item
    return priciest_item

def strategy_best(cookies, cps, time_left, build_info):
    """
    this is the best strategy that you can come up with. 
    """
    items = build_info.build_items()
    cost_per_benefit = float("inf")
    for item in items: 
        # check whether ROI or cost per benefit is highest
        if build_info.get_cost(item) / build_info.get_cps(item) < cost_per_benefit:
            cost_per_benefit = build_info.get_cost(item) / build_info.get_cps(item)
            best_cost = build_info.get_cost(item)
            best_item = item
    if build_info.get_cost(item)-cookies <= cps*time_left:
        return best_item
    else:
        return None


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
   

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

run()
## test phase 1
##import testsuite
##testsuite.run_test(ClickerState)
## test phase 2
#import testsuite2
#testsuite2.run_tests(ClickerState, simulate_clicker, strategy_cursor)
#import testsuite3
#testsuite3.run_simulate_clicker_tests(simulate_clicker,strategy_none,strategy_cursor)
#testsuite3.run_clicker_state_tests(ClickerState)
