import plotly as plot
import plotly.graph_objs as go
import tkinter
from enum import Enum
from datetime import datetime



class AXES(Enum):
    X_AXIS = 0
    Y_AXIS = 1
    Z_AXIS = 2
    ALL_AXES = 3

raw_data = [[], [], [], [], [], [], []]

event_lines = []

def read_data(filename):
    line_count = 0
    with open(filename, "r") as data:
        for line in data:
            line = line.strip()     #strips off new line characters
            if line.find("Parachute_Deployed") != -1 or line.find("Launch_Detect") != -1 or line.find("Landed") != -1: #if these lines are found, add them to a list
                event_lines.append(str(line_count) + ": " + line)
                continue
            data_line = line.split('\t')
            i = 0
            for element in data_line:
                raw_data[i].append(element)
                i = i + 1
            line_count = line_count + 1

    # for i in raw_data:
    #     print("X_ACCEL: {0}, Y_ACCEL: {1}, Z_ACCEL: {2}\nX_GYRO: {3}, Y_GYRO: {4}, Z_GYRO: {5}\nTEMP: {6}".format(
    #         i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

def get_list_of_data_values(size):
    i = 0;
    count = []
    while i < size:
        count.append(i)
        i = i + 1
    return count

def plot_raw(title, axe_label, data_count, value = []):
    plot_raw(title, axe_label, data_count, value, [], [])

def plot_raw(graph_title, axe_label, data_count,  value_0 = [], value_1 = [], value_2 = []):

    fileName = ""
    extension = str(datetime.now().time())
    extension = extension.replace(":", "_")
    if graph_title.find('Acceleration') != -1:
        fileName = "Accel_Data"
    elif graph_title.find("Gyro") != -1:
        fileName = "Gyro_Data"
    else:
        fileName = "Temp_data"

    fileName = fileName + "_" + extension + ".html"
    list = get_list_of_data_values(data_count)

    trace0 = go.Scatter(
        x = list,
        y = value_0,
        name = 'X Axis',
        mode = 'lines',
    )
    trace1 = go.Scatter(
        x = list,
        y = value_1,
        name = 'Y Axis',
        mode = 'lines'
    )
    trace2 = go.Scatter(
        x = list,
        y = value_2,
        name = 'Z Axis',
        mode = 'lines'
    )

    data = [trace0, trace1, trace2]

    layout = dict(
        title = graph_title,
        xaxis = dict(title = 'Data Points'),
        yaxis = dict(title = axe_label)
    )

    fig = dict(data = data, layout = layout)
    plot.offline.plot(fig, filename = fileName)

def plot_accel(axis):
    if axis == AXES.ALL_AXES:
        plot_raw("Acceleration for All Axes", "Force (G's)", len(raw_data[0]), raw_data[0], raw_data[1], raw_data[2])
    elif axis == AXES.X_AXIS:
        plot_raw("Acceleration for X Axis", "Force (G's)", len(raw_data[0]), raw_data[0])
    elif axis == AXES.Y_AXIS:
        plot_raw("Acceleration for Y Axis", "Force (G's)", len(raw_data[0]), raw_data[1])
    elif axis == AXES.Z_AXIS:
        plot_raw("Acceleration for Z Axis", "Forces (G's)", len(raw_data[0]), raw_data[2])
    else:
        return -1


def plot_gyro(axis):
    if axis == AXES.ALL_AXES:
        plot_raw("Gyro for All Axes", "Degrees", len(raw_data[0]), raw_data[3], raw_data[4], raw_data[5])
    elif axis == AXES.X_AXIS:
        plot_raw("Gyro for X Axis", "Degrees", len(raw_data[0]), raw_data[3])
    elif axis == AXES.Y_AXIS:
        plot_raw("Gyro for Y Axis", "Degrees", len(raw_data[0]), raw_data[4])
    elif axis == AXES.Z_AXIS:
        plot_raw("Gyro for Z Axis", "Degrees", len(raw_data[0]), raw_data[5])
    else:
        return -1

def plot_temp():
    plot_raw("Temperature", "Temp (Celsius)", len(raw_data[0]), raw_data[6])

def main():
    filename = "C:/Users/Chris/Desktop/DATALOG.TXT"
    read_data(filename)
    plot_accel(AXES.ALL_AXES)
    plot_gyro(AXES.ALL_AXES)
    # plot_temp()
    for i in event_lines:
        print(i)
main()