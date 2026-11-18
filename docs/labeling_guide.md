
# Customer Review Labeling Guide

## 1. Sentiment

| Sentiment | Definition | Example |
|---|---|---|
| positive | Customer is happy with the experience | Excellent product! |
| neutral | Mixed feelings or unclear opinion | Product is good, but delivery was late. |
| negative | Customer is unhappy | Terrible product quality. |

## 2. Primary Categories

| Category | Use it when | Example review |
|---|---|---|
| delivery_delay | The item came late or has not come | Ainda não chegou (It still has not arrived) |
| product_quality | The item is defective, poor, or not as described | Produto de péssima qualidade (Terrible quality product) |
| wrong_or_missing_item | A different item came, or part of the order is missing | Recebi só um dos dois itens (I received only one of the two items) |
| damaged_in_transit | The item arrived broken or packaging was damaged | Veio quebrado (It came broken) |
| seller_communication | The seller did not reply or gave wrong information | O vendedor não respondeu (The seller did not reply) |
| customer_service | Complaints about the marketplace's support team | O suporte não resolveu nada (Support did not solve anything) |
| refund_or_return | Problems with refunds, returns or cancellations | Não consegui devolver o produto (I could not return the product) |
| price_value | Comments on price versus quality | Muito caro para o que é (Too expensive for what it is) |
| positive_experience | Praise only, with no problem raised | Adorei, chegou rápido (Loved it, arrived fast) |
| other | None of the above, or text is too short or unclear | Ok |

## 3. Additional Fields

| Field | Allowed values / Definition |
|---|---|
| sentiment | positive, neutral, negative |
| primary_category | One of the ten categories above |
| key_issue | Short English summary, maximum 12 words |
| needs_followup | true or false; whether the customer still has an unsolved problem |

## 4. Tie-Break Rules

1. If a review has several problems, pick the one the customer seems most upset about.
2. Praise plus a complaint counts as neutral, unless one side clearly dominates.
3. A positive review with no problem is positive and positive_experience.
4. If you truly cannot tell, use neutral and other. Do not agonize.
5. Judge what the customer wrote, not their star rating. Some 5-star reviews contain complaints, and some 1-star reviews are about something unrelated to the seller.

## 5. Manual Labeling

I will manually label only:
- sentiment
- primary_category

The AI will generate:
- key_issue
- needs_followup

I will evaluate key_issue by reading a sample of AI-generated summaries.
