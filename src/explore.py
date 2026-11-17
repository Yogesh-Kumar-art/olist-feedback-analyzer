import pandas as pd

reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

print(reviews.shape)                       # rows and columns
print(reviews.head())                      # first 5 rows
print(reviews["review_score"].value_counts())   # how many 1-star, 2-star, ...
print(reviews["review_comment_message"].notna().sum())  # reviews with written text