# pd_read_html_noon.py



# Read noon.com html using pandas to find the tables with the parfum specifications


# Imports

from tqdm import tqdm
import pandas as pd
from functools import reduce
from timeit import default_timer as timer


# Start timer

start = timer()


# Import the dataframe with the links to scrape

df = pd.read_csv("noon_parfum_links.csv")
links = df["link"].to_list()
names = df["name"].to_list()

# We can use a shorter slice of the list just for trial and error, without having to wait hours for all of the scraping to be done (and maybe have an error)

#links = links[0:10] # Increment these list slices for gradual testing, then try to scrape them all
#names = names[0:10]

# Loop through the list of links and names to read the tables on those pages, keep track of the links and names to merge with other scraped data, 
# append the dataframes to a list, and then concatenate the list of all of the dfs so they can be merged with the other scraped data, elsewhere

# Due to this error, we will wrap this for loop in a try and except block (apparently not every parfum page has 2 tables, some probably dont even have any)
"""
df1 = df[1]
IndexError: list index out of range
"""

# List of dataframes we will append each dataframe to, so we can concatenate them all at the end

dfs = []

# A set for all of the unique columns

cs = set()

# Note: We are just wrapping the lists of links and names with 'tqdm' which is a package that tracks the progress of for loops, for convenience

# Fun Fact: tqdm derives from the Arabic word taqaddum (تقدّم) which can mean “progress,” and is an abbreviation for “I love you so much” in Spanish (te quiero demasiado).
# https://pypi.org/project/tqdm/

for link, name in zip(tqdm(links), tqdm(names)):

    try:

        df = pd.read_html("https://www.noon.com/" + link)
    
        # Index the list to create two separate dataframes
    
        df0 = df[0]
        df1 = df[1]
    
        # Concatenate the dataframes
    
        df = pd.concat([df0, df1], ignore_index=True)
    
        # Transpose the concatenated dataframe, use the first row as column headers, then drop the first row
    
        df2 = df.T
        df2.columns = df2.iloc[0]
        df2 = df2.iloc[1:]

        # Reset the index to avoid duplicate index error

        df2 = df2.reset_index(drop=True)
    
        # Add the link and name to the df for future merging
    
        df2["link"] = link
        df2["name"] = name

        # Get rid of any duplicate indexes, otherwise there will be an error in concatenation

        df2 = df2.loc[~df2.index.duplicated(keep='first')]

        # Convert all of the columns to string type, for easier handling later

        cols = df2.columns.values.tolist()
        df2[cols] = df2[cols].astype(str)

        # Add all of the column names to a set, so there are no duplicates, and we can print all of the unique column names at the end

        for c in cols:
            cs.add(c)

        # Append the dataframe to the list of dataframes so they can be concataned after scraping is complete

        dfs.append(df2)

    # If there is an Exception, ie: an Error like the IndexError mentioned above, the Error will be printed 
    # The Error could also be "logged", but we don't really need to, the error exists simply because the data does not exist on the webpage
    # "continue" means the loop will continue to loop, it just goes to the next iteration

    except Exception as e:
        print(e)
        continue


# [2:06:42<00:04,  4.94s/it] ... whoops
"""pandas.errors.InvalidIndexError: Reindexing only valid with uniquely valued Index objects"""
# It's not great to get an error at the end of 2 hours of scraping, another lesson learned (I thought ignore_index=True would be fine), so we can google the error, and take the first SO
# https://stackoverflow.com/questions/35084071/concat-dataframe-reindexing-only-valid-with-uniquely-valued-index-objects


# Set the index on 'name' for each dataframe, concatenate all of the dataframes along the rows, and save the data to csv
# (We could also have created an original dataframe with column names and appended the the data as a dictionary, but this concat should handle unknown column differences easier)

dfss = [df.set_index('name') for df in dfs]
parfums = pd.concat(dfss, axis=0)
parfums.to_csv("noon_parfum_notes.csv")


# Print the set of column names, so we can see all of the unique column names from all of the webpages

print(cs)
"""
{nan, 'Size', 'Shipping Weight', 'Irritation Free', 'Tope Note', 'Package Type', 'Olfactive Family', 'Fragrance Note', 'link', 'Base Note', 'Height', 'Top notes', 'Scent Note', 'Country Of Origin', 'Package weight', 'Package weight in KGs', 'Recommended Usage', 'Application Area', 'Suitable for the season', 'Fragrance Classification', 'Scent', 'Product Dimension', 'Container Type', "What's In The Box", 'Sulfate Free', 'Fragrance Family', 'Scent/Notes', 'name', 'Introduced Year', 'Model Name', 'Scent Notes', 'Department', 'Long-Lasting', 'Lanched', 'Fragrance', 'Notes Contains', 'Top Note', 'Fragnance Family', 'Width', 'Notes Available', 'Package thickness', 'Ingredients', 'Launched', 'Long Lasting', 'scents_notes', 'Grade', 'Long-lasting', 'Middle / Heart Notes', 'Fragrance Segment', 'Colour Name', 'Heart/Middle Note', 'Scents/Notes', 'Anti-perspirant', 'Longlasting', 'Form', 'Country of Origin', 'Fragrance Notes', 'Set Includes', 'Colour Family', 'Cruelty Free', 'Middle Note', 'Scent Life', 'Composition', 'Skin type', 'Model Number', 'Material', 'Fragrance Note Family', 'Package height', 'Package Width', 'Suitable For', 'Volume', 'Product Height', 'Packaging Type', 'Formulation', 'Perfumer', 
Dimensions', 'Depth', 'Fragrance Category', 'Dimension', 'Note', 'Key Notes', 'Includes', 'Dispenser Type', 'Non-toxic', 'Weight', 'Notes', 'Aromatherapy Type', 'Scent Type', 'Occasion', 'Paraben Free', 'Product Width/Depth', 'Anti-Perspirant', 'Base notes', 'Paraben/Sulphate Free', 'Fragrance Type', 'Cruelty-free', 'Scent Family', 'Product Line', 'Skin Type', 'Perfume Scent', 'Product Dimensions', 'Scents'}
"""


# Stop timer

Runtime = timer() - start # in seconds

print("Runtime:", Runtime) # 7355.8862703 seconds = 2:02:20, also seen from tqdm output


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Original code for testing the concept before creating the for loop, incremental steps are helpful for building our scraping tool

#df = pd.read_html("https://www.noon.com/uae-en/arezza-flussi-edp-100ml/N45412662A/p?o=e2310ab2e6790b8c") # NO NOTES - some parfums do not have notes
#df = pd.read_html("https://www.noon.com/uae-en/pianissimo-edp-50ml/N11074521A/p?o=c6a3fc88e4aead9c") # Some parfums do have notes
#
## Inspect the list of dataframes
#
#print(df[0])
#print(df[1])
#
## Index the list to create two separate dataframes
#
#df0 = df[0]
#df1= df[1]
#
## Concatenate the dataframes
#
#df = pd.concat([df0, df1], ignore_index=True)
#print(df)
#
## Transpose the concatenated dataframe, use the first row as column headers, then drop the first row
#
#df2 = df.T
#df2 = df2.rename(columns=df2.iloc[0])
#df2 = df2.iloc[1:]
#print(df2)


# Additional planning for next steps

## This can be created into a function, and we can use pandas read_html to scrape all of Specifications tables using the urls that we get with scrapy (we keep it separate, here, no function necessary)
## We will also want to add another two columns to each dataframe for the parfum name and url so when we scrape the parfum specs we can keep track of the name and url with this new data
