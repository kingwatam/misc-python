"""
Test suite for the ClickerState class.
"""

import poc_simpletest    
import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

def print_header(title):
    print ""
    print "--------------------------------------------------"    
    print title
    print "--------------------------------------------------"    

def simulate_clicker_with_cursor_strategy_test(simulate_clicker,strategy_cursor):
    """
    Tests for simulations using the cursor_strategy
    """
    
    print_header("Starting tests for strategy_cursor used by simulate_clicker")    
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
        
    state = simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_cursor)
    # using str() here since float number computation yields errors
    # e.g.: try this code:
    # 		print 0.1 + 0.2 == 0.3 
    # It will evaluate to False
    # see https://docs.python.org/2/tutorial/floatingpoint.html#representation-error
    suite.run_test(str(state.get_cookies()), "6965195661.5", "Test #1: state.get_cookies() after time=10000000000.0 does not equal 6965195661.5.\n")
    suite.run_test(str(state.get_cps()), "16.1", "Test #2: state.get_cps() after time=10000000000.0 does not equal 16.1. It seems that you do not buy the cursor items at the right time.\n")
    suite.run_test(str(state.get_time()), "10000000000.0", "Test #3: state.get_time() after time=10000000000.0 does not equal 10000000000.0. Did you forget to wait until the end of the duration at the end of the simulate_clicker method?\n")
    suite.run_test(str(state.get_history()), "[(0.0, None, 0.0, 0.0), (15.0, 'Cursor', 15.0, 15.0), (31.0, 'Cursor', 17.25, 32.6), (48.0, 'Cursor', 19.8375, 53.0), (65.0, 'Cursor', 22.813125, 75.1), (84.0, 'Cursor', 26.23509375, 101.7), (104.0, 'Cursor', 30.1703578125, 131.7), (126.0, 'Cursor', 34.6959114844, 166.9), (149.0, 'Cursor', 39.900298207, 206.0), (175.0, 'Cursor', 45.8853429381, 252.8), (203.0, 'Cursor', 52.7681443788, 306.0), (233.0, 'Cursor', 60.6833660356, 366.0), (266.0, 'Cursor', 69.785870941, 435.3), (303.0, 'Cursor', 80.2537515821, 516.7), (343.0, 'Cursor', 92.2918143194, 608.7), (387.0, 'Cursor', 106.135586467, 714.3), (436.0, 'Cursor', 122.055924437, 836.8), (490.0, 'Cursor', 140.364313103, 977.2), (550.0, 'Cursor', 161.418960069, 1139.2), (616.0, 'Cursor', 185.631804079, 1324.0), (690.0, 'Cursor', 213.476574691, 1538.6), (772.0, 'Cursor', 245.498060894, 1784.6), (863.0, 'Cursor', 282.322770028, 2066.7), (964.0, 'Cursor', 324.671185533, 2389.9), (1077.0, 'Cursor', 373.371863362, 2762.8), (1204.0, 'Cursor', 429.377642867, 3194.6), (1345.0, 'Cursor', 493.784289297, 3688.1), (1503.0, 'Cursor', 567.851932691, 4256.9), (1679.0, 'Cursor', 653.029722595, 4908.1), (1877.0, 'Cursor', 750.984180984, 5660.5), (2098.0, 'Cursor', 863.631808132, 6522.4), (2346.0, 'Cursor', 993.176579352, 7514.4), (2625.0, 'Cursor', 1142.15306625, 8658.3), (2938.0, 'Cursor', 1313.47602619, 9972.9), (3289.0, 'Cursor', 1510.49743012, 11482.2), (3684.0, 'Cursor', 1737.07204464, 13220.2), (4128.0, 'Cursor', 1997.63285134, 15218.2), (4627.0, 'Cursor', 2297.27777904, 17513.6), (5189.0, 'Cursor', 2641.86944589, 20155.0), (5822.0, 'Cursor', 3038.14986278, 23193.4), (6535.0, 'Cursor', 3493.87234219, 26687.1), (7339.0, 'Cursor', 4017.95319352, 30707.1), (8245.0, 'Cursor', 4620.64617255, 35327.7), (9267.0, 'Cursor', 5313.74309843, 40642.1), (10420.0, 'Cursor', 6110.8045632, 46753.0), (11721.0, 'Cursor', 7027.42524767, 53778.4), (13191.0, 'Cursor', 8081.53903483, 61863.4), (14850.0, 'Cursor', 9293.76989005, 71153.8), (16725.0, 'Cursor', 10687.8353736, 81841.3), (18844.0, 'Cursor', 12291.0106796, 94131.5), (21240.0, 'Cursor', 14134.6622815, 108267.9), (23949.0, 'Cursor', 16254.8616238, 124521.9), (27014.0, 'Cursor', 18693.0908673, 143218.4), (30481.0, 'Cursor', 21497.0544974, 164713.8), (34405.0, 'Cursor', 24721.612672, 189435.0), (38847.0, 'Cursor', 28429.8545728, 217863.8), (43877.0, 'Cursor', 32694.3327588, 250558.8), (49574.0, 'Cursor', 37598.4826726, 288159.0), (56027.0, 'Cursor', 43238.2550735, 331394.1), (63340.0, 'Cursor', 49723.9933345, 381122.5), (71627.0, 'Cursor', 57182.5923347, 438302.8), (81021.0, 'Cursor', 65759.9811849, 504060.8), (91673.0, 'Cursor', 75623.9783626, 579690.0), (103751.0, 'Cursor', 86967.575117, 666651.6), (117452.0, 'Cursor', 100012.711385, 766668.9), (132994.0, 'Cursor', 115014.618092, 881679.7), (150630.0, 'Cursor', 132266.810806, 1013949.7), (170644.0, 'Cursor', 152106.832427, 1166056.1), (193361.0, 'Cursor', 174922.857291, 1340977.0), (219151.0, 'Cursor', 201161.285885, 1542139.0), (248434.0, 'Cursor', 231335.478767, 1773474.7), (281689.0, 'Cursor', 266035.800582, 2039514.7), (319459.0, 'Cursor', 305941.17067, 2345451.7), (362366.0, 'Cursor', 351832.34627, 2697289.1), (411113.0, 'Cursor', 404607.198211, 3101889.2), (466506.0, 'Cursor', 465298.277942, 3567190.4), (529458.0, 'Cursor', 535093.019634, 4102282.4), (601011.0, 'Cursor', 615356.972579, 4717638.2), (682352.0, 'Cursor', 707660.518466, 5425304.9), (774830.0, 'Cursor', 813809.596236, 6239111.3), (879985.0, 'Cursor', 935881.035671, 7174990.8), (999570.0, 'Cursor', 1076263.19102, 8251255.8), (1135581.0, 'Cursor', 1237702.66967, 9488955.9), (1290294.0, 'Cursor', 1423358.07013, 10912315.5), (1466301.0, 'Cursor', 1636861.78064, 12549180.6), (1666555.0, 'Cursor', 1882391.04774, 14431568.2), (1894424.0, 'Cursor', 2164749.7049, 16596323.7), (2153743.0, 'Cursor', 2489462.16064, 19085786.1), (2448885.0, 'Cursor', 2862881.48473, 21948663.5), (2784835.0, 'Cursor', 3292313.70744, 25240973.5), (3167276.0, 'Cursor', 3786160.76356, 29027139.4), (3602684.0, 'Cursor', 4354084.87809, 33381219.4), (4098446.0, 'Cursor', 5007197.60981, 38388415.6), (4662983.0, 'Cursor', 5758277.25128, 44146693.0), (5305898.0, 'Cursor', 6622018.83897, 50768717.5), (6038140.0, 'Cursor', 7615321.66482, 58384034.3), (6872199.0, 'Cursor', 8757619.91454, 67141653.8), (7822319.0, 'Cursor', 10071262.9017, 77212925.8), (8904744.0, 'Cursor', 11581952.337, 88794873.3), (10138007.0, 'Cursor', 13319245.1875, 102114113.7), (11543249.0, 'Cursor', 15317131.9657, 117431251.5), (13144585.0, 'Cursor', 17614701.7605, 135045947.5), (14969532.0, 'Cursor', 20256907.0246, 155302859.2), (17049482.0, 'Cursor', 23295443.0783, 178598299.2), (19420257.0, 'Cursor', 26789759.54, 205388056.7), (22122733.0, 'Cursor', 30808223.471, 236196283.1), (25203556.0, 'Cursor', 35429456.9917, 271625747.6), (28715959.0, 'Cursor', 40743875.5404, 312369622.4), (32720699.0, 'Cursor', 46855456.8715, 359225080.4), (37287120.0, 'Cursor', 53883775.4022, 413108848.2), (42494376.0, 'Cursor', 61966341.7125, 475075194.6), (48432817.0, 'Cursor', 71261292.9694, 546336486.6), (55205584.0, 'Cursor', 81950486.9148, 628286967.3), (62930425.0, 'Cursor', 94243059.952, 722530027.5), (71741768.0, 'Cursor', 108379518.945, 830909546.4), (81793095.0, 'Cursor', 124636446.787, 955546001.2), (93259648.0, 'Cursor', 143331913.805, 1098877913.7), (106341529.0, 'Cursor', 164831700.875, 1263709614.3), (121267234.0, 'Cursor', 189556456.006, 1453266067.8), (138297697.0, 'Cursor', 217989924.407, 1671255994.2), (157730907.0, 'Cursor', 250688413.069, 1921944403.2), (179907190.0, 'Cursor', 288291675.029, 2210236082.2), (205215238.0, 'Cursor', 331535426.283, 2541771511.0), (234099006.0, 'Cursor', 381265740.226, 2923037248.6), (267065593.0, 'Cursor', 438455601.26, 3361492855.7), (304694245.0, 'Cursor', 504223941.448, 3865716792.5), (347646655.0, 'Cursor', 579857532.666, 4445574327.5), (396678726.0, 'Cursor', 666836162.566, 5112410493.1), (452654024.0, 'Cursor', 766861586.95, 5879272075.7), (516559156.0, 'Cursor', 881890824.993, 6761162897.3), (589521347.0, 'Cursor', 1014174448.74, 7775337352.2), (672828534.0, 'Cursor', 1166300616.05, 8941637970.2), (767952343.0, 'Cursor', 1341245708.46, 10282883677.1), (876574354.0, 'Cursor', 1542432564.73, 11825316233.3), (1000616134.0, 'Cursor', 1773797449.44, 13599113687.3), (1142273569.0, 'Cursor', 2039867066.86, 15638980751.3), (1304056130.0, 'Cursor', 2345847126.88, 17984827885.8), (1488831759.0, 'Cursor', 2697724195.92, 20682552069.2), (1699878210.0, 'Cursor', 3102382825.3, 23784934898.9), (1940941741.0, 'Cursor', 3567740249.1, 27352675157.7), (2216304243.0, 'Cursor', 4102901286.47, 31455576437.5), (2530860008.0, 'Cursor', 4718336479.44, 36173912912.5), (2890203515.0, 'Cursor', 5426086951.35, 41599999868.2), (3300729830.0, 'Cursor', 6239999994.05, 47839999856.2), (3769749438.0, 'Cursor', 7175999993.16, 55015999858.6), (4305619567.0, 'Cursor', 8252399992.14, 63268399845.2), (4917894405.0, 'Cursor', 9490259990.96, 72758659834.2), (5617496905.0, 'Cursor', 10913798989.6, 83672458834.2), (6416915302.0, 'Cursor', 12550868838.0, 96223327667.1), (7330427907.0, 'Cursor', 14433499163.7, 110656826826.0), (8374360237.0, 'Cursor', 16598524038.3, 127255350873.0), (9567379152.0, 'Cursor', 19088302644.1, 146343653513.0)]", "Test #4: state.get_history() after time=10000000000.0 does not equal the expected history. It seems your buying algorithm does not work correctly. Compare your history to the expected history for debugging.\n")
    # One should not access private fields, so i created this method.
    #suite.run_test(str(state.get_cookies_total()), "153308849166.0", "Test #4: state.get_cookies_total() after time=10000000000.0 does not equal 153308849166.0")        
    
    suite.report_results()
    
