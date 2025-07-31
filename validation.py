import pandas as pd

# This script is for validating LLM answers against the original data.
# It assumes the transcribed CSV files are in the same directory.

try:
    games_df = pd.read_csv('task 5\data\Final_Game_Results_2025.csv')
    players_df = pd.read_csv('task 5/data/player_stats_2025.csv')
except FileNotFoundError:
    print("Data files not found. Please ensure they are transcribed and in the root directory.")
    exit()

print("--- Data Validation ---")

# 1. Record
total_games = len(games_df)
wins = len(games_df[games_df['Result'].str.contains('W')])
losses = total_games - wins
print(f"Record: {wins}-{losses} in {total_games} games.")

# 2. Points Leader
players_df['Pts'] = pd.to_numeric(players_df['Pts'])
points_leader = players_df.loc[players_df['Pts'].idxmax()]
print(f"Points Leader: {points_leader['Player']} with {points_leader['Pts']} points.")

# 3. CT Leader
players_df['CT'] = pd.to_numeric(players_df['CT'])
ct_leader = players_df.loc[players_df['CT'].idxmax()]
print(f"Caused Turnover Leader: {ct_leader['Player']} with {ct_leader['CT']} CT.")

# 4. Scoring Efficiency (Shooting Pct, >=30 shots)
players_df['G'] = pd.to_numeric(players_df['G'])
players_df['Sh'] = pd.to_numeric(players_df['Sh'])
eligible_scorers = players_df[players_df['Sh'] >= 30].copy()
eligible_scorers['Shooting_Pct'] = eligible_scorers['G'] / eligible_scorers['Sh']
top_3_efficient = eligible_scorers.sort_values(by='Shooting_Pct', ascending=False).head(3)

print("\nTop 3 Most Efficient Scorers (G/Sh, >=30 Shots):")
print(top_3_efficient[['Player', 'Shooting_Pct', 'G', 'Sh']])

# 5. Analysis of Losses
losses_df = games_df[games_df['Result'].str.contains('L')]
avg_gf_in_losses = losses_df['SU_Score'].mean()
avg_ga_in_losses = losses_df['Opponent_Score'].mean()
print(f"\nIn losses, team averaged {avg_gf_in_losses:.2f} GF and {avg_ga_in_losses:.2f} GA.")