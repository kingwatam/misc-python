"""
Simulator for resource generation with upgrades
"""

try:
    import codeskulptor
    import simpleplot
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import SimpleGUICS2Pygame.simpleplot as simpleplot
import math

codeskulptor.set_timeout(20)

def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    current_time = 0
    time_increment = 0
    total_resources_generated = 0
    current_generation_rate = 1
    upgrade_cost = 1
    list_pairs = []    
    for dummy_i in range(num_upgrade):
        # Compute how long till the next upgrade is possible based on the current cost of an upgrade and the current resource generation rate
        time_increment = upgrade_cost / current_generation_rate
        current_time += time_increment
        # add generated resources to total
        total_resources_generated += time_increment* current_generation_rate
        # Simulate purchasing the upgrade by increasing the resource generation rate appropriately and incrementing the current cost of an upgrade
        current_generation_rate += 1
        upgrade_cost += upgrade_cost_increment
        list_pairs.append([current_time, total_resources_generated])
    return list_pairs

def test():
    """
    Testing code for resources_vs_time
    """
    data1 = resources_vs_time(0.5, 20)
    data2 = resources_vs_time(1.5, 10)
    data3 = resources_vs_time(0.0, 10)
    data4 = resources_vs_time(1.0, 10)
    print (data1)
    print (data2)
    print (data3)
    print (data4)
    simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2, data3, data4])

test()

# Sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]

def resources_vs_time2(upgrade_cost_increment_percent, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    current_time = 0
    time_increment = 0
    total_resources_generated = 0
    current_generation_rate = 1
    upgrade_cost = 1
    list_pairs = []    
    for dummy_i in range(num_upgrade):
        # Compute how long till the next upgrade is possible based on the current cost of an upgrade and the current resource generation rate
        time_increment = upgrade_cost / current_generation_rate
        current_time += time_increment
        # add generated resources to total
        total_resources_generated += time_increment* current_generation_rate
        # Simulate purchasing the upgrade by increasing the resource generation rate appropriately and incrementing the current cost of an upgrade
        current_generation_rate += 1
        upgrade_cost *= (1+upgrade_cost_increment_percent)
        list_pairs.append([current_time, total_resources_generated])
    return list_pairs

def test2():
    """
    Testing code for resources_vs_time
    """
    data1 = resources_vs_time(1.0, 50)
    data2 = resources_vs_time2(0.15,100)
    print (data1)
    print (data2)
    simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2])

test2()
input("Press enter to exit ;)")