def simulate_clicker_with_none_strategy_test(simulate_clicker,strategy_none):
    """
    Tests for simulations using the none_strategy
    """    

    print_header("Starting tests for strategy_none used by simulate_clicker")    

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
        
    state = simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_none)
    # using str() here since float number computation yields errors
    # e.g.: try this code:
    # 		print 0.1 + 0.2 == 0.3 
    # It will evaluate to False
    # see https://docs.python.org/2/tutorial/floatingpoint.html#representation-error
    suite.run_test(str(state.get_cookies()), "10000000000.0", "Test #1: state.get_cookies() after time=10000000000.0 does not equal 10000000000.0\n")
    suite.run_test(str(state.get_cps()), "1.0", "Test #2: state.get_cps() after time=10000000000.0 does not equal 1.0. It seems that you do not buy the cursor items at the right time.\n")
    suite.run_test(str(state.get_time()), "10000000000.0", "Test #3: state.get_time() after time=10000000000.0 does not equal 10000000000.0. Did you forget to wait until the end of the duration at the end of the simulate_clicker method?\n")
    suite.run_test(str(state.get_history()), "[(0.0, None, 0.0, 0.0)]", "Test #4: state.get_history() after time=10000000000.0 does not equal the expected history. It seems your buying algorithm does not work correctly. Compare your history to the expected history for debugging.\n")
    # One should not access private fields, so i created this method.
    #suite.run_test(str(state.get_cookies_total()), "10000000000.0", "Test #4: state.get_cookies_total() after time=10000000000.0 does not equal 10000000000.0")        

    suite.report_results()

