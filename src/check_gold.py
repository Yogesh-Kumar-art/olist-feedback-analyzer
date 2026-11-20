import pandas as pd

gold = pd.read_csv("data/labeled/gold_reviews_100.csv")
print(gold["gold_sentiment"].value_counts(dropna=False))
print(gold["gold_category"].value_counts(dropna=False))
print("Blank rows:", gold[["gold_sentiment", "gold_category"]].isna().any(axis=1).sum())