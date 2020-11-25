# nba-draft-probability
A python script which queries a database of NBA draft picks and returns a bar 
graph displaying the probability of a player becoming successful based on their 
draft range. One of the main takeaways is that drafting in the late 2nd round 
(picks 51-60) almost never works out. Furthermore, it is quite clear that all
picks in a given round are not valued equally, which places great importance on 
knowing pick-protection details before determining asset values in trades.

There are two scripts, one that prints a graph of individual picks in the first
round and the other which prints both rounds but uses ranges of picks as bins.

#### Individual pick probabilities
![histogram of draft picks individual picks, small bins](https://github.com/skandasastry/nba-draft-probability/blob/master/1976_2015_indivPickProbability.png?raw=true)

#### Bins as pick ranges
![histogram of draft picks nba](https://github.com/skandasastry/nba-draft-probability/blob/master/1976_2015_rangeProbability.png?raw=true)

Many thanks to Rory Pulvino at data.world for the dataset used to create this:

https://data.world/rvino88/1976-to-2015-nba-draft-data
