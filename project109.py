import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("project109.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

fsds, fsde = mean-deviation, mean+deviation
ssds, ssde = mean-(2*deviation), mean+(2*deviation)
tsds, tsde = mean-(3*deviation), mean+(3*deviation)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[fsds, fsds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[fsde, fsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[ssds, ssds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[ssde, ssde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

listOfDataWithin1Deviation = [result for result in data if result > fsds and result < fsde]
listOfDataWithin2Deviation = [result for result in data if result > ssds and result < ssde]
listOfDataWithin3Deviation = [result for result in data if result > tsds and result < tsde]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(deviation))

print("{}% of data lies within 1 standard deviation".format(len(listOfDataWithin1Deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(listOfDataWithin2Deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(listOfDataWithin3Deviation)*100.0/len(data)))