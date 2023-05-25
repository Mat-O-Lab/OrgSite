import pandas as pd
import os

# use pandas to read the markdown table
file_path = os.path.join(os.path.dirname(__file__), "events.md")
df = pd.read_csv(file_path, skiprows=14, sep='|').dropna(axis=1,how='all')
df.columns = df.columns.str.strip()
df.drop(index=df.index[0], axis=0, inplace=True)

print(df)
for _, row in df.iterrows():
    print(row)
    filename = f'{row["date"].strip()}-{row["title"].strip().replace(" ", "-")}.md'
    file_path= os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'w') as f:
        f.write(f"""---
layout: post
title: {row.title.strip().replace(':',' -')}
subtitle: {row.subtitle.strip().replace('"', '').replace(':',' -')}
categories: {row.categories.strip()}
tags: {row.tags.strip().split(', ')}
---

## {row.subtitle.strip().replace('"', '')} {row.title.strip()} [^fn1]

{row.text.strip()}

[^fn1]: [source]({row.link.strip()})""")
