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
        self._load_data = load_data(self._date)

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

    def get_temperature(self, loaded_data = None):
        """returns the list of temperature values for the current date
        """
        if loaded_data is None:
            loaded_data = self._load_data
            
        temperature_list = []
        for minute in loaded_data:
            temperature_list.append(minute[1])
        return temperature_list

    def get_sunlight(self, loaded_data = None):
        """returns the list of sunlight values for the current date
        """
        if loaded_data is None:
            loaded_data = self._load_data
            
        sunlight_list = []
        for minute in loaded_data:
            sunlight_list.append(minute[2])
        return sunlight_list

    def get_power(self, array, loaded_data = None):
        """returns the list of power outputs for the current date and the
        given array name
        """        
        if loaded_data is None:
            loaded_data = self._load_data 
                
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
            for minute in loaded_data:
                power_list.append(minute[3][9])    
        else:
            for minute in loaded_data:
                power_list.append(minute[3][arrays[array]])
        return power_list

canvaswidth=840
canvasheight=500

class Plotter(object):
    def __init__(self, master, pvdata):
        master.title("Canvas")

        self._draw_power = []
        self._draw_temperature = None
        self._draw_sunlight = None

        self._canvas = Canvas(master, bg="white", width=canvaswidth, height=canvasheight)
        self._canvas.pack(side=TOP, expand=True, fill=BOTH)

        self._canvas.bind("<Button-1>", self._click_event)
        self._canvas.bind("<ButtonRelease-1>", self._release_event)        
        self._canvas.bind("<B1-Motion>", self._move_event)

        self._pvdata = pvdata

    def _click_event(self, event):
        self._line = self._canvas.create_line(event.x, 0, event.x, canvasheight, fill="black")
        if event.x < 840 and event.x  > -1:
            try:
                print self._pvdata.get_temperature()[event.x]
            except Exception as e:                
                tkMessageBox.showerror(repr(e).split('(')[0], str(e))
    def _release_event(self,event):
        self.delete(self._line)
    def _move_event(self, event):
        self.delete(self._line)
        self._line = self._canvas.create_line(event.x, 0, event.x, canvasheight, fill="black")
        if event.x < 840 and event.x  > -1:
            try:
                print self._pvdata.get_temperature()[event.x]
            except Exception as e:
                tkMessageBox.showerror(repr(e).split('(')[0], str(e))
        
    def draw_power(self, colour):
    
        x_coord = 1
        all_rectangles = []
        
        for minute in self._pvdata.get_power('UQ Centre, St Lucia', load_data(self._pvdata.get_date())):            
            list_of_power = []
            list_of_power.append(x_coord)
            list_of_power.append(canvasheight)
            list_of_power.append(x_coord+1)
            list_of_power.append(canvasheight-minute/1000)
            x_coord += 1
            self._draw_power.append(self._canvas.create_rectangle(list_of_power, outline='orchid', fill='orchid'))

    def draw_temperature(self, colour):
        x_coord = 1
        list_of_temperatures = []
        for minute in self._pvdata.get_temperature(load_data(self._pvdata.get_date())):
            list_of_temperatures.append(x_coord)
            list_of_temperatures.append(canvasheight-minute*10)
            x_coord += 1
        self._draw_temperature = self._canvas.create_line(list_of_temperatures, fill="red")

    def draw_sunlight(self, colour):
        list_of_sunlight = []
        x_coord = 1
        for minute in self._pvdata.get_sunlight(load_data(self._pvdata.get_date())):
            list_of_sunlight.append(x_coord)
            list_of_sunlight.append(canvasheight-minute/3)
            x_coord += 1
        self._draw_sunlight = self._canvas.create_line(list_of_sunlight, fill='orange')
        
    def delete(self, item=ALL):
        self._canvas.delete(item)
            

class OptionsFrame(object):

    def __init__(self, master, plotter, pvdata):
        self._showpower =  IntVar()
        self._showtemp = IntVar()
        self._showsunlight =  IntVar()
        self._currentdate = yesterday()
        self._pvdata = pvdata
        self._plotter = plotter

        frame = Frame(master)
        Button(frame, text="Apply", command=self._apply_change).pack(side=LEFT)

        self._entry = Entry(master)        
        self._entry.insert(0,pvdata.get_date())
        self._entry.pack(side=TOP)

        Button(frame, text="Delete", command=plotter.delete).pack(side=RIGHT)

        Checkbutton(frame, text='Temperature', variable = self._showtemp).pack(side= LEFT)
        check_power = Checkbutton(frame, text='Power', variable =  self._showpower)
        Checkbutton(frame, text='Sunlight', variable = self._showsunlight).pack(side=LEFT)
        check_power.pack(side=LEFT)
        check_power.select()
        
        frame.pack(side=TOP)

        plotter.draw_power("orchid")
       
    def _apply_change(self):
        date = self._entry.get()
        old_date = self._pvdata.get_date()
        if date != old_date:
            self._pvdata.change_date(date)
        self._redraw()
            
    def _redraw(self):
        self._plotter.delete()
        if self._showpower.get():
            try:
                self._plotter.draw_power("orchid")
            except Exception as e:
                tkMessageBox.showerror(repr(e).split('(')[0], str(e))
                return None
        if self._showsunlight.get():
            try:
                self._plotter.draw_sunlight("orange")
            except Exception as e:
                tkMessageBox.showerror(repr(e).split('(')[0], str(e))
                return None
        if self._showtemp.get():
            try:
                self._plotter.draw_temperature("red")
            except Exception as e:
                tkMessageBox.showerror(repr(e).split('(')[0], str(e))
                return None
    def shown_graphs(self):
        return [self._showpower.get(), self._showsunlight.get(),  self._showtemp.get()]

class PVPlotApp(object):

    def __init(self):
        pass

    
pvd = PVData()


root = Tk()
app = Plotter(root,pvd)
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

