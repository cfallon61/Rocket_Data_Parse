import data_parse as parse
import easygui as gui


def main():
    try:
        filename = gui.fileopenbox("", "Data File")
    except TypeError:
        return
    parse.read_data(filename)
    get_data_choices()

def get_data_choices():
    options = ["Acceleration", "Gyro", "Temp"]
    choices = gui.multchoicebox("Choose the data to be plotted.", "Sensors", options)
    if choices is None:
        return -1

    if choices.count("Acceleration") == 1:
        selections = get_axis_choices()
        parse.plot_accel(selections)

    if choices.count("Gyro") == 1:
        selections = get_axis_choices()
        parse.plot_gyro(selections)

    if choices.count("Temp") == 1:
        parse.plot_temp()

def get_axis_choices():
    choices = ["X Axis", "Y Axis", "Z Axis"]
    selections = gui.multchoicebox("Choose the Axes to be plotted.", "Axes", choices)
    return selections

main()