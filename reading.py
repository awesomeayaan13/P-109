import pandas as pd
import statistics
import csv

import plotly.figure_factory as ff

import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
reading_score=df["reading score"]

mean=statistics.mean(reading_score)
median=statistics.median(reading_score)
mode=statistics.mode(reading_score)
print("Mean,Median And Mode of Reading Score is {},{} and {} respectivilly".format(mean,median,mode))

std_dev=statistics.stdev(reading_score)

first_std_dev_start , first_std_dev_end = mean-std_dev , mean+std_dev
second_std_dev_start ,second_std_dev_end = mean-(2*std_dev) , mean+(2*std_dev)
third_std_dev_start , third_std_dev_end = mean-(3*std_dev) , mean+(3*std_dev)

listOfDataWithin1StdDev=[result for result in reading_score if result > first_std_dev_start and result < first_std_dev_end]
listOfDataWithin2StdDev=[result for result in reading_score if result > second_std_dev_start and result < second_std_dev_end]
listOfDataWithin3StdDev=[result for result in reading_score if result > third_std_dev_start and result < third_std_dev_end]

print("{}% of data lies within 1 stdev".format(len(listOfDataWithin1StdDev)*100/len(reading_score)))
print("{}% of data lies within 2 stdev".format(len(listOfDataWithin2StdDev)*100/len(reading_score)))
print("{}% of data lies within 3 stdev".format(len(listOfDataWithin3StdDev)*100/len(reading_score)))

fig=ff.create_distplot([reading_score],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="stdDev1 Start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="stdDev1 End"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="stdDev2 Start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="stdDev2 End"))
fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.17],mode="lines",name="stdDev3 Start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.17],mode="lines",name="stdDev3 End"))


fig.show()