import pandas as pd

# 1. Load the files
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
translation = pd.read_csv("data/raw/product_category_name_translation.csv")

# 2. Keep only reviews with text, one row per review
reviews = reviews.dropna(subset=["review_comment_message"])
reviews = reviews.drop_duplicates(subset="review_id")

# 3. One product category per order (the first item in the order)
first_item = items.drop_duplicates(subset="order_id")[["order_id", "product_id"]]
category = first_item.merge(
    products[["product_id", "product_category_name"]], on="product_id", how="left"
)
category = category.merge(translation, on="product_category_name", how="left")
category = category[["order_id", "product_category_name_english"]]
category = category.rename(columns={"product_category_name_english": "product_category"})

# 4. Delivery dates from the orders file
order_dates = orders[[
    "order_id",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]]

# Combine everything into one table
df = reviews.merge(category, on="order_id", how="left")
df = df.merge(order_dates, on="order_id", how="left")
df["product_category"] = df["product_category"].fillna("unknown")

# 5. 40 reviews per star rating, then shuffle
parts = []
for score in [1, 2, 3, 4, 5]:
    group = df[df["review_score"] == score]
    parts.append(group.sample(n=40, random_state=42))
sample = pd.concat(parts)
sample = sample.sample(frac=1, random_state=42).reset_index(drop=True)

# 6a. Save the 200-review sample
sample.to_csv("data/sample/reviews_sample_1000.csv", index=False)

# 6b. Take 10 reviews per star rating = 50 reviews to hand-label
gold_parts = [sample[sample["review_score"] == s].head(10) for s in [1, 2, 3, 4, 5]]
gold = pd.concat(gold_parts)[["review_id", "review_score", "review_comment_message"]]
gold["gold_sentiment"] = ""
gold["gold_category"] = ""
gold.to_csv("data/labeled/gold_reviews_100.csv", index=False, encoding="utf-8-sig")

print("Sample size:", len(sample))
print(sample["review_score"].value_counts().sort_index())
print("Gold size:", len(gold))