import plotly as plot
import plotly.graph_objs as go
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

def get_list_of_data_values(size):
    i = 0;
    count = []
    while i < size:
        count.append(i)
        i = i + 1
    return count

def plot_raw(graph_title, axe_label, data_count, values = []):

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
    traces = []

    if len(values) <= 3 and len(values) > 0:
        for i in values:
            trace = go.Scatter(
                    x = list,
                    y = i,
                    name = 'X Axis',
                    mode = 'lines',
            )
            traces.append(trace)
    elif len(values) > 3:
        trace = go.Scatter(
            x=list,
            y=values,
            name='X Axis',
            mode='lines',
        )
        traces.append(trace)
    else:
        return

    layout = dict(
        title = graph_title,
        xaxis = dict(title = 'Data Points'),
        yaxis = dict(title = axe_label)
    )

    fig = dict(data = traces, layout = layout)
    plot.offline.plot(fig, filename = fileName)

def plot_accel(axes = []):
    axes = is_valid_selection_list(axes)
    if axes == False:
        return -1

    data_list = []

    if axes.count(AXES.X_AXIS) == 1:
        data_list.append(raw_data[0])
    if axes.count(AXES.Y_AXIS) == 1:
        data_list.append(raw_data[1])
    if axes.count(AXES.Z_AXIS) == 1:
        data_list.append(raw_data[2])

    plot_raw("Acceleration", "Force (G's)", len(raw_data[0]), data_list)

def plot_gyro(axes = []):
    axes = is_valid_selection_list(axes)
    if axes == False:
        return -1

    data_list = []

    if axes.count(AXES.X_AXIS) == 1:
        data_list.append(raw_data[3])
    if axes.count(AXES.Y_AXIS) == 1:
        data_list.append(raw_data[4])
    if axes.count(AXES.Z_AXIS) == 1:
        data_list.append(raw_data[5])

    plot_raw("Gyro", "Degrees/Second", len(raw_data[0]), data_list)

def plot_temp():
    plot_raw("Temperature", "Temp (Celsius)", len(raw_data[0]), raw_data[6])

def is_valid_selection_list(list = []):
    if list is None:
        print("Empty Axis List!")
        return False

    axis_list = []

    if list.count("X Axis") == 1:
        axis_list.append(AXES.X_AXIS)
    if list.count("Y Axis") == 1:
        axis_list.append(AXES.Y_AXIS)
    if list.count("Z Axis") == 1:
        axis_list.append(AXES.Z_AXIS)

    return axis_list