import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances

#League average statistics for 2024

league_obp = 0.312
league_slg = 0.399
constant_oaa = 15
league_speed = 27

#Read in data

df = pd.read_csv("4_tools.csv")
df = df.dropna(subset=["outs_above_average"])

#Normalize player statistics based on league averages

df['normalized_obp'] = df['on_base_percent'] / league_obp
df['normalized_slg'] = df['slg_percent'] / league_slg
df['normalized_oaa'] = 1 + (df['outs_above_average'] / constant_oaa)
df['normalized_speed'] = df['sprint_speed'] / league_speed

#Euclidean Distance

tools = df[['normalized_obp', 'normalized_slg', 'normalized_oaa', 'normalized_speed']].values
euclidean_dist = pairwise_distances(tools)
distance_df = pd.DataFrame(euclidean_dist, index=df['last_first'], columns=df['last_first'])

#Function: Return the top 10 players similar to the requested player

def SimilarPlayer(player_name, number=10):
    return distance_df[player_name].sort_values()[1:number+1]

#Prints Top 10 players similar 

Similarities = SimilarPlayer("Betts, Mookie")
print(f"Top 10 players similar to {Similarities.name}")
print(Similarities)