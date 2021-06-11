import pandas as pd
import statistics 
import csv
import plotly.figure_factory as ff

df=pd.read_csv("StudentsPerformance.csv")
reading=df["reading score"].to_list()

readingmean=statistics.mean(reading)
readingmedian=statistics.mean(reading)
readingmode=statistics.mode(reading)

print("mean,median and mode of reading is {}, {}, and {} respectively".format(readingmean,readingmedian,readingmode))
fig=ff.create_distplot([reading],["reading"],show_hist=False)
fig.show()
readingstdev=statistics.stdev(reading)

print("standard devation of reading is {}".format(readingstdev))
hfirst_stdStart, hfirst_stdEnd= readingmean-readingstdev,readingmean+readingstdev
hsecond_stdStart, hsecond_stdEnd= readingmean-(2*readingstdev), readingmean+(2*readingstdev)
hthird_stdStart, hthird_stdEnd= readingmean-(3*readingstdev), readingmean+(3*readingstdev)

readingDataWithinFirst_std=[result for result in reading if result > hfirst_stdStart and result < hfirst_stdEnd]
readingDataWithinSecond_std=[result for result in reading if result > hsecond_stdStart and result < hsecond_stdEnd]
readingDataWithinThird_std=[result for result in reading if result > hthird_stdStart and result < hthird_stdEnd]

print("{} % of data for reading lies within first standard devation".format(len(readingDataWithinFirst_std)*100/len(reading)))
print("{} % of data for reading lies within second standard devation".format(len(readingDataWithinSecond_std)*100/len(reading)))
print("{} % of data for reading lies within third standard devation".format(len(readingDataWithinThird_std)*100/len(reading)))