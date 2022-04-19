#1clean_links_df.py



# Clean the links which were scraped by 0get_parfum_links.py


# Imports

import pandas as pd

df = pd.read_csv("noon_parfum_links.csv")

df["name"] = df["name"].str.replace("<span>","")
df["name"] = df["name"].str.replace("<!-- -->","")
df["name"] = df["name"].str.replace("</span>","")

print(df)
df.to_csv("noon_parfum_links.csv")
