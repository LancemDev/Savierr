import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load user data (assuming you have a dataset with user IDs, saving goals, and preferences)
user_data = pd.read_csv("user_data.csv")

# Calculate similarity matrix between users
user_similarities = cosine_similarity(user_data[['preference1', 'preference2', ...]])

# Recommend goals for a target user based on similar users' goals
def recommend_goals(user_id):
    similar_users = user_similarities[user_id].argsort()[-5:-1]  # Find top 4 similar users
    recommended_goals = user_data[user_data['user_id'].isin(similar_users)]['saving_goal'].tolist()
    return recommended_goals
