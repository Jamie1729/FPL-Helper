# FPL Helper
This project is a work in progress.

This will be a python based machine learning project to predict the best scoring team in fantasy premier league (FPL). \
See the [fantasy premier league](https://fantasy.premierleague.com/) website for more infomation.

## Required packages
See requirements.txt for python packages needed to run this script
## Models
### Hidden Markov Models
A Hidden Markov Model is a representation of sequential data where each data point 
**X<sub>n</sub>** is sampled from a latent (hidden) state **Z<sub>n</sub>**. In this case
the latent state is the "form" the player is in. 


<img src="/public/hmm.png" alt="hmm" width="856" height="272">

### Offset Neural Network