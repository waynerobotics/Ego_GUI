from Tkinter import *
import Tkinter as tk
# from tk import *

window = tk.Tk()
window.title("WSU Robotics Command Center")
# window.configure(background='grey')

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=200, padx=200)

# Create a Tkinter variable
tkvar = StringVar(window)

# Dictionary with options
choices = {'Lane Mode', 'Speed Mode', 'Main Competition', 'Obstacle Mode',
           'Waypoint Mode', 'Init Param Server', 'Status Check', 'Kill All'}
tkvar.set('Main Competition')  # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose an option!").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)

# on change dropdown value


def change_dropdown(*args):
    # print( tkvar.get() )
    if tkvar.get() == 'Main Competition':
        print("Main Competition")
    elif tkvar.get() == 'Lane Mode':
        print("Lane Mode")
    elif tkvar.get() == 'Speed Mode':
        print("Speed Mode")
    elif tkvar.get() == 'Obstacle Mode':
        print("Obstacle Mode")
    elif tkvar.get() == 'Waypoint Mode':
        print("Waypoint Mode")
    elif tkvar.get() == 'Init Param Server':
        print("Init Param Server")
    elif tkvar.get() == 'Status Check':
        print("Status Check")
    elif tkvar.get() == 'Kill All':
        window.destroy()
    else:
        pass


# link function to change dropdown
tkvar.trace('w', change_dropdown)
window.mainloop()
