import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

#reading scores data

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

#Calculating the mean and the standard deviation

mean = sum(data) / len(data)
stnd_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values

first_stnd_start, first_stnd_end = mean-stnd_deviation, mean+stnd_deviation
second_stnd_start, second_stnd_end = mean-(2*stnd_deviation), mean+(2*stnd_deviation)
third_stnd_start, third_stnd_end = mean-(3*stnd_deviation), mean+(3*stnd_deviation)

#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stnd_start, first_stnd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stnd_end, first_stnd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stnd_start, second_stnd_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_stnd_end, second_stnd_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()
#Printing the findings

list_of_data_within_one_stnd = [result for result in data if result > first_stnd_start and result < first_stnd_end]
list_of_data_within_two_stnd = [result for result in data if result > second_stnd_start and result < second_stnd_end]
list_of_data_within_three_stnd = [result for result in data if result > third_stnd_start and result < third_stnd_end]

print("Mean of this data is ", mean)
print("Median of this data is ", median)
print("Mode of this data is ", mode)
print("Standard deviation of this data is ", stnd_deviation)
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_one_stnd)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_two_stnd)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_three_stnd)*100.0/len(data)))