def run_clicker_state_tests(ClickerState):
    """
    Tests for the ClickerState object
    """
    
    print_header("Starting tests for ClickerState object")    

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test constructor.
    clickerState = ClickerState()
    suite.run_test(clickerState.get_cookies(), 0.0, "Test #1: get_cookies after init is not 0.0")
    suite.run_test(clickerState.get_cps(), 1.0, "Test #2: get_cps after init is not 1.0")
    suite.run_test(clickerState.get_time(), 0.0, "Test #3: get_time after init is not 0.0")
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0)], "Test #4: get_history after init is not [(0.0, None, 0.0, 0.0)]")

    #test time_until method.
    suite.run_test(clickerState.time_until(0), 0.0, "Test #6: time_until(0) after init is not 0.0")
    suite.run_test(clickerState.time_until(1), 1.0, "Test #7: time_until(1) after init is not 1.0")
    suite.run_test(clickerState.time_until(3.1415), 4.0, "Test #8: time_until(3.1415) after init is not 4.0")
    
    #test wait method.
    clickerState = ClickerState()
    clickerState.wait(1)
    suite.run_test(clickerState.get_time(), 1.0, "Test #9: get_time() after wait(1) is not 1.0")
    suite.run_test(clickerState.get_cookies(), 1.0, "Test #10: get_cookies() after wait(1) is not 1.0")
    clickerState.wait(3.1415)
    suite.run_test(clickerState.get_time(), 1.0 + 3.1415, "Test #11: get_time() after wait(1+3.1415) is not 4.1415")
    suite.run_test(clickerState.get_cookies(), 1.0 + 3.1415, "Test #12: get_cookies() after wait(1+3.1415) is not 4.1415")
        
    #test time_until method and wait method in combination.
    clickerState = ClickerState()
    clickerState.wait(1)
    suite.run_test(clickerState.time_until(0.5), 0.0, "Test #13: time_until(0.5) after wait(1) is not 0.0")
    suite.run_test(clickerState.time_until(1), 0.0, "Test #14: time_until(1) after wait(1) is not 0.0")
    suite.run_test(clickerState.time_until(2), 1.0, "Test #15: time_until(2) after wait(1) is not 1.0")
        
    clickerState = ClickerState()
    clickerState.wait(100.0)
    
    time = clickerState.time_until(50.0)    
    detail = ""
    if time < 0:
        detail = "Your time_until method returned a value < 0 ("+str(time)+"). Maybe you forgot to return always 0 if the amount of cookies to wait for is smaller or equal the amount of cookies you already have?"
    elif time > 0:
        detail = "Your time_until method returned a value > 0 ("+str(time)+"). Did you forgot to include the cookies you already have into your calculation?"
    suite.run_test(time,0.0,"Test #35: time_until may not work correctly. After waiting 100s one should have 100 cookies. When you call time_until(50) after that, it should return 0.0!\n"+detail)
                
        
    #test buy_item method.
    clickerState = ClickerState()
    suite.run_test(clickerState.buy_item("too expensive yet",0.1,1.0), None, "Test #16: buy item that is too expensive after initializing")
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0)], "Test#17: check history after trying to buy too expensive item")

    #test adjusting cps by buying an item
    clickerState = ClickerState()
    item_name = "free item! yeah!"
    item_cps_plus = 1.0
    price = 0.0    
    cookies = 0.0
    clickerState.buy_item(item_name,price,item_cps_plus)
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0),(0.0,item_name,price,cookies)], "Test #19: history after buying not as expected")
    suite.run_test(clickerState.get_cps(), 2.0, "Test #20: cps after buying item is not adjusted!")   
    suite.run_test(clickerState.time_until(1.0), 1.0, "Test #21: incorrect calculation of time_until after after buying item with cps +2.0")   
    
    #test history after buying more items at the same time
    another_item_name = "WLAN cable"
    item_cps_plus = 1.0
    price = 0.0    
    clickerState.buy_item(another_item_name,price,item_cps_plus)
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0),(0.0,item_name,price,cookies),(0.0,another_item_name,price,cookies)], "Test #23: incorrect history after buying a 2nd item")
    
    #test history after buying more items at different times
    time_to_wait = 2.0
    clickerState.wait(time_to_wait)
    coockies_now = clickerState.get_cookies()
    clickerState.buy_item(another_item_name,coockies_now,item_cps_plus)
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0),(0.0,item_name,price,cookies),(0.0,another_item_name,price,cookies),(time_to_wait,another_item_name,coockies_now,coockies_now)], "Test #25: incorrect history after buying a 3rd item")
    suite.run_test(clickerState.get_cookies(), 0.0, "Test #26: The cookies are not spent completely. The buy_item method may not correctly adjust the cookies after buying.")    
    
    #test buy_item in a more complex scenario.
    # 1. calculate the time to wait until we have enough cookies to buy an item
    # 2. wait just not long enough (one nanosecond) before trying to buy the item
    # 3. try to buy the item
    # 4. check the item is not bought yet
    # 5. wait a nanosecond
    # 6. buy again
    # 7. check the item was bought.
    # 8. check the cps were adjusted correctly
    clickerState = ClickerState()
    price = 10
    item_name = "rubber duck"
    item_cps_plus = 3.1415
    time_to_wait = clickerState.time_until(price)
    clickerState.wait(time_to_wait-(1.0/1000000)) #just a nanosecond too early!
    suite.run_test(clickerState.get_cookies() < price, True, "Test #27: There are too many cookies after the testet time.")       
    clickerState.buy_item(item_name,price,item_cps_plus)
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0)], "Test #29: The item, that was too expensive to buy is in the history.")
    clickerState.wait(1.0/1000000) #waiting another nanosecond
    suite.run_test(clickerState.get_cookies() == price, True, "Test #30: There are too few cookies after the testet time.")       
    clickerState.buy_item(item_name,price,item_cps_plus)
    suite.run_test(clickerState.get_history(), [(0.0, None, 0.0, 0.0),(time_to_wait,item_name,price,price)], "Test #32: Incorrect history after buying an item.")
    suite.run_test(clickerState.get_cps(), 1.0+item_cps_plus, "Test #33: cps are incorrect after buying")    
    suite.run_test(clickerState.get_cookies(), 0.0, "Test #34: cookies are incorrect after buying")    
        
    suite.report_results()
    
