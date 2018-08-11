import data_parse as parse
import easygui as gui


def main():
    try:
        filename = gui.fileopenbox("", "Data File")         #try to open the data file for parsing
    except TypeError:
        return
    parse.read_data(filename)       #read the data from the file
    get_data_choices()

def get_data_choices():
    options = ["Acceleration", "Gyro", "Temp"]
    choices = gui.multchoicebox("Choose the data to be plotted.", "Sensors", options)
    if choices is None:     #if there is no choice selected, stop running the program
        return -1

    if choices.count("Acceleration") == 1:      #if Acceleration is checked parse the acceleration data
        selections = get_axis_choices()
        parse.plot_accel(selections)

    if choices.count("Gyro") == 1:      #if gyro is checked parse the gyro data
        selections = get_axis_choices()
        parse.plot_gyro(selections)

    if choices.count("Temp") == 1:      #if temp is checked parse the temp data
        parse.plot_temp()

def get_axis_choices():     #get the axes which are to be plotted
    choices = ["X Axis", "Y Axis", "Z Axis"]
    selections = gui.multchoicebox("Choose the Axes to be plotted.", "Axes", choices)
    return selections

main()
