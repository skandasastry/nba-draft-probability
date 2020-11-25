# nba-draft-probability

## Summary

Every year in the offseason, the NBA teams gather and select the best college basketball players to join their team. There are two rounds, with 60 total picks, each team getting two picks. The worst teams are given the best picks in the draft in order to give them a chance to rebuild their roster. As an avid NBA fan, I have always been interested in the way NBA talent is evaluated in the draft, and about how to gauge trade value of draft assets. In this project, I used a script to calculate the amount of NBA players drafted at each position who had a **significant** (to be defined later) NBA career. By finding this fraction for each pick (and 10-pick range) of the draft, I made a histogram that aims to visualize the dropoffs in value as a team picks later in the draft.  

The criteria I used to determine an NBA player had a "significant" career was if they played 2800 total minutes in the NBA and averaged above 5 points per game. Although this may seem arbitrary, it did have some thought behind it. I considered a player to be a regular contributor for a team if they played 10 minutes per game (out of 48 total) for 70 games (out of 82 games) each season. The average NBA career length is 5 seasons, and to allow for injury, we can approximate 4 seasons of 70 games at 10 minutes per game = 2800 minutes total. The second criteria, 5 ppg seems intuitive, but can be backed by data as well. In the 2019-2020 season, 351 players achieved the criteria of 5 points per game, according to [NBA Stats](https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&CF=PTS*GE*5:MIN*GE*10&Season=2019-20&SeasonType=Regular%20Season). Since there are 30 teams in the NBA, there are 11.7 players per team who passed this threshold. This seems adequate because 12 players is a long, but reasonable rotation size for most NBA teams. (Maybe someone can pull the data on how many players enter an average game to verify this - this is definitely on my docket). 

In short, the objective was to provide an estimate of the value of each position in the draft by plotting the likelihood of the player to succeed based on prior data.


## Results and Conclusions

Here are the two histograms I created. One splits up the probabilities by 10-pick bins, giving the probability of pick in the 1-10, 11-20, etc. range of being a rotation player. The other splits the probabilities up by 1-pick bins, giving the probability of the 1st, 2nd, etc. picks turning out to be a useful rotation player.


### Bins as pick ranges
![histogram of draft picks nba](https://github.com/skandasastry/nba-draft-probability/blob/master/1976_2015_rangeProbability.png?raw=true)


### 1-pick bin ranges
![histogram of draft picks individual picks, small bins](https://github.com/skandasastry/nba-draft-probability/blob/master/1976_2015_indivPickProbability.png?raw=true)



One of the main takeaways from the 10-pick bin range histogram is that drafting in the late 2nd round 
(picks 51-60) almost never works out. To give this some context, many NBA executives feel more comfortable
taking "project" players that late in the draft who may have an incredibly high best-case potential but 
are not likely to pan out.

Furthermore, it is quite clear that all
picks in a given round are not valued equally. Don't let your team's GM fool you into thinking a top-25 protected pick he received in a trade is valuable! If we define the goal of the draft as finding as many rotation pieces as possible, then picks in the range 21-30 are essentially 50% as valuable as picks in range 1-10. 



## Acknowledgements

Many thanks to Rory Pulvino at data.world for the dataset used to create this: https://data.world/rvino88/1976-to-2015-nba-draft-data

Used matplotlib, pandas, numpy, and csv to read the data in, process it, and plot it.