class BuildInfoMock:
    '''
    Mock class recording all calls.
    '''
    def __init__(self,cost,cps):
        self._captured_calls = {'clone':[],'get_cost':[],'get_cps':[],'update_item':[]}
        self._cost = cost
        self._cps = cps
    
    def clone(self):
        self._captured_calls['clone'].append([])
        return self
    
    def get_cost(self, item):
        self._captured_calls['get_cost'].append(item)
        return self._cost
    
    def get_cps(self, item):
        self._captured_calls['get_cps'].append(item)
        return self._cps
    
    def update_item(self, item):
        self._captured_calls['update_item'].append(item)
    
    def get_captured_calls(self):
        return self._captured_calls
    
class StrategyCallInterceptor:
    '''
    A class to monitor the calls on a strategy by the simulate_clicker method.
    '''
    def __init__(self,item_names):
        self._item_names = item_names
        self._captured_calls = []
        self._item_index = -1

    def test_strategy(self,cookies,cps,time_left,build_info):
        '''
        Test strategy function to verify the call.
        '''
        self._captured_calls.append((cookies,cps,time_left,build_info))     
        if self._item_index < len(self._item_names)-1:
            self._item_index += 1
        else:
            return None
        return self._item_names[self._item_index]
    
    def get_captured_calls(self):
        return self._captured_calls
    
