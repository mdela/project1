import csv
from datetime import datetime
import matplotlib.pyplot as plt 



# file1 contains California highs and lows
# file2 contains California COVID increases

file1 = 'CAhighsandlows.csv' # change file directory here
file2 = 'CAcovid.csv' # change file directory here

# declare all of the lists
tempDates, tempHighs, tempLows, tempAvgs = [], [], [], []
covidDates, covidIncreases = [], []

# proceed with file1
with open(file1) as f1: 
	reader = csv.reader(f1)
	header_row = next(reader)

	for row in reader:
		tempDate = datetime.strptime(row[1], "%Y-%m-%d")
		tempHigh = int(row[4])
		tempLow = int(row[5])
		tempAvg = int(row[3])

		tempDates.append(tempDate)
		tempHighs.append(tempHigh)
		tempLows.append(tempLow)
		tempAvgs.append(tempAvg)

with open(file2) as f2:
	reader = csv.reader(f2)
	header_row = next(reader)

	for row in reader:
		covidDate = datetime.strptime(row[0], "%Y-%m-%d")
		covidIncrease = int(row[21])

		covidDates.append(covidDate)
		covidIncreases.append(covidIncrease)

fig, ax = plt.subplots(2, 1)

fig.suptitle('Weather Relation to Covid', size=15)

ax[0].plot(tempDates, tempHighs, c='red')
ax[0].plot(tempDates, tempLows, c='blue')
ax[0].fill_between(tempDates, tempHighs, tempLows, facecolor='blue', alpha = 0.2)

ax[0].set_title('Highs and Lows (March 2020 - March 2021)')
ax[0].xaxis.set_ticks([])

ax[1].plot(covidDates, covidIncreases, c='purple')
ax[1].set_title('COVID Daily Cases (March 2020 - March 2021)')

plt.show() 
