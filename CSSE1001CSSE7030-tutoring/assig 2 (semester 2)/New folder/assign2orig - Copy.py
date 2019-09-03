###################################################################
#
#   CSSE1001/7030 - Assignment 2
#
#   Student Number: 43710034
#
#   Student Name: Jake Wood
#
###################################################################

#
# Do not change the following import
#

from assign2_support import *

####################################################################
#
# Insert your code below
#
####################################################################

class PVData(object):
    """A class used to hold the PV data for a given date
    """

    def __init__(self):
        """Initializes the PV data to yesterdays date
        """
        self._date = yesterday()

    def change_date(self, date):
        """Changes the date to be a given date
        """
        self._date = date

    def get_date(self):
        """Returns the date for the stored data
        """
        return self._date

    def get_time(self, time_index):
        """returns the time for the given index of the time data
        """
        return load_data(self._date)[time_index][0]

    def get_temperature(self):
        """returns the list of temperature values for the current date
        """
        temperature_list = []
        for minute in load_data(self._date):
            temperature_list.append(minute[1])
        return temperature_list

    def get_sunlight(self):
        """returns the list of sunlight values for the current date
        """
        sunlight_list = []
        for minute in load_data(self._date):
            sunlight_list.append(minute[2])
        return sunlight_list

    def get_power(self, array):
        """returns the list of power outputs for the current date and the
        given array name
        """
        arrays = {'UQ Centre, St Lucia' : 0,
                  'Concentrating Array' : 1,
                  'Multi Level Car Park #1' : 2,
                  'Multi Level Car Park #2' : 3,
                  'Sir Llew Edwards Bld.' : 4,
                  'Prentice Building' : 5,
                  'Advanced Engineering Bld.' : 6,
                  'Learning Innovation Bld.' : 7,
                  'Global Change Institute' : 8}
        power_list = []
        if array == "All Arrays Combined":
            for minute in load_data(self._date):
                power_list.append(minute[3][9])    
        else:
            for minute in load_data(self._date):
                power_list.append(minute[3][arrays[array]])
        return power_list

canvaswidth=840
canvasheight=500

class Plotter(object, Canvas, Frame):
    def __init__(self, master, pvdata):
        master.title("Canvas")

        self._draw_power = []
        self._draw_temperature = None
        self._draw_sunlight = None

        self._canvas = Canvas(master, bg="white", width=canvaswidth, height=canvasheight)
        self._canvas.pack(side=TOP, expand=True, fill=BOTH)

        self._pvdata = pvdata

    def draw_power(self):
    
        x_coord = 1
        all_rectangles = []
        for minute in self._pvdata.get_power('UQ Centre, St Lucia'):
            list_of_power = []
            list_of_power.append(x_coord)
            list_of_power.append(canvasheight)
            list_of_power.append(x_coord+1)
            list_of_power.append(canvasheight-minute/1000)
            x_coord += 1
            self._draw_power.append(self._canvas.create_rectangle(list_of_power, outline='orchid', fill='orchid'))

    def draw_temperature(self):

        x_coord = 1
        list_of_temperatures = []
        for minute in self._pvdata.get_temperature():
            list_of_temperatures.append(x_coord)
            list_of_temperatures.append(canvasheight-minute*10)
            x_coord += 1
        self._draw_temperature = self._canvas.create_line(list_of_temperatures, fill="red")

    def draw_sunlight(self):

        list_of_sunlight = []
        x_coord = 1
        for minute in self._pvdata.get_sunlight():
            list_of_sunlight.append(x_coord)
            list_of_sunlight.append(canvasheight-minute/3)
            x_coord += 1
        self._draw_sunlight = self._canvas.create_line(list_of_sunlight, fill='orange')
        
    def delete_power(self):
        for line in self._draw_power:
             self._canvas.delete(line)
            

    def toggle(self):
        if self._showtemp:
            self._showtemp = 0
        else:
            self._showtemp = 1
        print self._showtemp

class OptionsFrame(object, Frame):

    def __init__(self, master, plotter, pvdata):

        self._showtemp = 0
        self._showsunlight = 0
        self._currentdate = yesterday()
        self._pvdata = pvdata

        frame = Frame(master)
        Button(frame, text="Apply", command=plotter.draw_power).pack(side=LEFT)

        self._temp_button = Checkbutton(frame, command=self.toggle, variable=self._showtemp)
        self._temp_button.pack()
        
        frame.pack(side=TOP)
        Button(frame, text="Delete", command=plotter.delete_power).pack(side=RIGHT)
        
        self._entry = Entry(master).pack(side=TOP)
        
        
        Button(frame, text="Get date", command=self.get_change_date()).pack(side=BOTTOM)
        
        frame.pack(side=TOP)
        
    def get_change_date(self):
        print "get date"
        self._pvdata.change_date("14-09-2014")



    def toggle(self):
        pass

    

class PVPlotApp(object):

    def __init(self):
        pass

    
pvd = PVData()


root = Tk()
app = Plotter(root, pvd)
frame = OptionsFrame(root, app, pvd)
root.mainloop()







####################################################################
#
# WARNING: Leave the following code at the end of your code
#
# DO NOT CHANGE ANYTHING BELOW
#
####################################################################

def main():
    root = Tk()
    app = PVPlotApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