def simulate_clicker_with_mocks(simulate_clicker):
    """
    Testing the simulate_clicker method itself
    """
    print_header("Starting tests for simulate_clicker using a test strategy")    
    
     # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    default_cost = 15.0
    default_cps = 0.1
    
    build_info_mock = BuildInfoMock(default_cost,default_cps);
    strategy_interceptor = StrategyCallInterceptor(["my_item","my_other_item","the_last_item"])
    state = simulate_clicker(build_info_mock, 100, strategy_interceptor.test_strategy)
    
    calls = build_info_mock.get_captured_calls()

    explanation = "\nThis test verifies, that you do not call the same methods more than once per\nturn in the main loop of the simulate_clicker function. However, you can call it as often\nas you like per turn but in general you should call a method once and store it into a\nvariable to avoid too many method calls. (You never know how long the computation within\na method of may take, if you don't know the code within)\n\n"
    
    suite.run_test(calls['clone'], [[]], "Test #1: BuildInfo object was not cloned!\n"+explanation)        
    suite.run_test(calls['get_cost'], ['my_item', 'my_other_item', 'the_last_item'], "Test #2: BuildInfo.get_cost should have been called 3 times but was "+str(len(calls['get_cost']))+" times!\n"+explanation)        
    suite.run_test(calls['get_cps'], ['my_item', 'my_other_item', 'the_last_item'], "Test #3: BuildInfo.get_cps should have been called 3 times but was "+str(len(calls['get_cps']))+" times!\n"+explanation)        
    suite.run_test(calls['update_item'], ['my_item', 'my_other_item', 'the_last_item'], "Test #4: BuildInfo.update_item should have been called 3 times but was "+str(len(calls['get_cps']))+" times!\n"+explanation)        
    
    suite.run_test(state.get_time(), 100.0, "Test #5: ClickerState.get_time was not correct after simulate_clicker. Did you forget to wait until the end of the duration?\n")        
    suite.run_test(str(state.get_cps()), str(1.3), "Test #6: ClickerState.get_cps was not correct after simulate_clicker. Make sure you were buying the items and the buy function works correctly.\n")        
    suite.run_test(str(state.get_cookies()), str(76.4), "Test #7: ClickerState.get_cookies was not correct after simulate_clicker. Make sure you were buying the items and accumulate cookies correctly.\n")        
    suite.run_test(str(state.get_history()), "[(0.0, None, 0.0, 0.0), (15.0, 'my_item', 15.0, 15.0), (29.0, 'my_other_item', 15.0, 30.4), (42.0, 'the_last_item', 15.0, 46.0)]", "Test #8: Your history was not correct. This may be due to some error in the way you buy items within the simulate_clicker function.\n")        
    
    suite.report_results()

