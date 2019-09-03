
###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Number: s4371003
#
#   Student Name: Jake Wood
#
###################################################################

#####################################
# Support given below - DO NOT CHANGE
#####################################

from assign1_support import *

def load_data(dateStr):
    """The function that loads the data from the storage and formats it in
    a legible and sensible format

    load_data(date) -> list
    """
    list_of_minutes = []
    count = len(get_data_for_date(dateStr).split("\n"))-1
    #Calling support function giving the data as input and splitting by line and iterating
    #line one by one
    for line in get_data_for_date(dateStr).split("\n"):
        elements_in_line  = line.split(",")
        var = tuple(elements_in_line[:3])
        var1 = elements_in_line[3:]
        new_list = []
        for element in var1:
            new_list.append(float(element))
        if count > 0:
            list_of_minutes.append((var[0], float(var[1]), float(var[2]), tuple(new_list)))
            count -= 1
    return list_of_minutes        
    

def max_temperature(data):
    """Calculates the maximum temperate of a particular date and returns
    that value and the times it occured in a list.

    max_temperature(load_data(date)) -> list
    """
    max_temp = 0
    time_list = []
    for line in data:
        if line[1] > max_temp:
            max_temp = line[1]
    for line in data:
        if line[1] == max_temp:
            time_list.append(line[0])      
    return (max_temp, time_list)


def total_energy(data):
    """Takes the data collated in load_data and calculates the total energy
    of the arrays for the day.

    total_energy(load_data(date)) -> string
    """
    tot_energy = 0
    #interates through all of the array values and adds them to the tot_energy
    for line in data:
        for index in range(0,9):
            tot_energy += float(line[3][index])/60
    #divides by 1000 to show kWh
    return tot_energy/1000


def max_power(data):
    """Takes the data collated in load_data and calculates the maximum power output
    of each respective array.

    max_power(load_data(date)) -> list
    """
    #The following variables refer to the maximum power output for the respective array
    uq_centre = 0
    concentrating = 0
    car_park_1 = 0
    car_park_2 = 0
    sir_llew = 0
    prentice = 0
    advanced_eng = 0
    learning_bld = 0
    global_change = 0
    #iterates through each line checking if the particular index for that time is greater then the current highest power, if it is the value is updated with the new max power
    for line in data:
        if line[3][0] > uq_centre:
            uq_centre = line[3][0]
        if line[3][1] > concentrating:
            concentrating = line[3][1]
        if line[3][2] > car_park_1:
            car_park_1 = line[3][2]
        if line[3][3] > car_park_2:
            car_park_2 = line[3][3]
        if line[3][4] > sir_llew:
            sir_llew = line[3][4]
        if line[3][5] > prentice:
            prentice = line[3][5]
        if line[3][6] > advanced_eng:
            advanced_eng = line[3][6]
        if line[3][7] > learning_bld:
            learning_bld = line[3][7]
        if line[3][8] > global_change:
            global_change = line[3][8]
    return [('UQ Centre, St Lucia', uq_centre/1000), ('Concentrating Array', concentrating/1000), ('Multi Level Car Park #1', car_park_1/1000), ('Multi Level Car Park #2', car_park_2/1000), ('Sir Llew Edwards Bld', sir_llew/1000), ('Prentice Building', prentice/1000), ('Advanced Engineering Bld.', advanced_eng/1000), ('Learning Innovation Bld.', learning_bld/1000), ('Global Change Institute', global_change/1000)]
    
def display_stats(date):
    """Takes the date and uses all calculations from the functions above to create
    a logically formatted menu of data for a particular day.

    display_stats(string) -> string
    """
    print '\n' + 'Statistics for ' + date + '\n'
    max_temp = 'Maximum Temperature: ' + str(max_temperature(load_data(date))[0])+ 'C at times '
    #creates a loop with a count to capture the times in which the max temperature
    #over the course of a day.
    count = len(max_temperature(load_data(date))[1])
    for index in range(len(max_temperature(load_data(date))[1])):
        max_temp += str(max_temperature(load_data(date))[1][index])
        if count > 1:
            max_temp += ', '
            count -= 1
    print max_temp + '\n'
    print 'Total Energy Production : ' + (str("{0:.1f}".format(total_energy(load_data(date))))) + 'kWh' + '\n'
    print 'Maximum Power Outputs:' + '\n'
    print str(max_power(load_data(date))[0][0]) + str("{0:.1f}".format(max_power(load_data(date))[0][1])).rjust(40-len(str(max_power(load_data(date))[0][0]))) + 'kW'
    print str(max_power(load_data(date))[1][0]) + str("{0:.1f}".format(max_power(load_data(date))[1][1])).rjust(40-len(str(max_power(load_data(date))[1][0]))) + 'kW'
    print str(max_power(load_data(date))[2][0]) + str("{0:.1f}".format(max_power(load_data(date))[2][1])).rjust(40-len(str(max_power(load_data(date))[2][0]))) + 'kW'
    print str(max_power(load_data(date))[3][0]) + str("{0:.1f}".format(max_power(load_data(date))[3][1])).rjust(40-len(str(max_power(load_data(date))[3][0]))) + 'kW'
    print str(max_power(load_data(date))[4][0]) + str("{0:.1f}".format(max_power(load_data(date))[4][1])).rjust(40-len(str(max_power(load_data(date))[4][0]))) + 'kW'
    print str(max_power(load_data(date))[5][0]) + str("{0:.1f}".format(max_power(load_data(date))[5][1])).rjust(40-len(str(max_power(load_data(date))[5][0]))) + 'kW'
    print str(max_power(load_data(date))[6][0]) + str("{0:.1f}".format(max_power(load_data(date))[6][1])).rjust(40-len(str(max_power(load_data(date))[6][0]))) + 'kW'
    print str(max_power(load_data(date))[7][0]) + str("{0:.1f}".format(max_power(load_data(date))[7][1])).rjust(40-len(str(max_power(load_data(date))[7][0]))) + 'kW'
    print str(max_power(load_data(date))[8][0]) + str("{0:.1f}".format(max_power(load_data(date))[8][1])).rjust(40-len(str(max_power(load_data(date))[8][0]))) + 'kW' + '\n'


def interact():
    """The function that defines the way the user
    iterates with the program

    interact() -> None
    """
    print 'Welcome to PV calculator' + '\n' + '\n'
    while True:
        command = raw_input('Command: ')
        if command == 'q':
            #This will quit the program
            break
        #checks that the word date is at the beginning of the command
        elif len(command) == 15:
            #constraints the command to a certain length
            if command[:4] != 'date':
                print 'Unknown command: ' + command + '\n'
            if command[:4] == 'date':
                #gives an unknown command for any exceptions
                try:
                    display_stats(command[5:])
                except Exception:
                    print 'Unknown command: ' + command
        else:
            print 'Unknown command: ' + command + '\n'
            
                            
    

##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

if __name__ == '__main__':
    interact()

