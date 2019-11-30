#Skanda Sastry
#2.13.2019
#Objective: Determine the probability of a player selected in the draft to 
#become an NBA "rotation" player (based on criteria of ppg and mpg)

from pandas import read_csv
from numpy import zeros
import matplotlib.pyplot as plt


#csv of draft picks and various career stats
df = read_csv("1976_to_2015_Draftees_edit2.csv")
statNames = list(df.columns.values)

#start >= 1976, end <= 2015
YEAR_START = 1976
YEAR_END = 2015

#+1 because drafts are inclusive. e.g., 2004-2013 is ten total drafts
YEAR_RANGE = YEAR_END + 1 - YEAR_START
MINS_CRITERIA = 2800
PPG_CRITERIA = 5


nbaPlayerCount = zeros(6)

#loop through the csv, collect how many players of each pick range satisfies 
#the criteria
for index, row in df.iterrows():
    ppg = row[statNames[18]]
    mins = row[statNames[10]]
    
    if (row[statNames[4]] <= YEAR_END
        and row[statNames[4]] >= YEAR_START
        #ppg minimum
        and ppg >= PPG_CRITERIA
        #total minutes minimum
        and mins >= MINS_CRITERIA):
            pk_pos = row[statNames[5]]
            if (pk_pos >= 1 and pk_pos <= 10): 
                nbaPlayerCount[0] += 1
            elif (pk_pos >= 11 and pk_pos <= 20):
                nbaPlayerCount[1] += 1
            elif (pk_pos >= 21 and pk_pos <= 30):
                nbaPlayerCount[2] += 1
            elif (pk_pos >= 31 and pk_pos <= 40):
                nbaPlayerCount[3] += 1
            elif (pk_pos >= 41 and pk_pos <= 50):
                nbaPlayerCount[4] += 1
            elif (pk_pos >= 51 and pk_pos <= 60):
                nbaPlayerCount[5] += 1
        
    
#nbaPlayerCount divided by total picks from the range of years
nbaPlayerProbability = zeros(6, dtype=float)

for i in range(len(nbaPlayerCount)):
    totalPicks = YEAR_RANGE * 10
    nbaPlayerProbability[i] = round(nbaPlayerCount[i]/totalPicks, 3)


draftRange = [1, 2, 3, 4, 5, 6]

LABELS = [
"Pick 1-10", 
"Pick 11-20", 
"Pick 21 to 30", 
"Pick 31 to 40",
"Pick 41 to 50",
"Pick 51 to 60"
]

#Making a Bar graph depicting the data
fig = plt.figure()
ax = plt.subplot()
rects1 = ax.bar(draftRange, nbaPlayerProbability, width = 0.8, align = 'center')

def autolabel(rects):
    i = 0

    #Attach a text label above each bar displaying its height
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                nbaPlayerProbability[i], ha='center', va='bottom')
        
        i += 1

autolabel(rects1)

plt.xticks(draftRange, LABELS)

plt.title("Probability of a draft pick from "
+ str(YEAR_START) + " to " 
+ str(YEAR_END) + " to become a rotation "
+ "NBA player ("+ str(MINS_CRITERIA) + " minutes and " +
str(PPG_CRITERIA) + " ppg)")

plt.xlabel("Draft Pick Range")
plt.ylabel("Probability")

plt.savefig("draft_picks_test", dpi=300)

plt.show()





 

        


    
