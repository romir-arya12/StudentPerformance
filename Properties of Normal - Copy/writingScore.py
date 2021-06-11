import pandas as pd
import statistics 
import csv
import plotly.figure_factory as ff

df=pd.read_csv("StudentsPerformance.csv")
writing=df["writing score"].to_list()

writingmean=statistics.mean(writing)
writingmedian=statistics.mean(writing)
writingmode=statistics.mode(writing)

print("mean,median and mode of writing is {}, {}, and {} respectively".format(writingmean,writingmedian,writingmode))
fig=ff.create_distplot([writing],["writing"],show_hist=False)
fig.show()
writingstdev=statistics.stdev(writing)

print("standard devation of writing is {}".format(writingstdev))
hfirst_stdStart, hfirst_stdEnd= writingmean-writingstdev,writingmean+writingstdev
hsecond_stdStart, hsecond_stdEnd= writingmean-(2*writingstdev), writingmean+(2*writingstdev)
hthird_stdStart, hthird_stdEnd= writingmean-(3*writingstdev), writingmean+(3*writingstdev)

writingDataWithinFirst_std=[result for result in writing if result > hfirst_stdStart and result < hfirst_stdEnd]
writingDataWithinSecond_std=[result for result in writing if result > hsecond_stdStart and result < hsecond_stdEnd]
writingDataWithinThird_std=[result for result in writing if result > hthird_stdStart and result < hthird_stdEnd]

print("{} % of data for writing lies within first standard devation".format(len(writingDataWithinFirst_std)*100/len(writing)))
print("{} % of data for writing lies within second standard devation".format(len(writingDataWithinSecond_std)*100/len(writing)))
print("{} % of data for writing lies within third standard devation".format(len(writingDataWithinThird_std)*100/len(writing)))