class OwlTestLikeBuildInfo:
    '''    
    A build info class like the one use in owl test.
    '''
    def __init__(self):
        self._calls = 0;
    
    def clone(self):
        return self
    
    def get_cost(self, item):       
        return 15*1.15**self._calls
    
    def get_cps(self, item):        
        return 50
    
    def update_item(self, item):
        self._calls += 1
    
    
def simulate_clicker_like_in_owl_test(simulate_clicker,strategy_cursor):
    """
    Testing the simulate_clicker method like in the owl test suite
    """
    print_header("Starting tests for simulate_clicker using a test similat to the owl test")    
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    state = simulate_clicker(OwlTestLikeBuildInfo(), 16, strategy_cursor)
    
    suite.run_test(str(state.get_time()), str(16.0), "Test #1: ClickerState.get_time was not correct after simulate_clicker. Did you forget to wait until the end of the duration?\n")        
    suite.run_test(str(state.get_cps()), str(151.0), "Test #2: ClickerState.get_cps was not correct after simulate_clicker. Make sure you were buying the items and the buy function works correctly.\n")        
    suite.run_test(str(state.get_cookies()), str(13.9125), "Test #3: ClickerState.get_cookies was not correct after simulate_clicker. Make sure you were buying the items and accumulate cookies correctly.\n")        
    suite.run_test(len(state.get_history()), 4, "Test #4: Your history was not correct. There should be 4 entries in your history. Please look at the expected history and compare the values. Especially look at the time values in the history entries.\n")            
    suite.run_test(str(state.get_history()), "[(0.0, None, 0.0, 0.0), (15.0, 'Cursor', 15.0, 15.0), (16.0, 'Cursor', 17.25, 66.0), (16.0, 'Cursor', 19.8375, 66.0)]", "Test #8: Your history was not correct. Make sure to two items at second 16.\n")        
    
    suite.report_results()
    
def run_simulate_clicker_tests(simulate_clicker,strategy_none,strategy_cursor):    
    simulate_clicker_with_none_strategy_test(simulate_clicker,strategy_none)
    #simulate_clicker_with_cursor_strategy_test(simulate_clicker,strategy_cursor) 
    #simulate_clicker_like_in_owl_test(simulate_clicker,strategy_cursor)
    #simulate_clicker_with_mocks(simulate_clicker)
    
    