# importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import praw
import os

st.write(
    """
# Cryptocurrency Reddit mention counter WebApp

## This app shows the most popular cryptocurrencies mentioned in the 'Cryptocurrency' subreddit and counts the number of times each currency is mentioned.
"""
)


# Creating reddit connection
with open("pw.txt", "r") as f:
    pw = f.read()

with open("client_id.txt", "r") as f:
    client_id = f.read()

with open("client_secret.txt", "r") as f:
    client_secret = f.read()


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="<console:HAPPY:1.0>",
    username="anupsam7",
    password=pw,
)

subreddit = reddit.subreddit("CryptoCurrency")

currencies = [
    "bitcoin",
    "ethereum",
    "dogecoin",
    "xrp",
    "cardano",
    "litecoin",
    "polkadot",
    "stellar",
    "chainlink",
    "binance",
    "tether",
    "monero",
    "binance coin",
    "usd coin",
    "uniswap",
    "bitcoin cash",
    "polygon",
    "solana",
    "vechain",
]
new_list = []

# adding the ticker symbols as some posts use symbols instead of currency name

currencies.extend(
    [
        "btc",
        "eth",
        "usdt",
        "ada",
        "bnb",
        "doge",
        "usdc",
        "dot",
        "uni",
        "icp",
        "link",
        "bch",
        "ltc",
        "matic",
        "xlm",
        "busd",
        "sol",
        "vet",
        "etc",
    ]
)

for submission in subreddit.hot(limit=10):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            for currency in currencies:
                if currency in comment_lower:
                    new_list.append(currency)

conversion = {
    "btc": "bitcoin",
    "bitcoin": "bitcoin",
    "eth": "ethereum",
    "usdt": "tether",
    "ada": "cardano",
    "bnb": "binance",
    "doge": "dogecoin",
    "usdc": "usd",
    "dot": "polkadot",
    "uni": "uniswap",
    "icp": "internet computer",
    "link": "chainlink",
    "bch": "bitcoin cash",
    "ltc": "litecoin",
    "matic": "polygon",
    "xlm": "stellar",
    "busd": "binance usd",
    "sol": "solana",
    "vet": "vechain",
    "etc": "ethereum classic",
}

# converting symbols to currency names

updated_list = []
for x in new_list:
    if x in conversion.keys():
        updated_list.append(conversion[x])
    else:
        updated_list.append(x)

# displaying curencies and count

from collections import Counter

final_list = Counter(sorted(updated_list)).most_common()

# st.write(final_list)

final_list = final_list[:5]  # selecting the top 5 currencies

x_val = [x[0] for x in final_list]
y_val = [x[1] for x in final_list]

# displaying bar plot
fig, ax = plt.subplots()
ax.bar(x_val, y_val, color="cyan")
plt.xlabel("Currencies")
plt.ylabel("Count of mention in comments", fontsize=12)
plt.title("Top 5 most mentioned currencies and their count", fontsize=15)
plt.xticks(rotation=90, fontsize=15)
plt.figure(figsize=(1, 1))
st.pyplot(fig)
