# nba-draft-probability
A python script which queries a database of NBA draft picks and returns a bar 
graph displaying the probability of a player becoming successful based on their 
draft range. One of the main takeaways is that drafting in the late 2nd round 
(picks 51-60) almost never works out. Furthermore, it is quite clear that all
picks in a given round are not valued equally, which places great importance on 
knowing pick-protection details before determining asset values in trades.

There are two scripts, one that prints a graph of individual picks in the first
round and the other which prints both rounds but uses ranges of picks as bins.

The output graphs for the default criteria (5 ppg, 2800 mpg) from 1976 - 2015 
are included in the repo as png files.

Many thanks to Rory Pulvino at data.world for the dataset used to create this.
